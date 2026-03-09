import os

filepath = 'modules/unified_module_blueprint.md'

markdown_table = """

## Sandman Universal Nomenclature Reference

This reference outlines the unified naming conventions used across the Sandman ecosystem. The names are consistent across all module interfaces, but their context changes depending on where they are used.

### Context Interfaces

*   **Config File**: The keys used in `config.json` (or `config.yml`) to define module behavior and default jobs.
*   **CLI Flag**: The command-line arguments used to execute a module directly from the terminal.
*   **Python**: The argument variables or dictionary keys used when running a module as an imported Python class.
*   **Markdown Frontmatter**: The structured metadata block at the top of generated `.md` files.
*   **JSON Data**: The properties within the generated raw `.json` output files.

---

### 1. Sourcing & Identification

These variables define **where** data is coming from and **what** it is called.

| Name | Interface Usage | Description |
| :--- | :--- | :--- |
| **`source`** | Config / CLI (`--source`) / Python | The platform or sub-community being targeted (e.g., 'news', 'linkedin'). |
| | Frontmatter / JSON | Identifies the origin of the scraped post. |
| **`post_id`** | Frontmatter / JSON | A unique identifier derived from the source platform's own ID system. |
| **`post_URL`** | Frontmatter / JSON | The direct web link to the original content on the source platform. |
| **`poster`** | Frontmatter / JSON | The author, OP, or entity that created the post (e.g., 'employer_name'). |
| **`module`** | Frontmatter / JSON | The Sandman module that generated the file (e.g., 'reddit2md'). |

---

### 2. Search & Filtering

These variables define **how** to query the source and **what** to ignore.

| Name | Interface Usage | Description |
| :--- | :--- | :--- |
| **`query`** | Config / CLI (`--query`) / Python | The main search term (used predominantly in job or web scrapers). |
| **`min_score`** | Config / CLI (`--min-score`) / Python | The minimum score or upvotes required to process a post. |
| **`blacklist_terms`** | Config / CLI (`--blacklist-terms`) / Python | List of keywords. If found in the title/body, the post is skipped. |
| **`blacklist_urls`** | Config / CLI (`--blacklist-urls`) / Python | List of domain fragments to ignore when capturing links. |
| **`min_age_hours`** | Config / CLI (`--min-age-hours`) / Python | Minimum time a post must exist before it is considered mature. |
| **`max_age_hours`** | Config / CLI (`--max-age-hours`) / Python | Maximum age for a post to be considered fresh/relevant. |

---

### 3. Limits & Data Management

These variables dictate the **size** and **retention** of your data footprint.

| Name | Interface Usage | Description |
| :--- | :--- | :--- |
| **`max_results`** | Config / CLI (`--max-results`) / Python | The maximum number of new items to fetch during a single run. |
| **`db_limit`** | Config / CLI (`--db-limit`) / Python | Footprint control. The maximum number of records to keep in the SQLite cache. |
| **`save_json`** | Config / CLI (`--save-json`) / Python | Boolean. Whether to save a sanitized `.json` copy alongside the markdown. |
| **`md_log`** | Config / CLI (`--md-log`) / Python | Boolean. Whether to append run results to the human-readable Scrape Log. |

---

### 4. Categorization & Output Formatting

These variables define how the data is **presented** and **organized** locally.

| Name | Interface Usage | Description |
| :--- | :--- | :--- |
| **`label`** | Config / CLI (`--label`) / Python | Custom user-defined categorization override (formerly 'flair'). |
| | Frontmatter / JSON | Classifications provided by the source or overridden by the user. |
| **`group_by_source`** | Config / CLI (`--group-by-source`) / Python | Boolean. Whether to create sub-folders for each source (e.g., `/reddit/news/`). |
| **`detail`** | Config / CLI (`--detail`) / Python | Controls output depth (e.g., capturing XS vs XL comment trees). |
| **`sort`** | Config / CLI (`--sort`) / Python | The sorting method applied to the source feed (e.g., 'new', 'top'). |
| **`post_links`** | Frontmatter / JSON | A list of all external URLs found within the content. |
| **`date_posted`** | Frontmatter / JSON | The original publication timestamp of the post. |
| **`date_scraped`**| Frontmatter / JSON | The timestamp of when Sandman extracted the data. |

"""

with open(filepath, 'a', encoding='utf-8') as f:
    f.write(markdown_table)

print("Appended successfully.")
