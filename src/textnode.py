from enum import Enum
from htmlnode import LeafNode

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
    
def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    if text_type not in TextType:
        raise Exception("invalid text type")
    for old_node in old_nodes:
        if isinstance(old_node, TextNode) and old_node.text_type == TextType.text:
            old_node_text = old_node.text
            if old_node_text.count(delimiter) % 2 == 1:
                raise Exception("invalid Markdown syntax, matching delimiter missing")
            text_list = old_node_text.split(sep=delimiter)
            for i in range(0,len(text_list)):
                if i % 2 == 0:
                    new_nodes.append(TextNode(text_list[i], TextType.text))
                else:
                    new_nodes.append(TextNode(text_list[i], text_type))
        else:
            new_nodes.append(old_node)
    return new_nodes
