from enum import Enum
from htmlnode import LeafNode

class TextNode:
    def __init__(self, TEXT, TEXT_TYPE, URL=None):
        self.text = TEXT
        self.text_type = TEXT_TYPE
        self.url = URL

    def __eq__ (self, tn):
        if (self.text == tn.text and
            self.text_type == tn.text_type and
            self.url == tn.url):
            return True
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

class TextType(Enum):
    text = "text"
    bold = "bold"
    italic = "italic"
    code = "code"
    link = "link"
    image = "image"

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.text:
        return LeafNode(value=text_node.text)
    elif text_node.text_type == TextType.bold:
        return LeafNode(tag="b", value=text_node.text)
    elif text_node.text_type == TextType.italic:
        return LeafNode(tag="i", value=text_node.text)
    elif text_node.text_type == TextType.code:
        return LeafNode(tag="code", value=text_node.text)
    elif text_node.text_type == TextType.link:
        return LeafNode(tag="a", value=text_node.text, prop={"href": text_node.url})
    elif text_node.text_type == TextType.image:
        return LeafNode(tag="img", prop={"href": text_node.url, "alt": text_node.text})
    else:
        raise ValueError(f"unrecognised text type: {text_node.text_type}")