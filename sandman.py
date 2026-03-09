import yaml
import argparse
import sys
import os

# Add modules directory to path so we can import modules by name
sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))

def load_config(config_path):
    if not os.path.exists(config_path):
        print(f"[!] No config found at {config_path}")
        return None
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)

def run_job(job_config, global_defaults):
    module_name = job_config.get("module")
    job_name = job_config.get("name", "Untitled Job")
    
    print(f"\n--- Running Job: {job_name} (Module: {module_name}) ---")
    
    # Merge global defaults with job-specific overrides
    settings = global_defaults.copy()
    settings.update(job_config)

    # Dispatch to the correct module
    if module_name == "reddit":
        try:
            from reddit2md.reddit2md import RedditScraper
            scraper = RedditScraper()
            # RedditScraper's run() method handles the dictionary of overrides
            scraper.run(source=settings.get("source"), overrides=settings)
        except ImportError:
            print("[!] Error: Could not import reddit2md. Ensure it's in the modules folder.")
        except Exception as e:
            print(f"[!] Error in Reddit job: {e}")

    elif module_name == "jobs":
        try:
            from job2md.job2md import JobScraper
            scraper = JobScraper(overrides=settings)
            scraper.run()
        except ImportError:
            print("[!] Error: Could not import job2md. Ensure it's in the modules folder.")
        except Exception as e:
            print(f"[!] Error in Jobs job: {e}")

    else:
        print(f"[!] Warning: Unknown module '{module_name}'. Skipping job.")

def main():
    parser = argparse.ArgumentParser(description="Sandman Master Orchestrator")
    parser.add_argument("--config", default="config.yml", help="Path to master config")
    parser.add_argument("--debug", type=bool, help="Global debug override")
    
    args = parser.parse_args()
    
    config = load_config(args.config)
    if not config:
        return

    global_defaults = config.get("global_defaults", {})
    jobs = config.get("jobs", [])

    if not jobs:
        print("[!] No jobs defined in config. Done.")
        return

    print(f"🚀 Sandman Nightly Worker started. Processing {len(jobs)} jobs...")
    
    for job in jobs:
        run_job(job, global_defaults)

    print("\n✨ All jobs complete. Nightly cycle finished.")

if __name__ == "__main__":
    main()
