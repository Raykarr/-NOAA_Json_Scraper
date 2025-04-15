import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import sys

def fetch_json_links(url, base_url, visited=None, depth=0):
    if visited is None:
        visited = set()
    
    json_links = []
    indent = "  " * depth  # For visualizing recursion depth

    # Avoid reprocessing URLs
    if url in visited:
        return json_links
    visited.add(url)
    
    print(f"{indent}Processing: {url}")
    try:
        response = requests.get(url)
        response.raise_for_status()
    except Exception as e:
        print(f"{indent}Error fetching {url}: {e}", file=sys.stderr)
        return json_links

    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Process all anchor tags on the page
    for link in soup.find_all('a'):
        href = link.get('href')
        if not href or href in ['../', 'Parent Directory']:
            continue

        full_url = urljoin(url, href)
        # Restrict to URLs starting with the base URL
        if not full_url.startswith(base_url):
            continue

        if href.endswith('/'):
            # Recursively process directory pages
            json_links.extend(fetch_json_links(full_url, base_url, visited, depth + 1))
        elif href.endswith('.json'):
            print(f"{indent}Found JSON: {full_url}")
            json_links.append(full_url)
    return json_links

if __name__ == "__main__":
    base_url = "https://services.swpc.noaa.gov/json/"
    links = fetch_json_links(base_url, base_url)
    
    # Save output to file
    output_file = "json_links.txt"
    with open(output_file, "w") as f:
        for link in links:
            f.write(link + "\n")
    
    print(f"\nTotal JSON links found: {len(links)}")
    print(f"Links have been saved to {output_file}")
