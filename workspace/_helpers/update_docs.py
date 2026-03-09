import re

def update_file(filepath, new_to_ai, new_body):
    with open(filepath, 'r') as f:
        content = f.read()
    
    parts = content.split('---', 2)
    if len(parts) >= 3:
        front_matter = parts[1]
        front_matter = re.sub(r'TO-AI:.*', f'TO-AI: |\n{new_to_ai}\n', front_matter, flags=re.DOTALL)
        new_content = f"---{front_matter}---{new_body}"
        
        with open(filepath, 'w') as f:
            f.write(new_content)

new_nom_to_ai = """  Your task is to maintain a hyper-organized, easily navigable nomenclature dictionary that translates Sandman's universal orchestration variables into the specific parameters used by underlying modules (like JobSpy and reddit2md).
  
  What you need to do:
  1. Keep this document strictly organized by the Sandman Standard Variable name, not by the module. Sandman is the source of truth.
  2. Clearly list what each standard variable maps to in JobSpy (job2md) and reddit2md (reddit2md).
  3. Maintain the standardized markdown front-matter schema for all generated text files.
  
  How to accomplish it:
  - Do not use bold markdown formatting anywhere in markdown files.
  - Keep the lists clean, scannable, and easy for a developer to reference when building a universal config file.
  - If a variable only applies to one module, explicitly state that it maps to 'N/A' or is 'Filtered by Sandman wrapper' for the other.
  
  End result:
  A clean, authoritative reference document that defines exactly what every variable is called in Sandman and how it translates to the individual scraping modules.
  
  Left to do:
  Add equivalent mappings for upcoming modules (like gmail2md or Facebook Marketplace scrapers) as they are integrated into the Sandman ecosystem."""

new_nom_body = """
# Sandman Universal Nomenclature Standard

This document establishes the unified naming conventions across the Sandman ecosystem. Sandman orchestration translates these universal standard variables down into the specific parameters required by individual modules (like reddit2md for Reddit, or job2md using JobSpy). 

All scraped entities are universally referred to as "posts" or "records".

## 1. Universal Configuration Variables

These are the public-facing variables users can set in Sandman config files. Sandman maps them to the respective module parameters.

### Search and Sourcing

* query
  * Used for: The primary search term.
  * Maps to JobSpy: search_term
  * Maps to reddit2md: N/A (reddit2md relies on source instead of search query)

* source
  * Used for: The platform, sub-community, or job board being targeted.
  * Maps to JobSpy: site_name (e.g., linkedin, indeed)
  * Maps to reddit2md: subreddit (must strip out any r/ or /r/ prefixes)

* group_by_source
  * Used for: Creating subfolders in the output directory for each source.
  * Maps to JobSpy: Handled by Sandman to put Indeed jobs in an "indeed" folder, etc.
  * Maps to reddit2md: Subreddit Folders

* location
  * Used for: Geographic search area.
  * Maps to JobSpy: location
  * Maps to reddit2md: N/A

* distance
  * Used for: Radius from the target location in miles.
  * Maps to JobSpy: distance
  * Maps to reddit2md: N/A

* job_type
  * Used for: Employment classification (fulltime, parttime, internship, contract).
  * Maps to JobSpy: job_type
  * Maps to reddit2md: N/A

* is_remote
  * Used for: Filtering for remote-only opportunities.
  * Maps to JobSpy: is_remote
  * Maps to reddit2md: N/A

### Limits and Data Retention

* max_results
  * Used for: The upper limit of items to retrieve or process.
  * Maps to JobSpy: results_wanted
  * Maps to reddit2md: Post Limit

* max_db_records
  * Used for: Footprint control for the SQLite cache. Oldest records are pruned.
  * Maps to JobSpy: Handled by Sandman wrapper
  * Maps to reddit2md: Maximum DB Records

* save_json
  * Used for: Persisting the raw or sanitized JSON data to the data directory.
  * Maps to JobSpy: Handled by Sandman wrapper
  * Maps to reddit2md: Save JSON

* enable_md_log
  * Used for: Appending run results to a human-readable markdown log.
  * Maps to JobSpy: Handled by Sandman wrapper
  * Maps to reddit2md: Update Scrape Log

### Filtering and Quality Control

* min_age_hours
  * Used for: The minimum time a post must exist before it is considered mature.
  * Maps to JobSpy: N/A (jobs are typically wanted fresh)
  * Maps to reddit2md: Minimum Post Age Hours

* max_age_hours
  * Used for: The maximum age of a post to be considered relevant.
  * Maps to JobSpy: hours_old
  * Maps to reddit2md: N/A

* blacklist_terms
  * Used for: List of keywords that will skip or exclude a post if found in the title or body.
  * Maps to JobSpy: Filtered by Sandman wrapper
  * Maps to reddit2md: Filter Keywords

* blacklist_urls
  * Used for: Domains or URL fragments to exclude.
  * Maps to JobSpy: Filtered by Sandman wrapper
  * Maps to reddit2md: URL Blacklist

* easy_apply
  * Used for: Filtering for jobs hosted directly on the job board.
  * Maps to JobSpy: easy_apply
  * Maps to reddit2md: N/A

### Formatting and Output Control

* verbosity
  * Used for: Controls the detail level of logging and data capture.
  * Maps to JobSpy: verbose (0 for errors, 1 for warnings, 2 for all)
  * Maps to reddit2md: Comment Detail Presets (Translates integer to XS, SM, MD, LG, XL)

* output_filetype
  * Used for: Determining the format of the extracted description.
  * Maps to JobSpy: description_format (markdown, html)
  * Maps to reddit2md: Always markdown

* debug
  * Used for: Enabling developer debug modes.
  * Maps to JobSpy: Handled by Sandman wrapper logging
  * Maps to reddit2md: Debug

### Advanced and Developer Edge Cases

* proxies
  * Used for: List of proxy servers to round-robin through.
  * Maps to JobSpy: proxies
  * Maps to reddit2md: Handled by Sandman wrapper if needed

* user_agent
  * Used for: Overriding the default browser user agent.
  * Maps to JobSpy: user_agent
  * Maps to reddit2md: Handled by Sandman wrapper

* auth_cert
  * Used for: Path to a CA Certificate file for network authentication.
  * Maps to JobSpy: ca_cert
  * Maps to reddit2md: N/A

* offset
  * Used for: Starting a search from a specific pagination index.
  * Maps to JobSpy: offset
  * Maps to reddit2md: N/A

* sort
  * Used for: Sorting method for the platform feed.
  * Maps to JobSpy: N/A
  * Maps to reddit2md: Reddit Sort Method (new, hot, top, rising)

* fetch_full_description
  * Used for: Fetching complete descriptions when not provided by default feeds.
  * Maps to JobSpy: linkedin_fetch_description
  * Maps to reddit2md: N/A

* employer_id
  * Used for: Searching for records posted by specific corporate IDs.
  * Maps to JobSpy: linkedin_company_ids
  * Maps to reddit2md: N/A

* target_country
  * Used for: Platform-specific country filtering.
  * Maps to JobSpy: country_indeed
  * Maps to reddit2md: N/A

* enforce_annual_salary
  * Used for: Normalizing wage data to an annual figure.
  * Maps to JobSpy: enforce_annual_salary
  * Maps to reddit2md: N/A

* query_google
  * Used for: Search term specific to Google jobs edge case.
  * Maps to JobSpy: google_search_term
  * Maps to reddit2md: N/A

## 2. Standardized Markdown Front-Matter Schema

Every markdown file generated by Sandman must adhere to this standardized front-matter schema. Note that we do not use the 'tags' parameter, as it interferes with standard Obsidian tagging.

* post_id
  * Description: A unique identifier derived consistently (e.g. source + URL ID).

* post_url
  * Description: The direct link to the original content. Replaces 'source_url' or 'Post Link'.

* source
  * Description: The platform or sub-community where the post originated. Replaces 'subreddit' or 'site_name'.

* module
  * Description: The specific Sandman module that executed the scrape (e.g. job2md, reddit2md).

* author
  * Description: The entity that created the post (e.g. employer company name for jobs, original poster for Reddit).

* category
  * Description: Classifications or labels provided by the source. Replaces 'metadata_label' or 'Flair'.

* time_posted
  * Description: The original publication timestamp. Replaces 'post_date'.

* time_scraped
  * Description: The timestamp of the Sandman extraction. Replaces 'scrape_date'.
"""

update_file('docs/nomenclature.md', new_nom_to_ai, new_nom_body)

