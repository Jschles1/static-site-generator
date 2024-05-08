from os import path, listdir, makedirs
from markdown_blocks import markdown_to_html_node


def extract_title(markdown):
    lines = markdown.strip().split("\n")
    if not lines[0].startswith("# "):
        raise Exception("No h1 provided")
    else:
        return lines[0].lstrip("# ")


def generate_page(from_path, template_path, dest_path):
    print(
        f"* Generating page from {from_path} to {dest_path} using {template_path} *")

    with open(from_path, "r") as md:
        markdown = md.read()
        title = extract_title(markdown)

        with open(template_path, "r") as tmp:
            template = tmp.read()
            html = markdown_to_html_node(markdown).to_html()

            template = template.replace(
                "{{ Title }}", title).replace("{{ Content }}", html)
            with open(dest_path, "w") as output_file:
                output_file.write(template)


def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if path.isfile(dest_dir_path):
        raise FileExistsError("Cannot copy directory into single file")
    if not path.exists(dir_path_content):
        raise FileNotFoundError("Source directory doesn't exist")
    if not path.exists(dest_dir_path):
        makedirs(dest_dir_path)

    if path.isfile(dir_path_content):
        pass
        return

    sub_dir = listdir(dir_path_content)
    for fsnode in sub_dir:
        source_node_path = path.join(dir_path_content, fsnode)
        dest_node_path = path.join(
            dest_dir_path, fsnode.replace(".md", ".html"))
        if path.isfile(source_node_path) and source_node_path.endswith(".md"):
            generate_page(source_node_path, template_path, dest_node_path)
        elif path.isdir(source_node_path):
            generate_pages_recursive(
                source_node_path, template_path, dest_node_path)
