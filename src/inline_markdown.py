import re
from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_link,
    text_type_image
)


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)


def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)


def get_link_text(link_tuple):
    return f"[{link_tuple[0]}]({link_tuple[1]})"


def get_image_text(image_tuple):
    return f"![{image_tuple[0]}]({image_tuple[1]})"


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        text: str = old_node.text
        extracted_links = extract_markdown_links(text)
        if old_node.text_type != text_type_text or len(extracted_links) == 0:
            new_nodes.append(old_node)
            continue
        split_nodes = []

        while len(extracted_links):
            link = extracted_links.pop(0)
            split_text = text.split(get_link_text(link), 1)
            text_node = split_text[0]
            if text_node != "":
                split_nodes.append(
                    TextNode(text=text_node, text_type=text_type_text))
            split_nodes.append(
                TextNode(text=link[0], text_type=text_type_link, url=link[1]))

            text = split_text[1]

        if text != "":
            split_nodes.append(TextNode(text=text, text_type=text_type_text))

        new_nodes.extend(split_nodes)
    return new_nodes


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        text: str = old_node.text
        extracted_images = extract_markdown_images(text)
        if old_node.text_type != text_type_text or len(extracted_images) == 0:
            new_nodes.append(old_node)
            continue
        split_nodes = []

        while len(extracted_images):
            image = extracted_images.pop(0)
            split_text = text.split(get_image_text(image), 1)
            text_node = split_text[0]
            if text_node != "":
                split_nodes.append(
                    TextNode(text=text_node, text_type=text_type_text))
            split_nodes.append(
                TextNode(text=image[0], text_type=text_type_image, url=image[1]))

            text = split_text[1]

        if text != "":
            split_nodes.append(TextNode(text=text, text_type=text_type_text))

        new_nodes.extend(split_nodes)
    return new_nodes


def text_to_textnodes(text):
    nodes = [TextNode(text, text_type_text)]
    nodes = split_nodes_delimiter(nodes, "**", text_type_bold)
    nodes = split_nodes_delimiter(nodes, "*", text_type_italic)
    nodes = split_nodes_delimiter(nodes, "`", text_type_code)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes
