import os
import shutil

def copy_static(src_dir="./static", dest_dir="./public"):
    if not os.path.exists(src_dir):
        raise ValueError(f"the provided path does not exist")
    if not os.path.exists(dest_dir):
        os.mkdir(dest_dir)
    dest_dir_contents = os.listdir(dest_dir)
    if dest_dir_contents != []:
        #delete contents of dest_dir to ensure idempotence
        shutil.rmtree(dest_dir)
        os.mkdir(dest_dir)
    src_dir_contents = os.listdir(src_dir)
    logged_paths = []
    for item in src_dir_contents:
        src_path = os.path.join(src_dir, item)
        dest_path = os.path.join(dest_dir, item)
        if os.path.isfile(src_path):
            shutil.copy(src_path, dest_dir)
            logged_paths.append(dest_path)
            return logged_paths
        else:
            logged_paths.extend(copy_static(src_path, dest_path))   
    return logged_paths
