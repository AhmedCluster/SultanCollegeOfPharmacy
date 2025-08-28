#!/usr/bin/env python3

import os
import re

# Define the directory containing the HTML files
dir_path = os.getcwd()

# Function to update paths in HTML files
def update_paths(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Update vision-mission.html references to about-us/vision-mission.html
    content = re.sub(r'href="vision-mission\.html"', r'href="about-us/vision-mission.html"', content)
    
    # Update goals-objectives.html references to about-us/goals-objectives.html
    content = re.sub(r'href="goals-objectives\.html"', r'href="about-us/goals-objectives.html"', content)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    
    print(f"Updated path references in {os.path.basename(file_path)}")

# Process all HTML files in the main directory
for filename in os.listdir(dir_path):
    if filename.endswith('.html') and filename != 'index.html':  # Skip index.html as we already updated it
        file_path = os.path.join(dir_path, filename)
        if os.path.isfile(file_path):
            update_paths(file_path)

print("All files updated successfully!")