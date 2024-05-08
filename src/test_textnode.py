import unittest

from textnode import TextNode, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node!", "bold")
        self.assertNotEqual(node, node2)

    def test_url_none(self):
        node = TextNode("This is a text node", "bold")
        self.assertEqual(node.url, None)

    def test_text_node_to_html_node(self):
        node = TextNode("This is a text node", "text")
        html_node = text_node_to_html_node(node)
        node2 = TextNode("This is a text node", "bold")
        html_node2 = text_node_to_html_node(node2)
        node3 = TextNode("This is a text node", "code")
        html_node3 = text_node_to_html_node(node3)
        node4 = TextNode("This is a text node", "link", "https://google.com")
        html_node4 = text_node_to_html_node(node4)
        node5 = TextNode("This is a text node", "image",
                         "https://google.com/logo.jpg")
        html_node5 = text_node_to_html_node(node5)

        self.assertEqual(html_node.value, "This is a text node")
        self.assertEqual(html_node2.value, "This is a text node")
        self.assertEqual(html_node3.value, "This is a text node")
        self.assertEqual(html_node4.value, "This is a text node")
        self.assertEqual(html_node4.props, {'href': 'https://google.com'})
        self.assertEqual(html_node5.value, "")
        self.assertEqual(html_node5.props, {
                         'src': 'https://google.com/logo.jpg', 'alt': 'This is a text node'})


if __name__ == "__main__":
    unittest.main()
