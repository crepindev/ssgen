from copystatic import copy_static
from generate_page import generate_pages_recursive

def main():
    print(f"copied files: {copy_static()}")
    generate_pages_recursive("./content", "./template.html", "./public")
    print("pages ready...")

main()