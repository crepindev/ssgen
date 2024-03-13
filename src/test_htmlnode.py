import unittest

from htmlnode import HTMLNode, LeafNode


class TestHMTLNode(unittest.TestCase):
    def test_props_to_html(self):
        props1 = {"href": "https://www.google.com"}
        props2 = {"href": "https://www.google.com", "target" : "_blank"}
        node1 = HTMLNode(props = props1)
        node2 = HTMLNode(props = props2)
        case1 = (node1.props_to_html() == " href = https://www.google.com")
        case2 = (node2.props_to_html() ==  ' href=https://www.google.com target="_blank"')
        return case1 and case2

class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node1 = LeafNode(value="test message",tag="p",props={"href": "https://www.google.com"})
        node2 = LeafNode(value="fortnite AA",tag="a")
        case1 = (node1.to_html() == '<p href="https://www.google.com">test message</p>')
        case2 = (node2.to_html() == '<a>fortnite AA</a>')
        return case1 and case2

if __name__ == "__main__":
    unittest.main()
