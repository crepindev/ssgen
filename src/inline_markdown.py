import re
from enum import Enum
from textnode import (
    TextNode,
    TextType
)

def text_to_textnodes(text):
    nodes = [TextNode(text,TextType.text)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.bold)
    nodes = split_nodes_delimiter(nodes, "*", TextType.italic)
    nodes = split_nodes_delimiter(nodes, "`", TextType.code)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    # It takes a list of "old nodes", a delimiter, and a text type. 
    # It should return a new list of nodes, where any "text" type nodes 
    # in the input list are (potentially) split into multiple nodes based on the syntax.
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

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        text = old_node.text
        matches = extract_markdown_images(text)
        if len(matches) == 0:
            new_nodes.append(old_node)
        else:
            for match in matches:
                split_text = text.split(f"![{match[0]}]({match[1]})", 1)
                new_node_text = TextNode(split_text[0], TextType.text)
                new_node_image = TextNode(match[0], TextType.image, match[1])
                new_nodes.extend([new_node_text, new_node_image])
                text = split_text[1]
            if len(text) > 0:
                new_nodes.append(TextNode(text, TextType.text))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        text = old_node.text
        matches = extract_markdown_links(text)
        if len(matches) == 0:
            new_nodes.append(old_node)
        else: 
            for match in matches:
                split_text = text.split(f"[{match[0]}]({match[1]})", 1)
                new_node_text = TextNode(split_text[0], TextType.text)
                new_node_image = TextNode(match[0], TextType.link, match[1])
                new_nodes.extend([new_node_text, new_node_image])
                text = split_text[1]
            if len(text) > 0:
                new_nodes.append(TextNode(text, TextType.text))
    return new_nodes

def extract_markdown_images(text):
    # Takes raw text and returns a list of tuples. 
    # Each tuple should contain the alt text and the URL of any markdown images.
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_markdown_links(text):
    # This one should extract markdown links instead of images. 
    # It should return tuples of anchor text and URLs.
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches