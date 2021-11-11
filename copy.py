# This script copy files into obj dir, and rename

import os
import glob
import shutil

need_list = list()

# get text files with name
text_files = glob.glob('datasets/**/*.txt', recursive=True)
for t in text_files:
    t_basename = os.path.basename(t)
    # copy
    shutil.copyfile(t, "./obj/{}".format(t_basename))
    # push to need list
    need_name = os.path.splitext(os.path.basename(t))[0]
    need_list.append(need_name)

    print("{0} {1}".format(t ,t_basename))

# get picture files with name
picture_files = glob.glob('datasets/**/*.jpg', recursive=True)
for p in picture_files:
    p_basename = os.path.basename(p)
    need_name = os.path.splitext(os.path.basename(p))[0]
    # if it is needed?
    if not need_name in need_list:
        continue
    # copy
    shutil.copyfile(p, "./obj/{}".format(p_basename))

    print("{0} {1}".format(p ,p_basename))

    
