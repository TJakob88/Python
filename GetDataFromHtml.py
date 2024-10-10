import re

# Specify the file path
file_path = r'C:\temp\phuketRestaurants.txt'

# Read the HTML file content
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Regex pattern to find data-restaurant-name="..."
pattern = r'data-restaurant-name="(.*?)"'

# Find all restaurant names
restaurant_names = re.findall(pattern, html_content)

# Remove duplicates by converting the list to a set
unique_restaurant_names = set(restaurant_names)

# Output the list of unique restaurant names
for name in unique_restaurant_names:
    print(name)
