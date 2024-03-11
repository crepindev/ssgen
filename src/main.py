from textnode import TextNode

def main():
    TEXT = "Hello there"
    TEXT_TYPE = "italics"
    URL = "www.goole.com"
    newTextNode = TextNode(TEXT, TEXT_TYPE, URL)
    print(newTextNode)
    pass

main()