import unittest
from markdown_blocks import *

class Test_Markdown_Blocks(unittest.TestCase):
    def test_markdown_to_blocks(self):
        example_input = "This is **bolded** paragraph\n" \
            "\n" \
            "This is another paragraph with *italic* text and `code` here\n" \
            "This is the same paragraph on a new line\n" \
            "\n" \
            "* This is a list\n" \
            "* with items\n"
        actual_result = markdown_to_blocks(example_input)
        expected_result = [
            "This is **bolded** paragraph", 
            "This is another paragraph with *italic* text and `code` here\n" \
                "This is the same paragraph on a new line", 
            "* This is a list\n* with items\n"]
        self.assertEqual(actual_result, expected_result)

    def test_block_to_block_type(self):
        input_dict = {
            "block1": "# This is a heading",
            "block2": "### This is a L3 heading",
            "block3": "* This is a list item\n* This is another list item",
            "block4": "This is a paragraph of text." \
                "It has some **bold** and *italic* words inside of it.",
            "block5": "1. This an an OL item\n2. This is another OL item\n3. And another",
            "block6": "```\ncode goes here.\n```",
            "block7": ">be me\n>greentext\n>ishiggydiggy"
        }
        output_dict = {
            "block1": BlockType.heading,
            "block2": BlockType.heading,
            "block3": BlockType.unordered_list,
            "block4": BlockType.paragraph,
            "block5": BlockType.ordered_list,
            "block6": BlockType.code,
            "block7": BlockType.quote
        }
        for key in input_dict:
            input_value = input_dict[key]
            expected_value = output_dict[key]
            actual_value = block_to_block_type(input_value)
            self.assertEqual(expected_value, actual_value)

if __name__ == "__main__":
    unittest.main()