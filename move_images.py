#!/usr/bin/env python3
"""
Script to move and rename generated images to the main images directory
"""

import os
import shutil

def move_and_rename_images():
    """Move generated images to main images directory with appropriate names"""
    
    # Define the mapping of generated images to final names
    image_mapping = {
        # UAV Localization & Navigation
        "UAV_Localization_1.png": "uav-docking.png",
        "UAV_Localization_2.png": "uav-collision-avoidance.png", 
        "UAV_Localization_3.png": "uav-landing.png",
        "UAV_Localization_4.png": "cooperative-localization.png",
        
        # Path Planning & Trajectory
        "Path_Planning_1.png": "facade-inspection.png",
        "Path_Planning_2.png": "direct-trajectory.png",
        "Path_Planning_3.png": "multi-robot-coverage.png",
        "Path_Planning_4.png": "crowd-navigation.png",
        
        # SLAM & Odometry
        "SLAM_Odometry_1.png": "liro-odometry.png",
        "SLAM_Odometry_2.png": "miliom-slam.png",
        "SLAM_Odometry_3.png": "ntu-viral-dataset.png",
        "SLAM_Odometry_4.png": "spins-ins.png",
        "SLAM_Odometry_5.png": "dlc-slam.png",
        
        # Multi-Robot Systems
        "Multi_Robot_1.png": "multi-robot-coverage.png",
        "Multi_Robot_2.png": "vision-plane-following.png",
        "Multi_Robot_3.png": "formation-control.png",
        
        # Hybrid Robots
        "Hybrid_Robots_1.png": "hybrid-robot-control.png",
        "Hybrid_Robots_2.png": "capsulebot-robot.png",
        "Hybrid_Robots_3.png": "sloped-terrain-control.png",
        "Hybrid_Robots_4.png": "cooperative-exploration.png",
        
        # Sensor Fusion
        "Sensors_Fusion_1.png": "av-pedestrian-awareness.png",
        "Sensors_Fusion_2.png": "av-drone-threat.png",
        "Sensors_Fusion_3.png": "hcto-odometry.png",
        
        # Other categories
        "Datasets_1.png": "ntu-viral-dataset.png",
        "Challenges_1.png": "cooperative-exploration.png",
        "Tethered_Robots_1.png": "neptune-tethered.png",
        "Tethered_Robots_2.png": "topological-braids.png"
    }
    
    source_dir = "publication_images"
    target_dir = "images"
    
    # Check if source directory exists
    if not os.path.exists(source_dir):
        print(f"Error: {source_dir} directory not found!")
        return
    
    # Check if target directory exists
    if not os.path.exists(target_dir):
        print(f"Error: {target_dir} directory not found!")
        return
    
    moved_count = 0
    
    for source_name, target_name in image_mapping.items():
        source_path = os.path.join(source_dir, source_name)
        target_path = os.path.join(target_dir, target_name)
        
        if os.path.exists(source_path):
            try:
                # Copy the image to the target directory
                shutil.copy2(source_path, target_path)
                print(f"✓ Moved {source_name} → {target_name}")
                moved_count += 1
            except Exception as e:
                print(f"✗ Error moving {source_name}: {e}")
        else:
            print(f"- Skipped {source_name} (file not found)")
    
    print(f"\nMove complete! Moved {moved_count} images to {target_dir}/ directory.")
    
    # Clean up the temporary publication_images directory
    try:
        shutil.rmtree(source_dir)
        print(f"✓ Cleaned up temporary {source_dir} directory")
    except Exception as e:
        print(f"⚠ Could not clean up {source_dir}: {e}")

if __name__ == "__main__":
    move_and_rename_images() 