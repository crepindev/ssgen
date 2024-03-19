import unittest

from inline_markdown import *
from textnode import (TextNode, TextType)

class Test_Inline_Markdown(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        #case1 - code text type
        node = TextNode("This is text with a `code block` word", TextType.text)
        actual_result = split_nodes_delimiter([node], "`", TextType.code)
        expected_result = [
            TextNode("This is text with a ", TextType.text),
            TextNode("code block", TextType.code),
            TextNode(" word", TextType.text),
        ]
        self.assertListEqual(actual_result, expected_result)

        #case2 - bold text type
        node = TextNode("This is text with a **bold block** word", TextType.text)
        actual_result = split_nodes_delimiter([node], "**", TextType.bold)
        expected_result = [
            TextNode("This is text with a ", TextType.text),
            TextNode("bold block", TextType.bold),
            TextNode(" word", TextType.text),
        ]
        self.assertListEqual(actual_result, expected_result)

        #case3 - multiple splits in single input node
        node = TextNode("This is a **bold block** here and another **bold block** over there", TextType.text)
        actual_result = split_nodes_delimiter([node], "**", TextType.bold)
        expected_result = [
            TextNode("This is a ", TextType.text),
            TextNode("bold block", TextType.bold),
            TextNode(" here and another ", TextType.text),
            TextNode("bold block", TextType.bold),
            TextNode(" over there", TextType.text)
        ]
        self.assertListEqual(actual_result, expected_result)
        
        #case4 - multiple input nodes
        node1 = TextNode("This is text with a `code block` word", TextType.text)
        node2 = TextNode("This is text with another `code block` word", TextType.text)
        actual_result = split_nodes_delimiter([node1, node2], "`", TextType.code)
        expected_result = [
            TextNode("This is text with a ", TextType.text),
            TextNode("code block", TextType.code),
            TextNode(" word", TextType.text),
            TextNode("This is text with another ", TextType.text),
            TextNode("code block", TextType.code),
            TextNode(" word", TextType.text),
        ]
        self.assertListEqual(actual_result, expected_result)

    def test_split_nodes_image(self):
        #case1 - single node with multiple images
        node = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and "\
                "another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.text,
        )
        actual_result = split_nodes_image([node])
        expected_result = [
            TextNode("This is text with an ", TextType.text),
            TextNode("image", TextType.image, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.text),
            TextNode("second image", TextType.image, "https://i.imgur.com/3elNhQu.png"),
        ]
        self.assertListEqual(actual_result, expected_result)

        #case2 - multiple input nodes
        node1 = TextNode(
            "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and "\
                "another ![second image](https://i.imgur.com/3elNhQu.png)",
            TextType.text,
        )
        node2 = TextNode("The REAL Jon Snow ![image](https://imgur.com/gallery/pFzbAtA)", TextType.text)
        actual_result = split_nodes_image([node1, node2])
        expected_result = [
            TextNode("This is text with an ", TextType.text),
            TextNode("image", TextType.image, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.text),
            TextNode("second image", TextType.image, "https://i.imgur.com/3elNhQu.png"),
            TextNode("The REAL Jon Snow ", TextType.text),
            TextNode("image", TextType.image, "https://imgur.com/gallery/pFzbAtA")
        ]
        self.assertListEqual(actual_result, expected_result)

    def test_split_nodes_link(self):
        #case1 - single node with multiple links
        node = TextNode(
            "This is text with a [link](https://i.imgur.com/zjjcJKZ.png) and "\
                "another [second link](https://i.imgur.com/3elNhQu.png)",
            TextType.text,
        )
        actual_result = split_nodes_link([node])
        expected_result = [
            TextNode("This is text with a ", TextType.text),
            TextNode("link", TextType.link, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.text),
            TextNode("second link", TextType.link, "https://i.imgur.com/3elNhQu.png"),
        ]
        self.assertListEqual(actual_result, expected_result)

        #case2 - multiple input nodes
        node1 = TextNode(
            "This is text with a [link](https://i.imgur.com/zjjcJKZ.png) and "\
                "another [second link](https://i.imgur.com/3elNhQu.png)",
            TextType.text,
        )
        node2 = TextNode("The REAL Jon Snow [is here](https://imgur.com/gallery/pFzbAtA)", TextType.text)
        actual_result = split_nodes_link([node1, node2])
        expected_result = [
            TextNode("This is text with a ", TextType.text),
            TextNode("link", TextType.link, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and another ", TextType.text),
            TextNode("second link", TextType.link, "https://i.imgur.com/3elNhQu.png"),
            TextNode("The REAL Jon Snow ", TextType.text),
            TextNode("is here", TextType.link, "https://imgur.com/gallery/pFzbAtA")
        ]
        self.assertListEqual(actual_result, expected_result)

    def test_text_to_textnodes(self):
        example_input = "This is **text** with an *italic* word and a `code block` and "\
            "an ![image](https://i.imgur.com/zjjcJKZ.png) and a [link](https://boot.dev)"
        actual_result = text_to_textnodes(example_input)
        expected_result = [
            TextNode("This is ", TextType.text),
            TextNode("text", TextType.bold),
            TextNode(" with an ", TextType.text),
            TextNode("italic", TextType.italic),
            TextNode(" word and a ", TextType.text),
            TextNode("code block", TextType.code),
            TextNode(" and an ", TextType.text),
            TextNode("image", TextType.image, "https://i.imgur.com/zjjcJKZ.png"),
            TextNode(" and a ", TextType.text),
            TextNode("link", TextType.link, "https://boot.dev"),
        ]
        self.assertListEqual(actual_result, expected_result)

    def test_extract_markdown_images(self):
        #case1 
        text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and "\
            "![another](https://i.imgur.com/dfsdkjfd.png)"
        matches = extract_markdown_images(text)
        expected_result = [
            ("image", "https://i.imgur.com/zjjcJKZ.png"),
            ("another", "https://i.imgur.com/dfsdkjfd.png")
        ]
        self.assertListEqual(matches, expected_result)

    def test_extract_markdown_links(self):
        text = "This is text with a [link](https://www.example.com) and "\
            "[another](https://www.example.com/another)"
        matches = extract_markdown_links(text)
        expected_result = [
            ("link", "https://www.example.com"), 
            ("another", "https://www.example.com/another")
        ]
        self.assertListEqual(matches, expected_result)

if __name__ == "__main__":
    unittest.main()