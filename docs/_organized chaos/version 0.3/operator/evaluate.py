import os
import json
import argparse
from pathlib import Path
import litellm

# Load configuration
def load_config(config_path="config.json"):
    with open(config_path, "r") as f:
        return json.load(f)

def read_file(filepath):
    with open(filepath, "r") as f:
        return f.read()

def write_markdown_evaluation(eval_dir, filename, eval_json, jd_content):
    output_path = Path(eval_dir) / f"eval_{filename}"
    
    # Parse JSON if it's a string
    if isinstance(eval_json, str):
        try:
            # Strip potential markdown formatting if the model ignored the instruction
            clean_json = eval_json.strip()
            if clean_json.startswith("```json"):
                clean_json = clean_json[7:]
            if clean_json.startswith("```"):
                clean_json = clean_json[3:]
            if clean_json.endswith("```"):
                clean_json = clean_json[:-3]
            eval_data = json.loads(clean_json.strip())
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON for {filename}: {e}")
            eval_data = {"error": "Failed to parse JSON", "raw_output": eval_json}
    else:
        eval_data = eval_json

    markdown_content = f"""---
traditional_fit_score: {eval_data.get('traditional_fit_score', 0)}
arbitrage_score: {eval_data.get('arbitrage_score', 0)}
recommended_action: "{eval_data.get('recommended_action', 'research')}"
primary_archetype: "{eval_data.get('primary_archetype', 'NONE')}"
anti_pattern_flags: {json.dumps(eval_data.get('anti_pattern_flags', []))}
green_flags: {json.dumps(eval_data.get('green_flags', []))}
missing_skills: {json.dumps(eval_data.get('missing_skills', []))}
transferable_skills: {json.dumps(eval_data.get('transferable_skills', []))}
---

# Evaluation: {filename}

## Reasoning
**Traditional Fit:** {eval_data.get('fit_reasoning', '')}

**Arbitrage / Exploitation Potential:** {eval_data.get('arbitrage_reasoning', '')}

## Website Strategy
{eval_data.get('website_strategy', '')}

---
## Original Job Description
{jd_content}
"""
    with open(output_path, "w") as f:
        f.write(markdown_content)
    print(f"✅ Evaluated: {filename} -> {output_path}")

def evaluate_jobs(force=False):
    config = load_config()
    inbox_dir = Path(config["inbox_dir"])
    eval_dir = Path(config["evaluations_dir"])
    
    # Ensure directories exist
    inbox_dir.mkdir(exist_ok=True)
    eval_dir.mkdir(exist_ok=True)
    
    profile_content = read_file(config["profile_path"])
    prompt_template = read_file(config["prompt_template_path"])
    
    model = config["llm_provider"]
    temperature = config["temperature"]

    files_to_process = list(inbox_dir.glob("*.md"))
    if not files_to_process:
        print("Inbox is empty. Drop Job Description markdown files into operator/inbox/.")
        return

    for jd_file in files_to_process:
        output_filename = f"eval_{jd_file.name}"
        output_path = eval_dir / output_filename
        
        if output_path.exists() and not force:
            print(f"⏭️ Skipping {jd_file.name} (already evaluated). Use --force to re-evaluate.")
            continue
            
        print(f"🔍 Evaluating {jd_file.name}...")
        jd_content = read_file(jd_file)
        
        prompt = prompt_template.format(
            profile=profile_content,
            job_description=jd_content
        )
        
        try:
            response = litellm.completion(
                model=model,
                messages=[{"role": "user", "content": prompt}],
                temperature=temperature,
            )
            
            result_content = response.choices[0].message.content
            write_markdown_evaluation(eval_dir, jd_file.name, result_content, jd_content)
            
        except Exception as e:
            print(f"❌ Error evaluating {jd_file.name}: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Operator Phase 0 Job Evaluator")
    parser.add_argument("--force", action="store_true", help="Force re-evaluation of already scored files")
    args = parser.parse_args()
    
    evaluate_jobs(force=args.force)
