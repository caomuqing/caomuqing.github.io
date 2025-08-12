#!/usr/bin/env python3
"""
Script to identify duplicate publications in the _publications directory
"""

import os
import re
from collections import defaultdict

def extract_publication_info(filepath):
    """Extract key information from a publication markdown file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract title
        title_match = re.search(r'title:\s*"([^"]+)"', content)
        title = title_match.group(1) if title_match else "No title"
        
        # Extract authors
        authors_match = re.search(r'authors:\s*["\']([^"\']+)["\']', content)
        authors = authors_match.group(1) if authors_match else "No authors"
        
        # Extract venue
        venue_match = re.search(r'venue:\s*["\']([^"\']+)["\']', content)
        venue = venue_match.group(1) if venue_match else "No venue"
        
        # Extract date
        date_match = re.search(r'date:\s*(\d{4}-\d{2}-\d{2})', content)
        date = date_match.group(1) if date_match else "No date"
        
        # Extract paperurl
        paperurl_match = re.search(r'paperurl:\s*["\']([^"\']+)["\']', content)
        paperurl = paperurl_match.group(1) if paperurl_match else "No URL"
        
        return {
            'filename': os.path.basename(filepath),
            'title': title.strip(),
            'authors': authors.strip(),
            'venue': venue.strip(),
            'date': date,
            'paperurl': paperurl.strip()
        }
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return None

def find_duplicates(publications_dir):
    """Find duplicate publications based on various criteria"""
    
    publications = []
    
    # Read all publication files
    for filename in os.listdir(publications_dir):
        if filename.endswith('.md'):
            filepath = os.path.join(publications_dir, filename)
            info = extract_publication_info(filepath)
            if info:
                publications.append(info)
    
    print(f"Analyzing {len(publications)} publications...\n")
    
    # Check for exact title duplicates
    title_groups = defaultdict(list)
    for pub in publications:
        title_groups[pub['title']].append(pub)
    
    print("=== EXACT TITLE DUPLICATES ===")
    exact_duplicates = []
    for title, pubs in title_groups.items():
        if len(pubs) > 1:
            exact_duplicates.append(pubs)
            print(f"\nTitle: {title}")
            for pub in pubs:
                print(f"  - {pub['filename']} | {pub['venue']} | {pub['date']}")
    
    # Check for similar titles (potential duplicates)
    print("\n\n=== SIMILAR TITLES (POTENTIAL DUPLICATES) ===")
    similar_titles = []
    
    for i, pub1 in enumerate(publications):
        for j, pub2 in enumerate(publications[i+1:], i+1):
            title1 = pub1['title'].lower()
            title2 = pub2['title'].lower()
            
            # Check if titles are very similar (80% similarity threshold)
            if are_titles_similar(title1, title2):
                similar_titles.append((pub1, pub2))
                print(f"\nSimilar titles:")
                print(f"  - {pub1['filename']}: {pub1['title']}")
                print(f"  - {pub2['filename']}: {pub2['title']}")
    
    # Check for same venue and date (potential duplicates)
    print("\n\n=== SAME VENUE & DATE (POTENTIAL DUPLICATES) ===")
    venue_date_groups = defaultdict(list)
    for pub in publications:
        key = f"{pub['venue']}_{pub['date']}"
        venue_date_groups[key].append(pub)
    
    for key, pubs in venue_date_groups.items():
        if len(pubs) > 1:
            venue, date = key.split('_', 1)
            print(f"\nVenue: {venue} | Date: {date}")
            for pub in pubs:
                print(f"  - {pub['filename']}: {pub['title']}")
    
    # Check for same paper URL (definite duplicates)
    print("\n\n=== SAME PAPER URL (DEFINITE DUPLICATES) ===")
    url_groups = defaultdict(list)
    for pub in publications:
        if pub['paperurl'] != "No URL":
            url_groups[pub['paperurl']].append(pub)
    
    for url, pubs in url_groups.items():
        if len(pubs) > 1:
            print(f"\nURL: {url}")
            for pub in pubs:
                print(f"  - {pub['filename']}: {pub['title']}")
    
    # Summary
    print("\n\n=== SUMMARY ===")
    print(f"Total publications: {len(publications)}")
    print(f"Exact title duplicates: {len(exact_duplicates)}")
    print(f"Similar titles: {len(similar_titles)}")
    print(f"Same venue & date: {sum(1 for pubs in venue_date_groups.values() if len(pubs) > 1)}")
    print(f"Same paper URL: {sum(1 for pubs in url_groups.values() if len(pubs) > 1)}")
    
    return {
        'exact_duplicates': exact_duplicates,
        'similar_titles': similar_titles,
        'venue_date_duplicates': [pubs for pubs in venue_date_groups.values() if len(pubs) > 1],
        'url_duplicates': [pubs for pubs in url_groups.values() if len(pubs) > 1]
    }

def are_titles_similar(title1, title2):
    """Check if two titles are similar (simple similarity check)"""
    # Remove common words and punctuation
    words1 = set(re.findall(r'\b\w+\b', title1))
    words2 = set(re.findall(r'\b\w+\b', title2))
    
    # Calculate Jaccard similarity
    intersection = len(words1.intersection(words2))
    union = len(words1.union(words2))
    
    if union == 0:
        return False
    
    similarity = intersection / union
    return similarity > 0.7  # 70% similarity threshold

if __name__ == "__main__":
    publications_dir = "_publications"
    
    if not os.path.exists(publications_dir):
        print(f"Error: Directory '{publications_dir}' not found!")
        exit(1)
    
    duplicates = find_duplicates(publications_dir)
    
    # Save results to file
    with open('duplicate_publications_report.txt', 'w', encoding='utf-8') as f:
        f.write("DUPLICATE PUBLICATIONS REPORT\n")
        f.write("=" * 50 + "\n\n")
        
        f.write("Exact Title Duplicates:\n")
        for group in duplicates['exact_duplicates']:
            f.write(f"Title: {group[0]['title']}\n")
            for pub in group:
                f.write(f"  - {pub['filename']} | {pub['venue']} | {pub['date']}\n")
            f.write("\n")
        
        f.write("Similar Titles:\n")
        for pub1, pub2 in duplicates['similar_titles']:
            f.write(f"  - {pub1['filename']}: {pub1['title']}\n")
            f.write(f"  - {pub2['filename']}: {pub2['title']}\n\n")
    
    print(f"\nDetailed report saved to 'duplicate_publications_report.txt'") 