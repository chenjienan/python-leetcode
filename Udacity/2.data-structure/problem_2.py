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
    if not path: raise Exception("path cannot be empty.")
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

import pprint

print("===Test case 1===")
files = find_files(".h", r'testdir')
pprint.pprint(files)

# return
# ['c:\\projects\\python-leetcode\\Udacity\\2.data-structure\\testdir\\subdir1\\a.h',
#  'c:\\projects\\python-leetcode\\Udacity\\2.data-structure\\testdir\\subdir3\\subsubdir1\\b.h',
#  'c:\\projects\\python-leetcode\\Udacity\\2.data-structure\\testdir\\subdir5\\a.h',
#  'c:\\projects\\python-leetcode\\Udacity\\2.data-structure\\testdir\\t1.h']

print("===Test case 2===")
files = find_files(".c", '.')
pprint.pprint(files)

# return
# ['c:\\projects\\python-leetcode\\Udacity\\2.data-structure\\.\\testdir\\subdir1\\a.c',
#  'c:\\projects\\python-leetcode\\Udacity\\2.data-structure\\.\\testdir\\subdir3\\subsubdir1\\b.c',
#  'c:\\projects\\python-leetcode\\Udacity\\2.data-structure\\.\\testdir\\subdir5\\a.c',
#  'c:\\projects\\python-leetcode\\Udacity\\2.data-structure\\.\\testdir\\t1.c']

print("===Test case 3===")
files = find_files(".abc", '.')
pprint.pprint(files)

# return 
# []

print("===Test case 4===")
files = find_files('', 'testdir')
pprint.pprint(files)

# return 
# ['c:\\projects\\python-leetcode\\Udacity\\2.data-structure\\testdir\\subdir1\\a.c',
#  'c:\\projects\\python-leetcode\\Udacity\\2.data-structure\\testdir\\subdir1\\a.h',
#  'c:\\projects\\python-leetcode\\Udacity\\2.data-structure\\testdir\\subdir2\\.gitkeep',
#  'c:\\projects\\python-leetcode\\Udacity\\2.data-structure\\testdir\\subdir3\\subsubdir1\\b.c',
#  'c:\\projects\\python-leetcode\\Udacity\\2.data-structure\\testdir\\subdir3\\subsubdir1\\b.h',
#  'c:\\projects\\python-leetcode\\Udacity\\2.data-structure\\testdir\\subdir4\\.gitkeep',
#  'c:\\projects\\python-leetcode\\Udacity\\2.data-structure\\testdir\\subdir5\\a.c',
#  'c:\\projects\\python-leetcode\\Udacity\\2.data-structure\\testdir\\subdir5\\a.h',
#  'c:\\projects\\python-leetcode\\Udacity\\2.data-structure\\testdir\\t1.c',
#  'c:\\projects\\python-leetcode\\Udacity\\2.data-structure\\testdir\\t1.h']

print("===Test case 5===")
files = find_files(".c", '')
pprint.pprint(files)

# return
# exception: path cannot be empty