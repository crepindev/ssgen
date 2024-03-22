from textnode import TextNode
from copystatic import copy_static
from generate_page import generate_page

def main():
    print(f"copied files: {copy_static()}")
    generate_page("./content/index.md", "./template.html", "./public/index.html")
    print("page ready...")

main()