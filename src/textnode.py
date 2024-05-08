from htmlnode import LeafNode


text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"


class TextNode:
    def __init__(self, text: str, text_type: str, url: str = None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other) -> bool:
        return self.text == other.text and self.text_type == other.text_type and self.url == other.url

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


def text_node_to_html_node(text_node):
    text_type = text_node.text_type

    if text_type == text_type_text:
        return LeafNode(None, text_node.text)
    if text_type == text_type_bold:
        return LeafNode("b", text_node.text)
    if text_type == text_type_italic:
        return LeafNode("i", text_node.text)
    if text_type == text_type_code:
        return LeafNode("code", text_node.text)
    if text_type == text_type_link:
        return LeafNode(tag="a", value=text_node.text, props={'href': text_node.url})
    if text_type == text_type_image:
        return LeafNode(tag="img", value="", props={'src': text_node.url, 'alt': text_node.text})
    raise Exception("Invalid text type")
