import os
import re
import base64
import mimetypes

def embed_images_as_base64(html_file):
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()

    # Regex to find <img src="...">
    # We will match anything that looks like src="filename.ext" where filename is local
    pattern = re.compile(r'src="([^"]+\.(png|jpg|jpeg|gif|webp))"', re.IGNORECASE)

    def replace_src(match):
        img_path = match.group(1)
        # Skip if it's already a data URI or external URL
        if img_path.startswith('data:') or img_path.startswith('http://') or img_path.startswith('https://'):
            return match.group(0)
            
        full_path = os.path.join(os.path.dirname(html_file), img_path)
        if os.path.exists(full_path):
            try:
                mime_type, _ = mimetypes.guess_type(img_path)
                if not mime_type:
                    if img_path.lower().endswith('.jpg') or img_path.lower().endswith('.jpeg'):
                        mime_type = 'image/jpeg'
                    elif img_path.lower().endswith('.png'):
                        mime_type = 'image/png'
                    else:
                        mime_type = 'application/octet-stream'
                
                with open(full_path, 'rb') as img_file:
                    encoded_string = base64.b64encode(img_file.read()).decode('utf-8')
                
                new_src = f'src="data:{mime_type};base64,{encoded_string}"'
                print(f"Embedded {img_path}")
                return new_src
            except Exception as e:
                print(f"Error encoding {img_path}: {e}")
                return match.group(0)
        else:
            print(f"File not found: {img_path}")
            return match.group(0)

    new_html = pattern.sub(replace_src, html_content)

    with open(html_file, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print("Done writing to " + html_file)

embed_images_as_base64('index.html')
