from os import path, listdir, makedirs
from shutil import copy, rmtree


def copy_files_recursive(source_dir_path, dest_dir_path):
    if path.isfile(dest_dir_path):
        raise FileExistsError("Cannot copy directory into single file")
    if not path.exists(source_dir_path):
        raise FileNotFoundError("Source directory doesn't exist")
    if path.exists(dest_dir_path):
        rmtree(dest_dir_path)
    makedirs(dest_dir_path)

    if path.isfile(source_dir_path):
        pass
        return

    sub_dir = listdir(source_dir_path)
    for fsnode in sub_dir:
        source_node_path = path.join(source_dir_path, fsnode)
        dest_node_path = path.join(dest_dir_path, fsnode)
        print(f" * {source_node_path} -> {dest_node_path}")
        if path.isfile(source_node_path):
            copy(source_node_path, dest_node_path)
        else:
            copy_files_recursive(source_node_path, dest_node_path)
