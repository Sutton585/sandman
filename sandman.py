import yaml
import argparse
import sys
import os

# Add modules directory to path so we can import modules by name
sys.path.append(os.path.join(os.path.dirname(__file__), 'modules'))

def load_config(config_path):
    if not os.path.exists(config_path):
        print(f"No config found at {config_path}")
        return None
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)

def run_task(task_config, base_settings):
    module_name = task_config.get("module")
    task_name = task_config.get("name", "Untitled Task")
    
    verbose = base_settings.get("verbose", 2)
    if verbose >= 1:
        print(f"\nRunning Task: {task_name} (Module: {module_name})")
    
    # Merge base settings with task-specific overrides
    settings = base_settings.copy()
    settings.update(task_config)

    # Apply group_by_module logic
    if settings.get("group_by_module", True) and module_name:
        if "md_output_directory" in settings:
            settings["md_output_directory"] = os.path.join(settings["md_output_directory"], module_name)
        if "json_output_directory" in settings:
            settings["json_output_directory"] = os.path.join(settings["json_output_directory"], module_name)

    # Dispatch to the correct module
    if module_name == "reddit":
        try:
            from reddit2md.reddit2md import RedditScraper
            scraper = RedditScraper()
            # RedditScraper's run() method handles the dictionary of overrides
            scraper.run(source=settings.get("source"), overrides=settings)
        except ImportError:
            print("Error: Could not import reddit2md. Ensure it's in the modules folder.")
        except Exception as e:
            print(f"Error in Reddit task: {e}")

    elif module_name == "jobs":
        try:
            from jobs2md.jobs2md import JobScraper
            scraper = JobScraper(overrides=settings)
            scraper.run()
        except ImportError:
            print("Error: Could not import jobs2md. Ensure it's in the modules folder.")
        except Exception as e:
            print(f"Error in Jobs task: {e}")

    else:
        print(f"Warning: Unknown module '{module_name}'. Skipping task.")

def main():
    parser = argparse.ArgumentParser(description="Sandman Master Orchestrator")
    parser.add_argument("--config", default="config.yml", help="Path to master config")
    parser.add_argument("--debug", type=bool, help="Global debug override")
    parser.add_argument("--verbose", type=int, choices=[0, 1, 2], help="Verbosity level (0: errors, 1: warnings, 2: all/debug)")
    
    args = parser.parse_args()
    
    config = load_config(args.config)
    if not config:
        return

    base_settings = config.get("settings", {})
    if args.verbose is not None:
        base_settings["verbose"] = args.verbose
    routine = config.get("routine", [])

    if not routine:
        print("No routine defined in config. Done.")
        return

    verbose = base_settings.get("verbose", 2)
    if verbose >= 1:
        print(f"Sandman Orchestrator started. Processing {len(routine)} tasks in routine...")
    
    for task in routine:
        run_task(task, base_settings)

    if verbose >= 1:
        print("\nAll tasks complete. Execution cycle finished.")

if __name__ == "__main__":
    main()