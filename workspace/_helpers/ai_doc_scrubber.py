import argparse
import os
import re
import json
import time
from pathlib import Path

try:
    from google import genai
    from google.genai import types
    HAS_GENAI = True
except ImportError:
    HAS_GENAI = False

def find_markdown_files(root_dir):
    ignore_dirs = {'.git', 'venv', 'node_modules', '__pycache__', '.pytest_cache'}
    ignore_files = {'nomenclature2.md', 'tasks.md'}
    
    md_files = []
    for dirpath, dirnames, filenames in os.walk(root_dir):
        dirnames[:] = [d for d in dirnames if d not in ignore_dirs]
        for f in filenames:
            if f.endswith('.md') and f not in ignore_files:
                md_files.append(Path(dirpath) / f)
    return md_files

def extract_paragraphs(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Strip YAML front matter to avoid modifying historical notes or metadata
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            content = parts[2] # Keep only the body
            
    # Split by double newline to get blocks/paragraphs
    blocks = re.split(r'\n\s*\n', content)
    return [b.strip() for b in blocks if b.strip()]

def analyze_with_gemini(client, block, target_terms, new_term, context):
    prompt = f"""
    You are an expert technical writer and software architect.
    
    We are updating our documentation.
    Old terms: {', '.join(target_terms)}
    New term: {new_term}
    New functionality context: {context}
    
    Please read the following documentation excerpt:
    '''
    {block}
    '''
    
    1. Determine if it describes the old variable or old functionality, or if it is already correct.
    2. Determine if the current text conflicts with the new functionality context.
    3. If it is inaccurate or uses the old term, rewrite it to use the new term and accurately describe the new functionality.
    
    Return a JSON object strictly matching this schema:
    {{
        "is_inaccurate": true/false,
        "reason": "explanation of why it is inaccurate or accurate",
        "proposed_rewrite": "the rewritten markdown text (or null if already accurate)"
    }}
    """
    try:
        response = client.models.generate_content(
            model='gemini-2.5-flash',
            contents=prompt,
            config=types.GenerateContentConfig(
                response_mime_type="application/json",
            )
        )
        return json.loads(response.text)
    except Exception as e:
        print(f"Error calling Gemini: {e}")
        return None

def main():
    parser = argparse.ArgumentParser(description="AI-Assisted Documentation Scrubber")
    parser.add_argument('--task-id', required=True, help="Task identifier (e.g., Task_1, Task_7)")
    parser.add_argument('--target-terms', required=True, help="Comma-separated list of old variable names")
    parser.add_argument('--new-term', required=True, help="The standardized variable name")
    parser.add_argument('--context', required=True, help="String describing how the logic/functionality has changed")
    parser.add_argument('--workspace-root', default=".", help="Root directory to scan")
    
    args = parser.parse_args()
    target_terms = [t.strip().lower() for t in args.target_terms.split(',')]
    
    # Ensure reports directory exists
    reports_dir = os.path.join("workspace", "_helpers", "task_reports")
    os.makedirs(reports_dir, exist_ok=True)
    report_path = os.path.join(reports_dir, f"{args.task_id}_impact_report.md")
    
    if not HAS_GENAI:
        print("Warning: google-genai package is not installed. Please `pip install google-genai`.")
        print("We will still extract the matching contexts into the report, but AI rewrites will be skipped.")
        client = None
    else:
        if not os.environ.get("GEMINI_API_KEY"):
            print("Warning: GEMINI_API_KEY environment variable not set.")
            print("We will still extract the matching contexts into the report, but AI rewrites will be skipped.")
            client = None
        else:
            client = genai.Client()

    md_files = find_markdown_files(args.workspace_root)
    matches = []

    for file_path in md_files:
        paragraphs = extract_paragraphs(file_path)
        for i, block in enumerate(paragraphs):
            block_lower = block.lower()
            if any(term in block_lower for term in target_terms):
                matches.append((file_path, i, block))

    # Build Front-Matter
    report_content = f"---\n"
    report_content += f"task: {args.task_id}\n"
    report_content += f"status: Pending Review\n"
    report_content += f"target_terms: [{', '.join(target_terms)}]\n"
    report_content += f"new_term: {args.new_term}\n"
    report_content += f"context: \"{args.context}\"\n"
    report_content += f"date_generated: {time.strftime('%Y-%m-%d %H:%M:%S')}\n"
    report_content += f"---\n\n"
    
    report_content += f"# Documentation Scrubbing Report for {args.task_id}\n\n"
    report_content += "> **Instructions**: Review the `AI Analysis` and `Proposed Rewrite` for each block below. If accurate, apply the rewrite to the source file.\n\n"
    report_content += "---\n\n"

    for file_path, idx, block in matches:
        report_content += f"## File: `{file_path}` (Block #{idx+1})\n"
        report_content += f"**Original:**\n```markdown\n{block}\n```\n\n"
        
        if client:
            print(f"Analyzing block in {file_path}...")
            analysis = analyze_with_gemini(client, block, target_terms, args.new_term, args.context)
            if analysis:
                report_content += f"**AI Analysis:**\n"
                report_content += f"- **Is Inaccurate?**: {analysis.get('is_inaccurate')}\n"
                report_content += f"- **Reason**: {analysis.get('reason')}\n\n"
                if analysis.get('is_inaccurate') and analysis.get('proposed_rewrite'):
                    report_content += f"**Proposed Rewrite:**\n```markdown\n{analysis.get('proposed_rewrite')}\n```\n\n"
        else:
            report_content += f"**AI Analysis:** Skipped (No client)\n\n"
            
        report_content += "---\n\n"
        
    with open(report_path, 'w', encoding='utf-8') as f:
        f.write(report_content)
        
    print(f"Report generated at {report_path}")

if __name__ == "__main__":
    main()