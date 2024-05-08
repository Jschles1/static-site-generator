import re
from html import escape
from htmlnode import ParentNode, LeafNode
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node

block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"


def get_header_tag_from_block(block):
    if block.startswith("# "):
        return "h1"
    elif block.startswith("## "):
        return "h2"
    elif block.startswith("### "):
        return "h3"
    elif block.startswith("#### "):
        return "h4"
    elif block.startswith("##### "):
        return "h5"
    elif block.startswith("###### "):
        return "h6"


def markdown_to_blocks(markdown: str):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks


def block_to_block_type(block):
    lines = block.split("\n")

    if (
        block.startswith("# ")
        or block.startswith("## ")
        or block.startswith("### ")
        or block.startswith("#### ")
        or block.startswith("##### ")
        or block.startswith("###### ")
    ):
        return block_type_heading
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return block_type_code
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return block_type_paragraph
        return block_type_quote
    if block.startswith("* "):
        for line in lines:
            if not line.startswith("* "):
                return block_type_paragraph
        return block_type_unordered_list
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return block_type_paragraph
        return block_type_unordered_list
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return block_type_paragraph
            i += 1
        return block_type_ordered_list
    return block_type_paragraph


def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)

    children = []
    for block in blocks:
        block_type = block_to_block_type(block)
        lines = block.split("\n")

        if block_type == block_type_quote:
            blockquote = LeafNode("blockquote", " ".join(
                list(map(lambda x: x.lstrip("> "), lines))))
            children.append(blockquote)
        elif block_type == block_type_unordered_list:
            ul = ParentNode("ul", [])
            for line in lines:
                li_text = line.lstrip("- ")
                li = ParentNode("li", [])
                text_nodes = text_to_textnodes(li_text)
                for node in text_nodes:
                    li.children.append(text_node_to_html_node(node))
                ul.children.append(li)
            children.append(ul)
        elif block_type == block_type_ordered_list:
            ol = ParentNode("ol", [])
            i = 1
            for line in lines:
                li_text = line.strip(f"{i}. ")
                li = ParentNode("li", [])
                text_nodes = text_to_textnodes(li_text)
                for node in text_nodes:
                    li.children.append(text_node_to_html_node(node))
                ol.children.append(li)
                i += 1
            children.append(ol)
        elif block_type == block_type_code:
            code = LeafNode("code", escape(block).replace("```", "").strip())
            pre = ParentNode("pre", [code])
            children.append(pre)
        elif block_type == block_type_heading:
            tag = get_header_tag_from_block(block)
            header_text = block.lstrip("# ")
            header = ParentNode(tag, [])
            text_nodes = text_to_textnodes(header_text)
            for node in text_nodes:
                header.children.append(text_node_to_html_node(node))
            children.append(header)
        elif block_type == block_type_paragraph:
            p_text = " ".join(
                list(map(lambda x: x.strip(), block.split("\n"))))
            text_nodes = text_to_textnodes(p_text)
            p = ParentNode("p", [])
            if len(text_nodes):
                for node in text_nodes:
                    p.children.append(text_node_to_html_node(node))
                children.append(p)

    node = ParentNode('div', children=children)
    return node
