import os
from markdown_blocks import markdown_to_htmlnode

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[1:].strip()
    raise Exception("no h1 header found")

def generate_page(from_path, template_path, dest_path):
    if not os.path.exists(from_path):
        raise Exception(f"{from_path} does not exist")
    if not os.path.exists(template_path):
        raise Exception(f"{template_path} does not exist")
    if not os.path.exists(os.path.dirname(dest_path)):
        os.makedirs(os.path.dirname(dest_path))
    with open(from_path, "r") as f:
        markdown = f.read()
    with open(template_path, "r") as f:
        template = f.read()
    node = markdown_to_htmlnode(markdown)
    content = node.to_html()
    title = extract_title(markdown)
    html = template.replace("{{ Title }}", title).replace("{{ Content }}", content)
    with open(dest_path, "w") as f:
        f.write(html)

def generate_pages_recursive(from_path_content, template_path, dest_dir_path):
    contents = os.listdir(from_path_content)    
    for item in contents:
        file_path = os.path.join(from_path_content, item)
        dest_path = os.path.join(dest_dir_path, item)
        if os.path.isfile(file_path):
            dest_path = dest_path.replace(".md",".html")
            generate_page(file_path, template_path, dest_path)
            print(f"written {item} to {dest_path}...")
        else:
            generate_pages_recursive(file_path, template_path, dest_path)
        
    