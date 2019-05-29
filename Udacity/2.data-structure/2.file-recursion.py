import os

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    
    base_dir = os.path.dirname(os.path.abspath(__file__))    
    target_dir = os.path.join(base_dir, path)
    
    files = []
    items = os.listdir(target_dir)
    for item_name in items:
        item_path = os.path.join(target_dir, item_name)
        if os.path.isfile(item_path) and item_path.endswith(suffix):            
            files.append(item_path)            
        
        elif os.path.isdir(item_path):
            for item in find_files(suffix, item_path):
                files.append(item)

    return files


# files = find_files(".h", r'testdir')

# import pprint
# pprint.pprint(files)