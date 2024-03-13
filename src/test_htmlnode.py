import unittest

from htmlnode import HTMLNode


class TestHMTLNode(unittest.TestCase):
    def test_props_to_html(self):
        props1 = {"href": "https://www.google.com"}
        props2 = {"href": "https://www.google.com", "target" : "_blank"}
        node = HTMLNode(props = props1)
        node2 = HTMLNode(props = props2)
        case1 = (node.props_to_html() == " href = https://www.google.com")
        case2 = (node2.props_to_html() ==  ' href=https://www.google.com target="_blank"')
        return f"case1={case1}, case2={case2}"


if __name__ == "__main__":
    unittest.main()
