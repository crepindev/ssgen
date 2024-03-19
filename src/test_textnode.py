import unittest

from textnode import *


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.bold)
        node2 = TextNode("This is a text node", TextType.bold)
        self.assertEqual(node1, node2)
    
    def test_textnode_to_htmlnode(self):
        #case1 - bold input text node
        input_node = TextNode("test",TextType.bold)
        output_node = textnode_to_htmlnode(input_node)
        self.assertEqual(output_node, LeafNode("b","test"))

if __name__ == "__main__":
    unittest.main()
