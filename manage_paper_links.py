#!/usr/bin/env python3
"""
Script to help manage paper links in the central configuration
"""

import os
import re

def load_paper_links():
    """Load the current paper links configuration"""
    config_file = '_data/paper_links.yml'
    if os.path.exists(config_file):
        with open(config_file, 'r', encoding='utf-8') as f:
            content = f.read()
        return parse_yaml_content(content)
    return {'papers': {}}

def parse_yaml_content(content):
    """Simple YAML parser for the paper links configuration"""
    papers = {}
    lines = content.split('\n')
    current_paper = None
    current_field = None
    
    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            continue
            
        if line.endswith(':') and not line.startswith('  '):
            # This is a paper title
            current_paper = line[:-1].strip('"')
            papers[current_paper] = {
                'url': None,
                'doi': None,
                'videos': [],
                'code': [],
                'presentations': []
            }
            current_field = None
        elif line.startswith('  ') and line.endswith(':'):
            # This is a field
            current_field = line.strip()[:-1]
        elif line.startswith('    - "') and line.endswith('"'):
            # This is a list item
            if current_paper and current_field:
                value = line[6:-1]  # Remove '    - "' and '"'
                if current_field in papers[current_paper]:
                    papers[current_paper][current_field].append(value)
        elif line.startswith('    ') and ':' in line and not line.startswith('    -'):
            # This is a simple field
            if current_paper and ':' in line:
                field, value = line.split(':', 1)
                field = field.strip()
                value = value.strip().strip('"')
                if value == 'null':
                    value = None
                papers[current_paper][field] = value
    
    return {'papers': papers}

def save_paper_links(config):
    """Save the paper links configuration"""
    config_file = '_data/paper_links.yml'
    
    yaml_content = [
        "# Central configuration for paper links",
        "# Update this file to change paper URLs across your site",
        "",
        "papers:"
    ]
    
    for title, info in config['papers'].items():
        yaml_content.append(f'  "{title}":')
        
        if info.get('url'):
            yaml_content.append(f'    url: "{info["url"]}"')
        else:
            yaml_content.append('    url: null')
            
        if info.get('doi'):
            yaml_content.append(f'    doi: "{info["doi"]}"')
        else:
            yaml_content.append('    doi: null')
            
        # Videos
        if info.get('videos') and len(info['videos']) > 0:
            yaml_content.append('    videos:')
            for video in info['videos']:
                yaml_content.append(f'      - "{video}"')
        else:
            yaml_content.append('    videos: []')
            
        # Code
        if info.get('code') and len(info['code']) > 0:
            yaml_content.append('    code:')
            for code in info['code']:
                yaml_content.append(f'      - "{code}"')
        else:
            yaml_content.append('    code: []')
            
        # Presentations
        if info.get('presentations') and len(info['presentations']) > 0:
            yaml_content.append('    presentations:')
            for presentation in info['presentations']:
                yaml_content.append(f'      - "{presentation}"')
        else:
            yaml_content.append('    presentations: []')
            
        yaml_content.append('')  # Empty line for readability
    
    with open(config_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(yaml_content))

def list_all_papers():
    """List all papers in the configuration"""
    config = load_paper_links()
    papers = config.get('papers', {})
    
    print("📚 PAPERS IN CENTRAL CONFIGURATION:")
    print("=" * 80)
    
    for i, (title, info) in enumerate(papers.items(), 1):
        print(f"{i:2d}. {title}")
        print(f"    URL: {info.get('url', 'Not set')}")
        print(f"    DOI: {info.get('doi', 'Not set')}")
        print(f"    Videos: {len(info.get('videos', []))}")
        print(f"    Code: {len(info.get('code', []))}")
        print(f"    Presentations: {len(info.get('presentations', []))}")
        print()

def add_paper():
    """Add a new paper to the configuration"""
    config = load_paper_links()
    
    print("📝 ADDING NEW PAPER")
    print("=" * 30)
    
    title = input("Paper title: ").strip()
    if not title:
        print("❌ Title cannot be empty")
        return
    
    url = input("Paper URL: ").strip()
    doi = input("DOI (optional): ").strip()
    
    config['papers'][title] = {
        'url': url if url else None,
        'doi': doi if doi else None,
        'videos': [],
        'code': [],
        'presentations': []
    }
    
    save_paper_links(config)
    print(f"✅ Added paper: {title}")

def update_paper():
    """Update an existing paper's links"""
    config = load_paper_links()
    papers = config.get('papers', {})
    
    if not papers:
        print("❌ No papers in configuration")
        return
    
    print("📝 UPDATING PAPER")
    print("=" * 30)
    
    # List papers for selection
    titles = list(papers.keys())
    for i, title in enumerate(titles, 1):
        print(f"{i:2d}. {title}")
    
    try:
        choice = int(input(f"\nSelect paper (1-{len(titles)}): ")) - 1
        if 0 <= choice < len(titles):
            title = titles[choice]
            current_info = papers[title]
            
            print(f"\nUpdating: {title}")
            print(f"Current URL: {current_info.get('url', 'Not set')}")
            print(f"Current DOI: {current_info.get('doi', 'Not set')}")
            print(f"Current Videos: {len(current_info.get('videos', []))}")
            print(f"Current Code: {len(current_info.get('code', []))}")
            print(f"Current Presentations: {len(current_info.get('presentations', []))}")
            
            new_url = input("New URL (press Enter to keep current): ").strip()
            new_doi = input("New DOI (press Enter to keep current): ").strip()
            
            if new_url:
                papers[title]['url'] = new_url
            if new_doi:
                papers[title]['doi'] = new_doi
            
            save_paper_links(config)
            print(f"✅ Updated paper: {title}")
        else:
            print("❌ Invalid selection")
    except ValueError:
        print("❌ Please enter a valid number")

def remove_paper():
    """Remove a paper from the configuration"""
    config = load_paper_links()
    papers = config.get('papers', {})
    
    if not papers:
        print("❌ No papers in configuration")
        return
    
    print("🗑️  REMOVING PAPER")
    print("=" * 30)
    
    # List papers for selection
    titles = list(papers.keys())
    for i, title in enumerate(titles, 1):
        print(f"{i:2d}. {title}")
    
    try:
        choice = int(input(f"\nSelect paper to remove (1-{len(titles)}): ")) - 1
        if 0 <= choice < len(titles):
            title = titles[choice]
            
            confirm = input(f"Are you sure you want to remove '{title}'? (y/N): ")
            if confirm.lower() in ['y', 'yes']:
                del papers[title]
                save_paper_links(config)
                print(f"✅ Removed paper: {title}")
            else:
                print("❌ Operation cancelled")
        else:
            print("❌ Invalid selection")
    except ValueError:
        print("❌ Please enter a valid number")

def main():
    """Main menu"""
    while True:
        print("\n" + "=" * 50)
        print("🔗 PAPER LINKS MANAGEMENT TOOL")
        print("=" * 50)
        print("1. List all papers")
        print("2. Add new paper")
        print("3. Update paper")
        print("4. Remove paper")
        print("5. Exit")
        print("=" * 50)
        
        choice = input("Select option (1-5): ").strip()
        
        if choice == '1':
            list_all_papers()
        elif choice == '2':
            add_paper()
        elif choice == '3':
            update_paper()
        elif choice == '4':
            remove_paper()
        elif choice == '5':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid option. Please select 1-5.")

if __name__ == "__main__":
    main() 