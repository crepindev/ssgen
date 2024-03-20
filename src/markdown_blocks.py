import re
from enum import Enum

from htmlnode import *
from inline_markdown import text_to_textnodes
from textnode import textnode_to_htmlnode

class BlockType(Enum):
    paragraph = "paragraph"
    heading = "heading"
    code = "code"
    quote = "quote"
    ulist = "unordered_list"
    olist = "ordered_list"

def markdown_to_blocks(markdown):
    matches = set(re.findall("\n{2,}", markdown))
    blocks = []
    for match in set(matches):
        blocks.extend(list(filter(None,markdown.split(match))))
    output = [block.strip(" ") for block in blocks]
    return output

def markdown_to_htmlnode(markdown):
    #top level function that converts a full markdown document into a HTML node
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        htmlnode = block_to_htmlnode(block)
        children.append(htmlnode)
    return ParentNode("div", children, None)

def block_to_htmlnode(block):
    #takes a block, identifies it's type and calls appropriate function to return HTMLNode
    block_type = block_to_blocktype(block)
    if block_type == BlockType.paragraph:
        return paragraph_to_htmlnode(block)
    elif block_type == BlockType.heading:
        return heading_to_htmlnode(block)
    elif block_type == BlockType.code:
        return code_to_htmlnode(block)
    elif block_type == BlockType.olist:
        return olist_to_htmlnode(block)
    elif block_type == BlockType.ulist:
        return ulist_to_htmlnode(block)
    elif block_type == BlockType.quote:
        return quote_to_htmlnode(block)
    else:
        raise ValueError("Invalid block type")

def block_to_blocktype(block):
    block_start = block.split()[0]
    block_end = block.split()[-1]
    lines = block.split("\n")
    len_lines = len(lines)
    if re.findall(r"#{1,6}", block_start) != []:
        return BlockType.heading
    elif block_start == "```" and block_end == "```":
        return BlockType.code
    else:
        outcome_counter = {"q": 0, "ul": 0, "ol": 0}
        ol_counter = 1
        for line in lines:
            line = line.strip()
            line_start = line.split("\n")[0]
            if line_start[0] == ">":
                outcome_counter["q"] += 1
            elif line_start[0] in "*-"  :
                outcome_counter["ul"] += 1
            elif (re.findall(r"\d\.", line_start) != []) and (int(line_start[0]) == ol_counter):
                outcome_counter["ol"] += 1
                ol_counter += 1
        if outcome_counter["q"] == len_lines:
            return BlockType.quote
        elif outcome_counter["ul"] == len_lines:
            return BlockType.ulist
        elif outcome_counter["ol"] == len_lines:
            return BlockType.olist
        else:
            return BlockType.paragraph

def text_to_children(text):
    textnodes = text_to_textnodes(text)
    children = []
    for textnode in textnodes:
        htmlnode = textnode_to_htmlnode(textnode)
        children.append(htmlnode)
    return children

def paragraph_to_htmlnode(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)

def heading_to_htmlnode(block):
    header = block.split("\n")[0]
    header_level = header.count("#")
    children = text_to_children(block[header_level:].strip())
    return ParentNode(f"h{header_level}", children)

def code_to_htmlnode(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")
    text = block.strip("```").strip()
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])

def olist_to_htmlnode(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)

def ulist_to_htmlnode(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)

def quote_to_htmlnode(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)

