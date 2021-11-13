# This script add name into train.txt
import os
import glob
import random

basename = "/content/yolotinyv3_medmask_demo/obj/{}\n"
count = 0

# get picture files with name
picture_files = glob.glob('obj/*.jpg', recursive=True)
with open("./train.txt", mode='w') as f:
    for p in picture_files:    
        p_basename = os.path.basename(p)
        
        f.write(basename.format(p_basename))
        print(p)

        count += 1

# add testing data
# get picture files with name
picture_files = glob.glob('obj/*.jpg', recursive=True)
with open("./test.txt", mode='w') as f:
    for p in picture_files:
        if not 1 == random.randrange(10):
            continue
        p_basename = os.path.basename(p)
        f.write(basename.format(p_basename))
        print(p)
print(count)

    
