import os
import shutil

def copy_static(from_dir, to_dir):
    # copy_static("./static", "./public"))
    if not os.path.exists(from_dir):
        raise ValueError(f"the provided path does not exist")
    if not os.path.exists(to_dir):
        os.mkdir(to_dir)
    to_dir_contents = os.listdir(to_dir)
    if to_dir_contents != []:
        #delete contents of to_dir to ensure idempotence
        shutil.rmtree(to_dir)
        os.mkdir(to_dir)
    from_dir_contents = os.listdir(from_dir)
    logged_paths = []
    for item in from_dir_contents:
        path = os.path.join(from_dir, item)
        if os.path.isfile(path):
            logged_paths.append(path)
            shutil.copy(path, to_dir)
            return logged_paths
        else:
            logged_paths.extend(copy_static(path, to_dir))   
    return logged_paths