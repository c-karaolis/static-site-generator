import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("div", "This is a text node")
        self.assertEqual(repr(node), "HTMLNode(div,This is a text node,None,None)")
        
    def test_repr_with_props(self):
        node = HTMLNode("div", "This is a text node", props={"class": "bold"})
        self.assertEqual(repr(node), "HTMLNode(div,This is a text node,None,{'class': 'bold'})")
    
    def test_props_to_html(self):
        node = HTMLNode("div", "This is a text node", props={"class": "bold"})
        self.assertEqual(node.props_to_html(), 'class="bold"')
        
    def test_props_to_html_empty(self):
        node = HTMLNode("div", "This is a text node")
        self.assertEqual(node.props_to_html(), "")
        
    def test_props_to_html_with_multiple_props(self):
        node = HTMLNode("div", "This is a text node", props={"class": "bold", "href": "http://www.google.com"})
        
    # LeafNode tests
    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")