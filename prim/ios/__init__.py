import sys
import os
import glob
import re
from pprint import pprint as pp


def ls(path, dir_only=False, file_only=False, glob_pattern=None, regex=None):
    if dir_only and file_only:
        print('Error: "dir_only" and "file_only" parameters are mutually exclusive. Please use one at a time!')
        return
    if glob_pattern and regex:
        print('Error: "glob_pattern" and "regex" parameters are mutually exclusive. Please use one at a time!')
        return

    contents = list()
    if glob_pattern:
        contents = glob.glob(os.path.join(path, glob_pattern))
        contents = [os.path.basename(each) for each in contents]
    else:
        contents = os.listdir(path)

    if dir_only:
        contents = [each for each in contents if os.path.isdir(os.path.join(path, each))]
    elif file_only:
        contents = [each for each in contents if os.path.isfile(os.path.join(path, each))]
    
    if regex:
        re_filter = re.compile(regex)
        for each in reversed(contents):
            match = re_filter.search(each)
            if not match:
                # result.append(os.path.join(path, match.group()))
                contents.remove(each)
    
    return contents


if __name__ == "__main__":
    files = ls('D:\downloads', file_only=True, regex=r'.*?\d+\.\d+')
    pp(files)
    print(len(files))