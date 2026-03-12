import os
import yaml
import json

# 1. Convert reddit2md config.json to config.yml
reddit_json_path = 'modules/reddit2md/config.json'
reddit_yaml_path = 'modules/reddit2md/config.yml'

if os.path.exists(reddit_json_path):
    with open(reddit_json_path, 'r') as f:
        data = json.load(f)
    
    # Rename 'jobs' to 'routine'
    if 'jobs' in data:
        data['routine'] = data.pop('jobs')
    
    with open(reddit_yaml_path, 'w') as f:
        yaml.dump(data, f, default_flow_style=False)
    
    os.remove(reddit_json_path)
    print(f"Converted {reddit_json_path} to {reddit_yaml_path}")

# 2. Update jobs2md config.yml nomenclature
job_yaml_path = 'modules/jobs2md/config.yml'
if os.path.exists(job_yaml_path):
    with open(job_yaml_path, 'r') as f:
        data = yaml.safe_load(f)
    
    if 'settings' in data:
        gd = data['settings']
        mapping = {
            'site_name': 'source',
            'results_wanted': 'max_results',
            'hours_old': 'max_age_hours'
        }
        new_gd = {}
        for k, v in gd.items():
            new_gd[mapping.get(k, k)] = v
        data['settings'] = new_gd
    
    with open(job_yaml_path, 'w') as f:
        yaml.dump(data, f, default_flow_style=False)
    print(f"Updated nomenclature in {job_yaml_path}")

