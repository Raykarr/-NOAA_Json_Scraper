# NOAA JSON Link Scraper

## Overview
This Python script is designed to scrape and collect JSON file links from the NOAA (National Oceanic and Atmospheric Administration) services website, specifically from the JSON directory at `https://services.swpc.noaa.gov/json/`.

## Features
- Recursively crawls the NOAA JSON services directory
- Discovers and collects links to JSON files
- Handles nested directories
- Prevents duplicate URL processing
- Saves discovered JSON links to a text file
- Provides console output with processing details

## Requirements
- Python 3.x
- `requests` library
- `beautifulsoup4` library

## Installation
1. Clone the repository
2. Install required dependencies:
```bash
pip install requests beautifulsoup4
```

## Usage
Run the script directly:
```bash
python noaa_json_scraper.py
```

### Output
- Console will display processing details
- Creates `json_links.txt` with all discovered JSON links

## How It Works
1. Starts from the base URL `https://services.swpc.noaa.gov/json/`
2. Recursively explores directories
3. Collects links ending with `.json`
4. Prevents processing the same URL multiple times
5. Restricts crawling to the base domain

## Customization
- Modify `base_url` to scrape different directories
- Adjust recursion depth or add more filtering as needed

## Error Handling
- Catches and logs errors during URL fetching
- Skips problematic URLs without stopping the entire process

## Potential Use Cases
- Data collection for space weather research
- Automated JSON resource discovery
- NOAA data archiving and analysis

## Disclaimer
This script is for educational and research purposes. Ensure compliance with NOAA's terms of service and usage policies.

## Contributing
Contributions, issues, and feature requests are welcome!
