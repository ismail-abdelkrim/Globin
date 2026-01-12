import csv
import os

output_dir = "src/content/products"
os.makedirs(output_dir, exist_ok=True)

csv_file = "products.csv"

print("Starting generation...")

try:
    with open(csv_file, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        count = 0
        for row in reader:
            safe_slug = "".join([c if c.isalnum() else "-" for c in row['title']]).lower()
            filename = f"{output_dir}/{safe_slug}.md"
            
            markdown_content = f"""---
title: "{row['title']}"
price: "{row['price']}"
image: "{row['image_url']}"
link: "{row['affiliate_link']}"
---

{row['description']}
"""
            # إنشاء الملف
            with open(filename, "w", encoding='utf-8') as f:
                f.write(markdown_content)
            
            count += 1

    print(f"Success! Generated {count} product pages.")

except FileNotFoundError:
    print("Error: Could not find products.csv file.")
except Exception as e:
    print(f"An error occurred: {e}")
