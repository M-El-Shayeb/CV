import os
import re

def revert_images(html_file):
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    images = [
        "chatglm-profile.jpg",
        "profile2.png",
        "zarqa-logo.png",
        "University_of_the_People_Logo.jpg",
        "cv-certificate.png",
        "cisco-ds-certificate.png",
        "ecommerce_service.png",
        "invoice_operations.png",
        "smart_camera.png",
        "smart_menu.png",
        "custom_ai.png",
        "social-media-service.png"
    ]
    
    # We will use re.sub with a function to replace each match with the corresponding image name
    # Ensure we only match exactly what we need
    pattern = re.compile(r'src="data:image/[^;]+;base64,[^"]+"')
    
    def replacer(match):
        if hasattr(replacer, "counter"):
            img = images[replacer.counter]
            replacer.counter += 1
            return f'src="{img}"'
        return match.group(0)
        
    replacer.counter = 0

    new_html = pattern.sub(replacer, html_content)

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Reverted to local filenames successfully.")

revert_images('index.html')
