import re
from enum import Enum

from htmlnode import ParentNode
#from inline_markdown import text_to_textnodes
#from textnode import textnode_to_htmlnode

class BlockType(Enum):
    paragraph = "paragraph"
    heading = "heading"
    code = "code"
    quote = "quote"
    unordered_list = "unordered_list"
    ordered_list = "ordered_list"

def markdown_to_blocks(markdown):
    matches = set(re.findall("\n{2,}", markdown))
    blocks = []
    for match in matches:
        blocks.extend(markdown.split(match))
    return ([block.strip(" ") for block in blocks])

def markdown_to_html_node(markdown):
    #top level function that converts a full markdown document into a HTML node
    pass

def block_to_html_node(block):
    #takes a block, identifies it's type and calls appropriate function to return HTMLNode
    block_type = block_to_block_type(block)
    if block_type == BlockType.paragraph:
        pass
    elif block_type == BlockType.heading:
        pass
    elif block_type == BlockType.code:
        pass
    elif block_type == BlockType.ordered_list:
        pass
    elif block_type == BlockType.unordered_list:
        pass
    elif block_type == BlockType.quote:
        pass
    else:
        raise ValueError("Invalid block type")

def block_to_block_type(block):
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
            return BlockType.unordered_list
        elif outcome_counter["ol"] == len_lines:
            return BlockType.ordered_list
        else:
            return BlockType.paragraph
        
# review below this line against solution

def paragraph_block_to_html_node(block):
    if block_to_block_type(block) != BlockType.paragraph:
        raise ValueError("incorrect block type for this function")
    return HTMLNode("p", block)

def heading_block_to_html_node(block):
    if block_to_block_type(block) != BlockType.heading:
        raise ValueError("incorrect block type for this function")
    header = block.strip("\n")[0]
    header_level = len(re.findall("#{1,6}",header)[0])
    return HTMLNode(f"h{header_level}", block)

def code_block_to_html_node(block):
    if block_to_block_type(block) != BlockType.code:
        raise ValueError("incorrect block type for this function")
    return HTMLNode("pre",None,HTMLNode("code", block))