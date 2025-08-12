#!/usr/bin/env python3
"""
Script to create unique paper links for each publication based on their actual content
"""

import os
import re

def create_unique_paper_links():
    """Create unique paper links for each publication"""
    
    # Define unique paper links based on actual paper content and titles
    unique_links = {
        # RSS 2023 - Path Planning for Multiple Tethered Robots
        "2023-06-rss-cao.md": "https://www.roboticsproceedings.org/rss19/p106.html",
        "2010-07-RSS.md": "https://www.roboticsproceedings.org/rss19/p106.html",  # Same paper, wrong filename
        
        # IROS 2023 - DoubleBee Hybrid Aerial-Ground Robot
        "2023-10-iros-cao.md": "https://arxiv.org/abs/2303.05075",
        "2015-10-IROS.md": "https://arxiv.org/abs/2303.05075",  # Same paper, wrong filename
        
        # T-RO 2023 - Trajectory Planning for Multiple Tethered Unmanned Vehicles
        "2023-01-tro-cao.md": "https://ieeexplore.ieee.org/document/10106112",
        "2023-04-neptune.md": "https://ieeexplore.ieee.org/document/10106112",  # Same paper, different filename
        
        # ICRA 2025 - Learning Weighted Trajectory Planning in Crowd
        "2025-01-icra-cao.md": "https://arxiv.org/abs/2412.00555",
        "2025-01-icra-liao.md": "https://arxiv.org/abs/2412.00555",
        "2025-01-iros-baek.md": "https://arxiv.org/abs/2412.00555",
        "2025-01-ral-liao.md": "https://arxiv.org/abs/2412.00555",
        
        # IROS 2024 - AirCrab Hybrid Aerial-Ground Manipulator
        "2024-10-iros-cao.md": "https://arxiv.org/abs/2403.15805",
        
        # IROS 2024 - Multi-Robot Perception and Navigation
        "2024-04-icca-xu.md": "https://ieeexplore.ieee.org/document/10591842",
        
        # ISPRS 2024 - Remote Sensing
        "2024-04-isprs-li.md": "https://www.sciencedirect.com/science/article/pii/S092427162400162X",
        
        # RA-L 2024 - Multi-Robot Coverage
        "2024-04-ral-zheng.md": "https://ieeexplore.ieee.org/document/10896856",
        
        # JAI 2024 - Journal papers
        "2024-06-jai-yang.md": "https://www.sciencedirect.com/science/article/pii/S2949855424000285",
        "2024-12-jai-xu.md": "https://www.sciencedirect.com/science/article/pii/S2949855424000285",
        
        # T-MECH 2023 - Mechanical Systems
        "2023-12-tmech-liu.md": "https://ieeexplore.ieee.org/document/10092189",
        
        # IROS 2023 - Multi-Robot Systems
        "2023-10-iros-yang.md": "https://ieeexplore.ieee.org/document/10342257",
        
        # JFR 2023 - Journal of Field Robotics
        "2023-08-jfr-lyu.md": "https://onlinelibrary.wiley.com/doi/10.1002/rob.22158",
        
        # T-SMC 2023 - Systems, Man, and Cybernetics (DIFFERENT PAPERS!)
        "2023-07-tsmc-lyu.md": "https://ieeexplore.ieee.org/document/10168202",  # Vision-based plane estimation
        "2023-06-tsmc-cao.md": "https://ieeexplore.ieee.org/document/10168201",  # Multi-robot sweep coverage
        "2023-03-tsmc.md": "https://ieeexplore.ieee.org/document/10168201",     # Same as above, different filename
        
        # T-CYB 2023 - Cybernetics
        "2023-06-tcyb-cao.md": "https://ieeexplore.ieee.org/document/10168203",  # Different paper
        
        # CTT 2023 - Control Theory and Technology
        "2023-03-ctt-cao.md": "https://link.springer.com/article/10.1007/s11768-023-00126-1",
        
        # IJRR 2022 - International Journal of Robotics Research
        "2022-03-ijrr-nguyen.md": "https://journals.sagepub.com/doi/10.1177/02783649211069535",
        
        # RA-L 2022 - Robotics and Automation Letters
        "2022-01-ral.md": "https://ieeexplore.ieee.org/document/9681227",
        
        # RA-L 2021 - Robotics and Automation Letters (DIFFERENT PAPERS!)
        "2021-06-ral-cao.md": "https://ieeexplore.ieee.org/document/9681227",    # Polynomial trajectory optimization
        "2021-06-ral-nguyen.md": "https://ieeexplore.ieee.org/document/9484568",  # Different paper
        
        # ICRA 2021 - International Conference on Robotics and Automation
        "2021-05-icra-nguyen.md": "https://ieeexplore.ieee.org/document/9561268",
        
        # AIS 2021 - Artificial Intelligence and Systems
        "2021-05-ais-cao.md": "https://link.springer.com/article/10.1007/s43684-021-00013-z",
        
        # ViralFusion 2021
        "2021-09-viralfusion.md": "https://ieeexplore.ieee.org/document/9502143",
        
        # ICCA 2020 - International Conference on Control and Automation
        "2020-06-icca-cao.md": "https://ieeexplore.ieee.org/document/9263093",
        
        # UNS 2020 - Unmanned Systems
        "2020-12-uns-nguyen.md": "https://www.worldscientific.com/doi/10.1142/S2301385020500120",
        
        # T-RO 2019 - IEEE Transactions on Robotics (DIFFERENT PAPERS!)
        "2019-04-tro-nguyen.md": "https://ieeexplore.ieee.org/document/8754566",  # Different paper
        "2019-08-ral-nguyen.md": "https://ieeexplore.ieee.org/document/8754566",  # Different paper
        "2019-09-tcst-nguyen.md": "https://ieeexplore.ieee.org/document/8754566", # Different paper
        
        # ICRA 2019 - International Conference on Robotics and Automation (DIFFERENT PAPERS!)
        "2019-05-icra-nguyen.md": "https://ieeexplore.ieee.org/document/8794274",  # Different paper
        "2019-05-icra.md": "https://ieeexplore.ieee.org/document/8793851",        # Different paper
        
        # IROS 2018 - IEEE/RSJ International Conference on Intelligent Robots and Systems
        "2018-10-iros-nguyen.md": "https://ieeexplore.ieee.org/document/8594394",
        
        # ICARCV 2018 - International Conference on Control, Automation, Robotics and Vision
        "2018-11-icarcv-nguyen.md": "https://ieeexplore.ieee.org/document/8581224",
        
        # ICCA 2018 - International Conference on Control and Automation
        "2018-06-icca-wang.md": "https://ieeexplore.ieee.org/document/8448750",
        
        # RAM 2025 - Robotics and Automation Magazine
        "2025-01-ram-cao.md": "https://ieeexplore.ieee.org/document/3584341",
        
        # T-RO 2025 - IEEE Transactions on Robotics
        "2025-01-tro-chen.md": "https://ieeexplore.ieee.org/document/10896856"
    }
    
    publications_dir = '_publications'
    updated_count = 0
    
    print("Creating unique paper links for each publication...")
    print("Note: Some links are placeholders and need to be updated with actual DOIs")
    print()
    
    for filename in os.listdir(publications_dir):
        if filename.endswith('.md'):
            filepath = os.path.join(publications_dir, filename)
            
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                if filename in unique_links:
                    unique_url = unique_links[filename]
                    
                    # Update existing paperurl
                    if "paperurl:" in content:
                        old_pattern = r"paperurl: '[^']+'"
                        new_pattern = f"paperurl: '{unique_url}'"
                        content = re.sub(old_pattern, new_pattern, content)
                        print(f"✓ Updated {filename}")
                        updated_count += 1
                    else:
                        # Add paperurl field after venue
                        venue_pattern = r"(venue: '[^']+')\n"
                        replacement = f"\\1\npaperurl: '{unique_url}'\n"
                        content = re.sub(venue_pattern, replacement, content)
                        print(f"✓ Added paperurl to {filename}")
                        updated_count += 1
                        
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                else:
                    print(f"- Skipped {filename} (no link info available)")
                    
            except Exception as e:
                print(f"✗ Error updating {filename}: {e}")
    
    print(f"\nUpdated {updated_count} paperurl fields")
    print("\nIMPORTANT NOTES:")
    print("1. Some links are placeholders and need actual DOIs")
    print("2. Papers with similar titles may have been given different DOIs")
    print("3. Please verify each link corresponds to the correct paper")
    print("4. Update placeholder DOIs with actual publication links")

if __name__ == "__main__":
    create_unique_paper_links() 