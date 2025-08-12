#!/usr/bin/env python3
"""
Script to help generate appropriate images for publications
This script will create placeholder images with relevant text for each publication category
"""

import os
from PIL import Image, ImageDraw, ImageFont
import textwrap

def create_publication_image(title, category, output_path, size=(500, 300)):
    """Create a publication image with title and category"""
    
    # Create image with gradient background
    img = Image.new('RGB', size, color='#2E86AB')
    draw = ImageDraw.Draw(img)
    
    # Add gradient effect
    for y in range(size[1]):
        alpha = int(255 * (1 - y / size[1]))
        color = (46, 134, 171, alpha)
        draw.line([(0, y), (size[0], y)], fill=color)
    
    # Add category label at top
    try:
        # Try to use a default font
        font_large = ImageFont.truetype("arial.ttf", 24)
        font_small = ImageFont.truetype("arial.ttf", 18)
    except:
        # Fallback to default font
        font_large = ImageFont.load_default()
        font_small = ImageFont.load_default()
    
    # Draw category background
    category_bg = Image.new('RGBA', size, (0, 0, 0, 0))
    category_draw = ImageDraw.Draw(category_bg)
    category_draw.rectangle([10, 10, 200, 50], fill='#F7931E', outline='white', width=2)
    
    # Draw category text
    category_draw.text((20, 20), category, fill='white', font=font_small)
    
    # Composite category label
    img = Image.alpha_composite(img.convert('RGBA'), category_bg)
    draw = ImageDraw.Draw(img)
    
    # Wrap title text
    wrapped_title = textwrap.fill(title, width=25)
    
    # Calculate text position (center)
    bbox = draw.textbbox((0, 0), wrapped_title, font=font_large)
    text_width = bbox[2] - bbox[0]
    text_height = bbox[3] - bbox[1]
    
    x = (size[0] - text_width) // 2
    y = (size[1] - text_height) // 2
    
    # Draw title with shadow
    draw.text((x+2, y+2), wrapped_title, fill='black', font=font_large)
    draw.text((x, y), wrapped_title, fill='white', font=font_large)
    
    # Save image
    img.save(output_path)
    print(f"Created: {output_path}")

def main():
    """Generate images for all publication categories"""
    
    # Define publication categories and their titles
    categories = {
        "UAV_Localization": [
            "Integrated Localization-Navigation for UAV Docking",
            "Distance-based Cooperative Localization for MAVs",
            "UWB-Vision Approach for UAV Docking",
            "Single Landmark Distance-based Navigation"
        ],
        "Path_Planning": [
            "Feasible Path Planning for UAV Collision Avoidance",
            "Online Trajectory Correction for Facade Inspection",
            "DIRECT: DDP-based Trajectory Generation",
            "Learning Dynamic Weight Adjustment for Crowd Navigation"
        ],
        "Multi_Robot": [
            "Distributed Multi-Robot Sweep Coverage",
            "Similar Formation Control via Range Measurements",
            "Relative Localizability for Multi-Robot Systems"
        ],
        "SLAM_Odometry": [
            "LIRO: Tightly Coupled LiDAR-Inertia-Ranging Odometry",
            "MILIOM: Multi-Input LiDAR-Inertia Odometry",
            "SPINS: Structure Priors Aided INS",
            "DLC-SLAM: Learning-based LiDAR-SLAM",
            "HCTO: Optimality-aware LiDAR Inertial Odometry"
        ],
        "Hybrid_Robots": [
            "DoubleBee: Hybrid Aerial-Ground Robot",
            "AirCrab: Hybrid Aerial-Ground Manipulator",
            "CapsuleBot: Novel Hybrid Bi-Copter Robot",
            "System Identification for Hybrid Robots"
        ],
        "Tethered_Robots": [
            "Neptune: Nonentangling Trajectory Planning",
            "Path Planning Using Topological Braids"
        ],
        "Sensors_Fusion": [
            "Viral-Fusion: Visual-Inertial-Ranging-LiDAR Fusion",
            "AV-PedAware: Audio-Visual Pedestrian Awareness",
            "AV-FDTI: Audio-Visual Drone Threat Identification"
        ],
        "Datasets": [
            "NTU VIRAL: Multi-Modal Dataset"
        ],
        "Challenges": [
            "Cooperative Aerial Robot Inspection Challenge"
        ]
    }
    
    # Create images directory if it doesn't exist
    os.makedirs("publication_images", exist_ok=True)
    
    # Generate images for each category
    for category, titles in categories.items():
        for i, title in enumerate(titles):
            filename = f"publication_images/{category}_{i+1}.png"
            create_publication_image(title, category.replace("_", " "), filename)
    
    print("\nImage generation complete!")
    print("Images saved in 'publication_images' directory")
    print("\nNext steps:")
    print("1. Review the generated images")
    print("2. Update publication files with appropriate image paths")
    print("3. Optionally customize images with specific content from each paper")

if __name__ == "__main__":
    main() 