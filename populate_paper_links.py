#!/usr/bin/env python3
"""
Script to automatically populate the paper_links.yml file with all existing publications
"""

import os
import re

def extract_publication_info(filepath):
    """Extract key information from a publication markdown file"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Extract title
        title_match = re.search(r'title:\s*"([^"]+)"', content)
        title = title_match.group(1) if title_match else None
        
        # Extract paperurl
        paperurl_match = re.search(r'paperurl:\s*["\']([^"\']+)["\']', content)
        paperurl = paperurl_match.group(1) if paperurl_match else None
        
        # Extract DOI if present in the URL or content
        doi = None
        if paperurl:
            # Try to extract DOI from common patterns
            doi_match = re.search(r'doi\.org/([^\s/]+)', paperurl)
            if doi_match:
                doi = doi_match.group(1)
            else:
                # Look for DOI in the content
                doi_content_match = re.search(r'doi:\s*["\']([^"\']+)["\']', content)
                if doi_content_match:
                    doi = doi_content_match.group(1)
        
        # Extract video links from excerpt and content
        video_links = []
        video_pattern = r'\[Video\]\(([^)]+)\)'
        video_matches = re.findall(video_pattern, content)
        video_links.extend(video_matches)
        
        # Extract code links from excerpt and content
        code_links = []
        code_pattern = r'\[Code\]\(([^)]+)\)'
        code_matches = re.findall(code_pattern, content)
        code_links.extend(code_matches)
        
        # Extract presentation links from excerpt and content
        presentation_links = []
        presentation_pattern = r'\[Presentation\]\(([^)]+)\)'
        presentation_matches = re.findall(presentation_pattern, content)
        presentation_links.extend(presentation_matches)
        
        return {
            'title': title,
            'paperurl': paperurl,
            'doi': doi,
            'video_links': video_links,
            'code_links': code_links,
            'presentation_links': presentation_links
        }
    except Exception as e:
        print(f"Error processing {filepath}: {e}")
        return None

def populate_paper_links():
    """Populate the paper_links.yml file with all existing publications"""
    
    publications_dir = '_publications'
    config_file = '_data/paper_links.yml'
    
    if not os.path.exists(publications_dir):
        print(f"Error: Publications directory '{publications_dir}' not found!")
        return
    
    print("📚 Scanning existing publications...")
    
    # Start building the YAML content
    yaml_content = [
        "# Central configuration for paper links",
        "# Update this file to change paper URLs across your site",
        "",
        "papers:"
    ]
    
    papers_count = 0
    papers_with_urls = 0
    papers_with_dois = 0
    papers_with_videos = 0
    papers_with_code = 0
    papers_with_presentations = 0
    
    # Process all publication files
    for filename in sorted(os.listdir(publications_dir)):
        if filename.endswith('.md'):
            filepath = os.path.join(publications_dir, filename)
            info = extract_publication_info(filepath)
            
            if info and info['title']:
                title = info['title'].strip()
                papers_count += 1
                
                # Add paper to YAML
                yaml_content.append(f'  "{title}":')
                
                if info['paperurl']:
                    yaml_content.append(f'    url: "{info["paperurl"]}"')
                    papers_with_urls += 1
                else:
                    yaml_content.append('    url: null')
                
                if info['doi']:
                    yaml_content.append(f'    doi: "{info["doi"]}"')
                    papers_with_dois += 1
                else:
                    yaml_content.append('    doi: null')
                
                # Add video links
                if info['video_links']:
                    yaml_content.append('    videos:')
                    for video in info['video_links']:
                        yaml_content.append(f'      - "{video}"')
                    papers_with_videos += 1
                else:
                    yaml_content.append('    videos: []')
                
                # Add code links
                if info['code_links']:
                    yaml_content.append('    code:')
                    for code in info['code_links']:
                        yaml_content.append(f'      - "{code}"')
                    papers_with_code += 1
                else:
                    yaml_content.append('    code: []')
                
                # Add presentation links
                if info['presentation_links']:
                    yaml_content.append('    presentations:')
                    for presentation in info['presentation_links']:
                        yaml_content.append(f'      - "{presentation}"')
                    papers_with_presentations += 1
                else:
                    yaml_content.append('    presentations: []')
                
                yaml_content.append('')  # Empty line for readability
                
                print(f"➕ Added: {title}")
                if info['paperurl']:
                    print(f"  URL: {info['paperurl']}")
                if info['doi']:
                    print(f"  DOI: {info['doi']}")
                if info['video_links']:
                    print(f"  Videos: {len(info['video_links'])}")
                if info['code_links']:
                    print(f"  Code: {len(info['code_links'])}")
                if info['presentation_links']:
                    print(f"  Presentations: {len(info['presentation_links'])}")
    
    # Save the YAML file
    try:
        with open(config_file, 'w', encoding='utf-8') as f:
            f.write('\n'.join(yaml_content))
        
        print(f"\n✅ Successfully updated {config_file}")
        print(f"📊 Total papers in configuration: {papers_count}")
        print(f"🔗 Papers with URLs: {papers_with_urls}")
        print(f"📝 Papers with DOIs: {papers_with_dois}")
        print(f"🎥 Papers with videos: {papers_with_videos}")
        print(f"💻 Papers with code: {papers_with_code}")
        print(f"📊 Papers with presentations: {papers_with_presentations}")
        
    except Exception as e:
        print(f"❌ Error saving configuration: {e}")

def show_current_papers():
    """Show all papers currently in the configuration"""
    config_file = '_data/paper_links.yml'
    
    if not os.path.exists(config_file):
        print("No paper_links.yml file found!")
        return
    
    try:
        with open(config_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Simple parsing to count papers
        lines = content.split('\n')
        papers = []
        current_paper = None
        
        for line in lines:
            if line.strip().endswith(':') and not line.startswith('#'):
                if line.strip() != 'papers:':
                    current_paper = line.strip()[:-1].strip('"')
                    papers.append(current_paper)
        
        if not papers:
            print("No papers in configuration!")
            return
        
        print(f"📚 PAPERS IN CONFIGURATION ({len(papers)} total):")
        print("=" * 80)
        
        for i, title in enumerate(papers, 1):
            print(f"{i:2d}. {title}")
        print()
            
    except Exception as e:
        print(f"Error reading configuration: {e}")

if __name__ == "__main__":
    print("🔗 PAPER LINKS POPULATION TOOL")
    print("=" * 50)
    print("1. Populate paper_links.yml with all existing publications")
    print("2. Show current papers in configuration")
    print("3. Exit")
    print("=" * 50)
    
    choice = input("Select option (1-3): ").strip()
    
    if choice == '1':
        populate_paper_links()
    elif choice == '2':
        show_current_papers()
    elif choice == '3':
        print("👋 Goodbye!")
    else:
        print("❌ Invalid option. Please select 1-3.") 