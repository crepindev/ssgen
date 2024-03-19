from enum import Enum
from htmlnode import *
import re

class TextType(Enum):
    text = "text"
    bold = "bold"
    italic = "italic"
    code = "code"
    link = "link"
    image = "image"


class TextNode:
    def __init__(self, TEXT, TEXT_TYPE, URL=None):
        self.text = TEXT
        self.text_type = TEXT_TYPE
        self.url = URL
        if not isinstance(TEXT_TYPE, TextType):
            raise TypeError("only accepts Enum class 'TextType' as input for TEXT_TYPE")

    def __eq__ (self, tn):
        if (self.text == tn.text and
            self.text_type == tn.text_type and
            self.url == tn.url):
            return True
        return False
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"


def textnode_to_htmlnode(textnode):
    if textnode.text_type == TextType.text:
        return LeafNode(value=textnode.text)
    elif textnode.text_type == TextType.bold:
        return LeafNode(tag="b", value=textnode.text)
    elif textnode.text_type == TextType.italic:
        return LeafNode(tag="i", value=textnode.text)
    elif textnode.text_type == TextType.code:
        return LeafNode(tag="code", value=textnode.text)
    elif textnode.text_type == TextType.link:
        return LeafNode(tag="a", value=textnode.text, prop={"href": textnode.url})
    elif textnode.text_type == TextType.image:
        return LeafNode(tag="img", prop={"href": textnode.url, "alt": textnode.text})
    else:
        raise ValueError(f"unrecognised text type: {textnode.text_type}")  

