import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHMTLNode(unittest.TestCase):
    def test1_props_to_html(self):
        props1 = {"href": "https://www.google.com"}
        node1 = HTMLNode(props = props1)
        self.assertEqual(node1.props_to_html(), ' href="https://www.google.com"')
        
    def test2_props_to_html(self):
        props2 = {"href": "https://www.google.com", "target" : "_blank"}
        node2 = HTMLNode(props = props2)
        self.assertEqual(node2.props_to_html(), ' href="https://www.google.com" target="_blank"')


class TestLeafNode(unittest.TestCase):
    def test1_to_html(self):
        node1 = LeafNode(tag="p", value="test message",props={"href": "https://www.google.com"})
        self.assertEqual(node1.to_html(), '<p href="https://www.google.com">test message</p>')

    def test2_to_html(self):
        node2 = LeafNode(tag="a", value="fortnite AA")
        self.assertEqual(node2.to_html(), '<a>fortnite AA</a>')


class TestParentNode(unittest.TestCase):
    def test1_to_html(self):
        node1 = ParentNode(tag="p",
            children=[
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ]
        )
        self.assertEqual(node1.to_html(), 
            "<p>"\
                "<b>Bold text</b>"\
                "Normal text"\
                "<i>italic text</i>"\
                "Normal text"\
            "</p>")
    
    def test2_to_html(self):
        node2 = ParentNode(tag="p",
            children=[
                ParentNode(tag="q",
                    children=[
                    LeafNode("b", "Bold text"),
                    LeafNode("b", "Bold text")
                    ]
                ),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ]
        )
        self.assertEqual(node2.to_html(), 
            "<p>"\
                "<q>"\
                    "<b>Bold text</b>"\
                    "<b>Bold text</b>"\
                "</q>"\
                "Normal text"\
                "<i>italic text</i>"\
                "Normal text"\
            "</p>"
        )


if __name__ == "__main__":
    unittest.main()
