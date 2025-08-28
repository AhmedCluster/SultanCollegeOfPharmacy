#!/usr/bin/env python3

import os
import re

# Define the directory containing the HTML files
dir_path = os.path.dirname(os.path.abspath(__file__))

# Function to update paths in HTML files
def update_paths(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Update ../goals-objectives.html references to goals-objectives.html
    content = re.sub(r'href="\.\./(goals-objectives\.html)"', r'href="\1"', content)
    
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)
    
    print(f"Updated path references in {os.path.basename(file_path)}")

# Process all HTML files in the about-us directory
for filename in os.listdir(dir_path):
    if filename.endswith('.html'):
        file_path = os.path.join(dir_path, filename)
        if os.path.isfile(file_path):
            update_paths(file_path)

print("All files in about-us directory updated successfully!")