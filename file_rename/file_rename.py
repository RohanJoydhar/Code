import os
import re
import time
from turtle import delay
from tqdm import tqdm
#creating counter for file rename 
def ctr_creater(ctr):
    if (10 > ctr >= 0):
        ctr = '000' + str(ctr)
    elif (100 > ctr >= 10):
        ctr = '00' + str(ctr)
    elif (1000 > ctr >= 100):
        ctr = '0' + str(ctr)
    else:
        ctr = str(ctr)
    return ctr



def rename():
    path = "/Users/rohan/Code/File rename/files"
    os.chdir(path)
    prefix = input("Enter the prefix you want to add to the file names: ") + '_'
    ctr = int(input("Enter the counter you want to start from: "))
    s = []
    list = os.listdir(path)
    q = len(list)
    #only for macOS, mac store files randomly
    list.sort()


    for file in tqdm(list):
        suffix = file.split('.')[1]
        # ".DS_Store" files are the files who store file sorting details and other positions of a file in a directry
        #the code will work for mac and windows properly
        if (suffix != "DS_Store"):
            s.append(suffix)
            mid_ctr = ctr_creater(ctr)
            new_name = prefix + mid_ctr + '.' + suffix
            os.rename(file, new_name)
            ctr += 1
            time.sleep(0.05)    
        

def main():
    print("This program will rename all the files in the directory: /Users/rohan/Code/File rename/files")
    input("Press enter to continue...")
    print("This program will rename all the files in the folder.")
    rename()
    print("Done!")
if __name__ == '__main__':
    main()
