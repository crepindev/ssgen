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

    def test_block_to_blocktype(self):
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
            "block3": BlockType.ulist,
            "block4": BlockType.paragraph,
            "block5": BlockType.olist,
            "block6": BlockType.code,
            "block7": BlockType.quote
        }
        for key in input_dict:
            input_value = input_dict[key]
            expected_value = output_dict[key]
            actual_value = block_to_blocktype(input_value)
            self.assertEqual(expected_value, actual_value)

    def test_text_to_children(self):
        input_str = "This is **text** with an *italic* word and a `code block` and "\
            "an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
        output_list = [
            LeafNode(value="This is "),
            LeafNode(tag="b", value="text"),
            LeafNode(value=" with an "),
            LeafNode(tag="i", value="italic"),
            LeafNode(value=" word and a "),
            LeafNode(tag="code", value="code block"),
            LeafNode(value=" and an "),
            LeafNode(tag="img", props={"href":"https://i.imgur.com/zjjcJKZ.png", "alt": "image"}),
            LeafNode(value=" and a "),
            LeafNode(tag="a", value="link", props={"href": "https://boot.dev"}),
        ]
        self.assertListEqual(output_list, text_to_children(input_str))

    def test_paragraph_to_htmlnode(self):
        md = "This is **bolded** paragraph text in a p tag here\n\n" \
            "This is another paragraph with *italic* text and `code` here"
        node = markdown_to_htmlnode(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><p>This is <b>bolded</b> paragraph text in a p tag here</p><p>This is another paragraph with <i>italic</i> text and <code>code</code> here</p></div>",
        )

    def test_heading_to_htmlnode(self):
        md = "# this is an h1\n\nthis is paragraph text\n\n## this is an h2"
        node = markdown_to_htmlnode(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><h1>this is an h1</h1><p>this is paragraph text</p><h2>this is an h2</h2></div>",
        )

    def test_code_to_htmlnode(self):
        pass

    def test_lists_to_htmlnode(self):
        md = "- This is a list\n- with items\n- and *more* items\n\n" \
        "1. This is an `ordered` list\n" \
        "2. with items\n3. and more items"
        node = markdown_to_htmlnode(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><ul><li>This is a list</li><li>with items</li><li>and <i>more</i> items</li></ul><ol><li>This is an <code>ordered</code> list</li><li>with items</li><li>and more items</li></ol></div>",
        )

    def test_quote_to_htmlnode(self):
        md = "> This is a\n> blockquote block\n\nthis is paragraph text"
        node = markdown_to_htmlnode(md)
        html = node.to_html()
        self.assertEqual(
            html,
            "<div><blockquote>This is a blockquote block</blockquote><p>this is paragraph text</p></div>",
        )


if __name__ == "__main__":
    unittest.main()