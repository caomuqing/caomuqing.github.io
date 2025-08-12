#!/usr/bin/env python3
"""
Simple script to create a list of all publications with their titles and current URLs
"""

import os
import re
from urllib.parse import quote_plus

def create_publication_list():
    """Create a simple list of all publications"""
    
    publications_dir = '_publications'
    publications_list = []
    
    print("Creating publication list for manual link correction...")
    print()
    
    for filename in os.listdir(publications_dir):
        if filename.endswith('.md'):
            filepath = os.path.join(publications_dir, filename)
            
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Extract title and current URL
                title_match = re.search(r'title:\s*"([^"]+)"', content)
                current_url_match = re.search(r'paperurl:\s*["\']([^"\']+)["\']', content)
                
                if title_match:
                    title = title_match.group(1)
                    current_url = current_url_match.group(1) if current_url_match else "None"
                    
                    publications_list.append({
                        'filename': filename,
                        'title': title,
                        'current_url': current_url
                    })
                    
                    print(f"✓ {filename}")
                    print(f"  Title: {title}")
                    print(f"  Current URL: {current_url}")
                    print()
                    
            except Exception as e:
                print(f"✗ Error processing {filename}: {e}")
    
    # Create a simple text file with the list
    output_filename = 'publications_to_fix.txt'
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write("PUBLICATIONS REQUIRING CORRECT LINKS\n")
        f.write("=" * 60 + "\n\n")
        f.write("INSTRUCTIONS:\n")
        f.write("1. For each publication below, search Google Scholar for the title\n")
        f.write("2. Find the correct paper and copy its DOI/link\n")
        f.write("3. Update the publication file with the correct link\n\n")
        f.write("=" * 60 + "\n\n")
        
        for i, pub in enumerate(publications_list, 1):
            f.write(f"{i:2d}. {pub['filename']}\n")
            f.write(f"    Title: {pub['title']}\n")
            f.write(f"    Current URL: {pub['current_url']}\n")
            f.write(f"    Google Scholar Search: https://scholar.google.com/scholar?q={quote_plus(pub['title'])}\n")
            f.write("-" * 60 + "\n\n")
    
    print(f"\nCreated '{output_filename}' with {len(publications_list)} publications")
    print("\nNEXT STEPS:")
    print("1. Open 'publications_to_fix.txt'")
    print("2. For each publication, click the Google Scholar link")
    print("3. Find the correct paper and copy its DOI/link")
    print("4. Update the publication file with the correct link")
    print("\nThis will help you systematically find the correct links for each paper!")

if __name__ == "__main__":
    create_publication_list() 