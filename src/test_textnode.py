import unittest

from textnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.bold)
        node2 = TextNode("This is a text node", TextType.bold)
        self.assertEqual(node1, node2)
    
    def test_text_node_to_html_node(self):
        #case1 - bold input text node
        input_node = TextNode("test",TextType.bold)
        output_node = text_node_to_html_node(input_node)
        self.assertEqual(output_node, LeafNode("b","test"))
    
    def test_split_nodes_delimiter(self):
        #case1 - code text type
        node = TextNode("This is text with a `code block` word", TextType.text)
        new_nodes = split_nodes_delimiter([node], "`", TextType.code)
        expected_outcome = [
            TextNode("This is text with a ", TextType.text),
            TextNode("code block", TextType.code),
            TextNode(" word", TextType.text),
        ]
        for i in range(0,len(expected_outcome)):
            self.assertEqual(new_nodes[i], expected_outcome[i])

        #case2 - bold text type
        node = TextNode("This is text with a **bold block** word", TextType.text)
        new_nodes = split_nodes_delimiter([node], "**", TextType.bold)
        expected_outcome = [
            TextNode("This is text with a ", TextType.text),
            TextNode("bold block", TextType.bold),
            TextNode(" word", TextType.text),
        ]
        for i in range(0,len(expected_outcome)):
            self.assertEqual(new_nodes[i], expected_outcome[i])

        #case3 - multiple splits in single input node
        node = TextNode("This is a **bold block** here and another **bold block** over there", TextType.text)
        new_nodes = split_nodes_delimiter([node], "**", TextType.bold)
        expected_outcome = [
            TextNode("This is a ", TextType.text),
            TextNode("bold block", TextType.bold),
            TextNode(" here and another ", TextType.text),
            TextNode("bold block", TextType.bold),
            TextNode(" over there", TextType.text)
        ]
        for i in range(0,len(expected_outcome)):
            self.assertEqual(new_nodes[i], expected_outcome[i])
        
        #case4 - multiple input nodes
        node1 = TextNode("This is text with a `code block` word", TextType.text)
        node2 = TextNode("This is text with another `code block` word", TextType.text)
        new_nodes = split_nodes_delimiter([node1, node2], "`", TextType.code)
        expected_outcome = [
            TextNode("This is text with a ", TextType.text),
            TextNode("code block", TextType.code),
            TextNode(" word", TextType.text),
            TextNode("This is text with another ", TextType.text),
            TextNode("code block", TextType.code),
            TextNode(" word", TextType.text),
        ]
        for i in range(0,len(expected_outcome)):
            self.assertEqual(new_nodes[i], expected_outcome[i])
        





if __name__ == "__main__":
    unittest.main()
