#!/usr/bin/env python3
"""
Script to update publication files with appropriate image paths
This will replace the dummy 500x300.png images with relevant ones
"""

import os
import re

def update_publication_images():
    """Update all publication files with appropriate image paths"""
    
    # Define the mapping of publications to images
    image_mapping = {
        # Publications that already have correct images
        "2023-01-tro-cao.md": "images/rss2.gif",  # Neptune
        "2023-06-rss-cao.md": "images/rss1.gif",  # Topological Braids
        "2023-10-iros-cao.md": "images/doublebee1.gif",  # DoubleBee
        "2024-10-iros-cao.md": "images/aircrab.gif",  # AirCrab
        "2025-01-icra-cao.md": "images/learning-planning.gif",  # Learning
        "2025-01-ram-cao.md": "images/caric1.gif",  # CARIC Challenge
        
        # Publications that need new images (using placeholder names)
        "2018-10-iros-nguyen.md": "images/uav-docking.png",
        "2018-06-icca-wang.md": "images/uav-collision-avoidance.png",
        "2018-11-icarcv-nguyen.md": "images/uav-landing.png",
        "2019-08-ral-nguyen.md": "images/cooperative-localization.png",
        "2019-05-icra-nguyen.md": "images/uwb-vision-docking.png",
        "2019-09-tcst-nguyen.md": "images/single-landmark-navigation.png",
        "2019-04-tro-nguyen.md": "images/robot-swarm-formation.png",
        "2020-06-icca-cao.md": "images/facade-inspection.png",
        "2021-06-ral-cao.md": "images/direct-trajectory.png",
        "2021-05-ais-cao.md": "images/multi-robot-coverage.png",
        "2021-05-icra-nguyen.md": "images/liro-odometry.png",
        "2021-06-ral-nguyen.md": "images/miliom-slam.png",
        "2022-03-ijrr-nguyen.md": "images/ntu-viral-dataset.png",
        "2023-08-jfr-lyu.md": "images/spins-ins.png",
        "2023-12-tmech-liu.md": "images/dlc-slam.png",
        "2024-04-isprs-li.md": "images/hcto-odometry.png",
        "2023-06-tsmc-cao.md": "images/multi-robot-coverage.png",
        "2023-07-tsmc-lyu.md": "images/vision-plane-following.png",
        "2023-06-tcyb-cao.md": "images/formation-control.png",
        "2023-03-ctt-cao.md": "images/hybrid-robot-control.png",
        "2023-10-iros-yang.md": "images/av-pedestrian-awareness.png",
        "2024-06-jai-yang.md": "images/av-drone-threat.png",
        "2024-12-jai-xu.md": "images/sloped-terrain-control.png",
        "2024-04-icca-xu.md": "images/cooperative-exploration.png",
        "2025-01-ral-liao.md": "images/crowd-navigation.png",
        "2025-01-iros-baek.md": "images/pipe-planner.png",
        "2025-01-icra-liao.md": "images/atom-human-prediction.png",
        "2025-01-tro-chen.md": "images/multi-robot-localization.png",
        "2024-04-ral-zheng.md": "images/capsulebot-robot.png",
    }
    
    publications_dir = "_publications"
    
    # Check if publications directory exists
    if not os.path.exists(publications_dir):
        print(f"Error: {publications_dir} directory not found!")
        return
    
    # Get all publication files
    publication_files = [f for f in os.listdir(publications_dir) if f.endswith('.md')]
    
    updated_count = 0
    
    for filename in publication_files:
        if filename in image_mapping:
            filepath = os.path.join(publications_dir, filename)
            
            # Read the file
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Replace the teaser image
                old_teaser = r'teaser: \'images/500x300\.png\''
                new_teaser = f"teaser: '{image_mapping[filename]}'"
                
                if re.search(old_teaser, content):
                    content = re.sub(old_teaser, new_teaser, content)
                    
                    # Write the updated content back
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    
                    print(f"✓ Updated {filename} → {image_mapping[filename]}")
                    updated_count += 1
                else:
                    print(f"- Skipped {filename} (no dummy image found)")
                    
            except Exception as e:
                print(f"✗ Error updating {filename}: {e}")
    
    print(f"\nUpdate complete! Updated {updated_count} publication files.")
    
    # Print summary of what needs to be done
    print("\n" + "="*60)
    print("NEXT STEPS:")
    print("="*60)
    
    print("\n1. Create the following images in your 'images' directory:")
    for filename, image_path in image_mapping.items():
        if not image_path.startswith("images/") or "500x300.png" in image_path:
            continue
        if not os.path.exists(image_path):
            print(f"   - {image_path}")
    
    print("\n2. Use the HTML template (publication_image_templates.html) to:")
    print("   - See color schemes and design guidelines")
    print("   - Use online tools like Canva or Figma")
    print("   - Create consistent 500x300 pixel images")
    
    print("\n3. Run the Python image generator:")
    print("   pip install Pillow")
    print("   python generate_publication_images.py")
    
    print("\n4. After creating images, run this script again to update paths")

if __name__ == "__main__":
    update_publication_images() 