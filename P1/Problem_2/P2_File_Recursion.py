import os

def find_files(suffix, path):
    if(not isinstance(suffix, str) or suffix is None) or (not isinstance(path, str) or path is None):
      return "The suffix or path entered is either null or empty, enter a valid format"

    files_found = list()
    return traverse_files(files_found, suffix, "./P2_subdirs")

def traverse_files(list, suffix, path):
  dirs = os.listdir(path)
  for itemName in dirs:
    if os.path.isfile(os.path.join(path, itemName)):
      # if the current item is a file
      # check if the length is bigger than the length of suffix
      if len(itemName) > len(suffix):
        file_suffix = itemName[-len(suffix):]
        if file_suffix == suffix:
          # if file_suffix is the one we want, append it to list 
          list.append(os.path.join(path, itemName))
    elif os.path.isdir(os.path.join(path, itemName)):
      # if itenName is a dir name, traverse the directory
      traverse_files(list, suffix, os.path.join(path, itemName))
  return list


print(find_files(".c", "./P2_subdirs"))

# Additional test cases

print(find_files(None, "./P2_subdirs/subdir2"))
# returns "The suffix or path entered is either null or empty, enter a valid format"
print(find_files(".h", "./P2_subdirs"))
# returns ['./P2_subdirs/subdir3/subsubdir1/b.h', './P2_subdirs/subdir5/a.h', './P2_subdirs/t1.h', './P2_subdirs/subdir1/a.h']
print(find_files("", ""))
# return empty list