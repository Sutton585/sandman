# Shortcut used to feed into the appscript/google sheets project:



## Action 1: Get current web page from safari
creates: {Variable: Web Page}

## Action 2: Run AppleScript
using input: {Variable: Web Page}
creates: {variable: AppleScript_Output}

```applescript
on run {input, parameters}
    tell application "Safari"
        set pageText to text of front document
        set pageURL to URL of front document
    end tell
    
    -- This script now ONLY gets the raw data and formats it.
    -- All cleaning and parsing will be done in the Python script.
    set combinedOutput to "<properties>
" & "source_URL: " & pageURL & "
" & "</properties>



" & pageText
    
    return combinedOutput
end run
```
## Action 3: Run Shell Script (python)
using input: {variable: AppleScript_Output}
creates: {variable: Python_Output}

```python
import sys
import re

def extract_property(content, regex_pattern):
    """A helper function to find a value in text using Regex."""
    match = re.search(regex_pattern, content, re.MULTILINE | re.IGNORECASE)
    if match and match.group(1):
        # Return the first captured group, stripped of HTML tags and whitespace
        clean_text = re.sub('<[^<]+?>', '', match.group(1))
        return clean_text.strip()
    return "" # Return empty if not found

def scrape_linkedin(content, url, source):
    """Scrapes data specifically from a LinkedIn job posting."""
    print(">>> Running LinkedIn Scraper...", file=sys.stderr) # Debug message
    
    # --- Step 1: Find all data from the original content ---
    job_title, company, location = "", "", ""
    lines = content.splitlines()
    share_line_index = -1

    # Find the "Share" line, which is our main anchor
    for i, line in enumerate(lines):
        if line.strip().lower() == "share":
            share_line_index = i
            break
    
    # If we found the anchor, extract the data relative to it
    if share_line_index != -1:
        company_line_index = share_line_index - 1
        if company_line_index >= 0:
            company = lines[company_line_index].strip()
        
        job_title_index = share_line_index + 2
        if job_title_index < len(lines):
            job_title = lines[job_title_index].strip()

        location_index = share_line_index + 3
        if location_index < len(lines):
            location = lines[location_index].strip()
            location = location.split('·')[0].strip()

    # --- Step 2: Clean up the main content body ---
    cleaned_content_string = content
    if 'company_line_index' in locals() and company_line_index != -1:
        cleaned_content_string = "\n".join(lines[company_line_index:])
    
    end_phrase = "See how you compare to others who clicked apply"
    cleaned_content_string = cleaned_content_string.split(end_phrase)[0]

    # --- Step 3: Extract the Job Description (jd) ---
    job_description = ""
    jd_parts = cleaned_content_string.split("About the job", 1)
    if len(jd_parts) > 1:
        job_description = jd_parts[1].strip()

    # --- Step 4: Clean the URL and create the Key ID (NEW ROBUST LOGIC) ---
    cleaned_url = ""
    keyID = ""
    # This Regex looks for EITHER "/view/some_numbers" OR "JobId=some_characters"
    match = re.search(r'view/(\d+)|JobId=([^&]+)', url)
    
    if match:
        # The ID will be in one of the two capture groups
        id_from_url = match.group(1) or match.group(2)
        keyID = f"{source}_{id_from_url}"
        
        # Reconstruct the clean URL based on the ID
        cleaned_url = f"https://www.linkedin.com/jobs/view/{id_from_url}"
    else:
        # Fallback if neither pattern matches
        cleaned_url = url.split("/?")[0]
        keyID = f"{source}_unknownID"

    # --- Step 5: Find compensation ---
    compensation = ""
    # Only search for compensation if our main "Share" anchor was found.
    if share_line_index != -1:
        # Define a search window of 10 lines starting from our anchor.
        search_window_start = share_line_index
        # Ensure the window doesn't go past the end of the email content.
        search_window_end = min(share_line_index + 10, len(lines))

        # Look for the first line starting with '$' ONLY within this specific window.
        for i in range(search_window_start, search_window_end):
            if lines[i].strip().startswith('$'):
                compensation = lines[i].strip()
                break # Found it, stop searching.
    
    # --- Step 6: Return all extracted data ---
    scraped_data = {
        "job_title": job_title,
        "company": company,
        "location": location,
        "comp": compensation,
        "jd": job_description,
        "cleaned_url": cleaned_url,
        "keyID": keyID,
        "cleaned_content": cleaned_content_string.strip(),
    }
    return scraped_data

def scrape_indeed(content, url, source):
    """Scrapes data specifically from an Indeed job posting."""
    print(">>> Running Indeed Scraper...", file=sys.stderr) # Debug message

    # --- Step 1: Clean the URL and create the Key ID ---
    cleaned_url = url.split('&')[0]
    delimiter = '='
    id_from_url = cleaned_url.rsplit(delimiter, 1)[-1]
    keyID = f"{source}_{id_from_url}"

    # --- Step 2: Clean up the main content body ---
    start_pattern = r'Find Jobs|Job Post Details'
    parts = re.split(start_pattern, content, 1)
    cleaned_content = parts[1] if len(parts) > 1 else content
    cleaned_content = cleaned_content.rsplit("Report job", 1)[0]

    # --- Step 3: Extract data from the CLEANED content ---
    job_title, company, compensation, job_description, location = "", "", "", "", ""
    
    cleaned_lines = [line for line in cleaned_content.strip().splitlines() if line.strip()]
    
    if len(cleaned_lines) > 0:
        job_title = cleaned_lines[0].strip()
    if len(cleaned_lines) > 1:
        company = cleaned_lines[1].strip()
    
    # Find compensation and location
    comp_line_index = -1
    for i, line in enumerate(cleaned_lines):
        if line.strip().startswith('$'):
            compensation = line.strip()
            comp_line_index = i
            break 
    
    if comp_line_index > 0:
        location = cleaned_lines[comp_line_index - 1].strip()

    # Find the job description
    jd_parts = cleaned_content.split("Full job description", 1)
    if len(jd_parts) > 1:
        job_description = jd_parts[1].strip()

    # --- Step 4: Return all extracted data ---
    scraped_data = {
        "job_title": job_title,
        "company": company,
        "location": location,
        "comp": compensation,
        "jd": job_description,
        "cleaned_url": cleaned_url,
        "keyID": keyID,
        "cleaned_content": cleaned_content.strip(),
    }
    return scraped_data

# --- Main Script ---

# Read the entire text block from the AppleScript action
input_text = sys.stdin.read()

# Separate the initial properties block from the main content
properties_match = re.search(r"<properties>.*?</properties>", input_text, re.DOTALL)
properties_block = properties_match.group(0) if properties_match else "<properties>\n</properties>"
content_body = input_text.replace(properties_block, "", 1).strip()

# Get the original URL from the initial properties block
original_url = extract_property(properties_block, r"source_URL:\s*(.*)")
source = re.sub(r'^.*://', '', original_url)
domain_part = source.split('/')[0]
source = domain_part.rsplit('.', 1)[0]
source = source.split('.')[-1]

scraped_data = {}

# --- 1. DETERMINE THE SOURCE ---
if "linkedin" in source:
    scraped_data = scrape_linkedin(content_body, original_url, source)
elif "indeed" in source:
    scraped_data = scrape_indeed(content_body, original_url, source)
else:
    scraped_data = {"cleaned_url": original_url} # Pass the URL through if source is unknown

# --- 2. REBUILD THE PROPERTIES BLOCK ---
final_props = {
    "Source": source,
    "KeyID": scraped_data.get("keyID"),
    "Employer": scraped_data.get("company"),
    "Title": scraped_data.get("job_title"),
    "Location": scraped_data.get("location"),
    "Comp": scraped_data.get("comp"),
    "Address": scraped_data.get("cleaned_url"),
    "Description": scraped_data.get("jd"), # Get "jd" from the scraped_data dictionary
}

properties_to_add = ""
for key, value in final_props.items():
    if value: # Only add properties that have a value
        properties_to_add += f"{key}: {value}\n"

# Inject the new properties just before the closing </properties> tag
final_properties_block = properties_block.replace("</properties>", properties_to_add + "</properties>")

# Replace the original properties block with our newly generated one
# final_text = input_text.replace(properties_block, final_properties_block)
final_text = final_properties_block + "\n\n\n" + scraped_data.get("cleaned_content", content_body)

# --- 3. PRINT THE FINAL, FULLY-PROCESSED TEXT ---
print(final_text)
```

## Action 4: extract {variable: KeyId}
## Action 5: extract {variable: Employer}
## Action 6: extract {variable: Title} %%Job Title%%
## Action 7: extract {variable: URL}
## Action 8: extract {variable: Comp} %%Compensation%%
## Action 9: extract {variable: Description} %%Job Description%%
## Action 10: Display confirmation alert with the full description text (allowing user to see that the currect page was scraped, and it was scraped properly, resulting in useful information)
## Action 11: create dictionary of these variables
## Action 11: display alert (ensure user does indeed want to continue, sending data to online Sheets DB)
## Action 12: use URL: POST containing payload of JSON-format dictionary of variables from above.