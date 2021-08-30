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
    files_found = list()
    

    return traverse_files(files_found, "./P2_subdirs")

def traverse_files(list, path):
  dirs = os.listdir(path)
  for el in dirs:
    if os.path.isfile(os.path.join(path, el)):
      last_chars = el[-2:]
      if last_chars == ".c":
        list.append(os.path.join(path, el))
    elif os.path.isdir(os.path.join(path, el)):
      traverse_files(list, os.path.join(path, el))
  return list


print(find_files(".c", "./P2_subdirs"))