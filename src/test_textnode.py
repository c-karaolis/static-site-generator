import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_equal(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    
    def test_not_equal(self):
        node = TextNode("This is a sdasd node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)
    
    def test_repr(self):
        node = TextNode("This is a text node", "bold")
        self.assertEqual(repr(node), "TextNode(This is a text node,bold,None)")
        
    def test_repr_with_url(self):
        node = TextNode("This is a text node", "bold", "http://www.google.com")
        self.assertEqual(repr(node), "TextNode(This is a text node,bold,http://www.google.com)")

    

if __name__ == "__main__":
    unittest.main()