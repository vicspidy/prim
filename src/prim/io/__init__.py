import os
import glob
import re

def ls(path, pattern='*'):
    # files = glob.glob(os.path.join(path, pattern))
    result = list()
    pattern = re.compile(pattern)
    for file in os.listdir(path): 
        match = re.search(pattern, file)
        if match:
            result.append(os.path.join(path, match.group()))
    return result


if __name__ == "__main__":
    p = '/home/ashish/Documents/projects/prim_root'
    print ls(p, r'.+?\.y[a]?ml')