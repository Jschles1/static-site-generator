import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        props = {"href": "https://www.google.com", "target": "_blank"}
        html_node = HTMLNode('h1', 'Hello', None, props)
        self.assertEqual(html_node.props_to_html(),
                         'href="https://www.google.com" target="_blank"')


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node = LeafNode("p", "This is a paragraph of text.")
        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node.to_html(), '<p>This is a paragraph of text.</p>')
        self.assertEqual(
            node2.to_html(), '<a href="https://www.google.com">Click me!</a>')

    def test_no_tag(self):
        node = LeafNode(None, "This is a paragraph of text.")
        self.assertEqual(node.to_html(), "This is a paragraph of text.")

    def test_no_value(self):
        node = LeafNode("p", None)
        self.assertRaises(ValueError, node.to_html)


class TestParentNode(unittest.TestCase):
    def test_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(
        ), "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")

        node2 = ParentNode(
            "div",
            [
                ParentNode(
                    "div",
                    [
                        LeafNode("p", "Paragraph"),
                        LeafNode("p", "Paragraph 2"),
                    ]
                ),
                ParentNode(
                    "div",
                    [
                        LeafNode("p", "Paragraph 3"),
                        LeafNode("a", "Click me!", {
                                 "href": "https://www.google.com"})
                    ]
                )
            ],
        )

        self.assertEqual(node2.to_html(
        ), '<div><div><p>Paragraph</p><p>Paragraph 2</p></div><div><p>Paragraph 3</p><a href="https://www.google.com">Click me!</a></div></div>')


if __name__ == "__main__":
    unittest.main()
