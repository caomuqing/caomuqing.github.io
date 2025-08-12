#!/usr/bin/env python3
"""
Script to generate search queries and export publication information for finding correct links
"""

import os
import re
import csv
from urllib.parse import quote_plus

def generate_search_queries():
    """Generate search queries and export publication information"""
    
    publications_dir = '_publications'
    publications_data = []
    
    print("Generating search queries and publication data...")
    print()
    
    for filename in os.listdir(publications_dir):
        if filename.endswith('.md'):
            filepath = os.path.join(publications_dir, filename)
            
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Extract publication information - handle both single and double quotes
                title_match = re.search(r'title:\s*["\']([^"\']+)["\']', content)
                authors_match = re.search(r'authors:\s*["\']([^"\']+)["\']', content)
                date_match = re.search(r'date:\s*["\'](\d{4})', content)
                venue_match = re.search(r'venue:\s*["\']([^"\']+)["\']', content)
                current_url_match = re.search(r'paperurl:\s*["\']([^"\']+)["\']', content)
                
                if title_match and date_match:
                    title = title_match.group(1)
                    authors = authors_match.group(1) if authors_match else "Unknown"
                    year = date_match.group(1)
                    venue = venue_match.group(1) if venue_match else "Unknown"
                    current_url = current_url_match.group(1) if current_url_match else "None"
                    
                    # Create search queries
                    google_scholar_query = f'"{title}" {authors} {year}'
                    google_scholar_url = f"https://scholar.google.com/scholar?q={quote_plus(google_scholar_query)}"
                    
                    # Create IEEE Xplore search (if it's an IEEE publication)
                    ieee_query = f'"{title}" {year}'
                    ieee_url = f"https://ieeexplore.ieee.org/search/searchresult.jsp?queryText={quote_plus(ieee_query)}"
                    
                    # Create arXiv search (if it might be on arXiv)
                    arxiv_query = f'"{title}" {authors}'
                    arxiv_url = f"https://arxiv.org/search/?query={quote_plus(arxiv_query)}&searchtype=all&source=header"
                    
                    publications_data.append({
                        'filename': filename,
                        'title': title,
                        'authors': authors,
                        'year': year,
                        'venue': venue,
                        'current_url': current_url,
                        'google_scholar_url': google_scholar_url,
                        'ieee_url': ieee_url,
                        'arxiv_url': arxiv_url
                    })
                    
                    print(f"✓ {filename}")
                    print(f"  Title: {title}")
                    print(f"  Authors: {authors}")
                    print(f"  Year: {year}")
                    print(f"  Venue: {venue}")
                    print(f"  Current URL: {current_url}")
                    print(f"  Google Scholar: {google_scholar_url}")
                    print()
                    
            except Exception as e:
                print(f"✗ Error processing {filename}: {e}")
    
    # Export to CSV
    csv_filename = 'publications_for_link_search.csv'
    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['filename', 'title', 'authors', 'year', 'venue', 'current_url', 
                     'google_scholar_url', 'ieee_url', 'arxiv_url']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for pub in publications_data:
            writer.writerow(pub)
    
    print(f"\nExported {len(publications_data)} publications to '{csv_filename}'")
    print("\nNEXT STEPS TO FIND CORRECT LINKS:")
    print("1. Open the CSV file in Excel/Google Sheets")
    print("2. For each publication, click the Google Scholar link")
    print("3. Find the correct paper and copy its DOI/link")
    print("4. Update the 'current_url' column with the correct link")
    print("5. Use the updated CSV to fix the publication files")
    
    # Also create a simple text summary
    summary_filename = 'publications_summary.txt'
    with open(summary_filename, 'w', encoding='utf-8') as f:
        f.write("PUBLICATIONS REQUIRING CORRECT LINKS\n")
        f.write("=" * 50 + "\n\n")
        
        for pub in publications_data:
            f.write(f"File: {pub['filename']}\n")
            f.write(f"Title: {pub['title']}\n")
            f.write(f"Authors: {pub['authors']}\n")
            f.write(f"Year: {pub['year']}\n")
            f.write(f"Venue: {pub['venue']}\n")
            f.write(f"Current URL: {pub['current_url']}\n")
            f.write(f"Google Scholar Search: {pub['google_scholar_url']}\n")
            f.write("-" * 50 + "\n\n")
    
    print(f"Also created '{summary_filename}' with a readable summary")
    print("\nYou can now systematically search for the correct links!")

if __name__ == "__main__":
    generate_search_queries() 