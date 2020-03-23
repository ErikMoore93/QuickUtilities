"""
Program             : Header
Author              : Erik Moore
Date Created        : 03/19/2020
Purpose             : corrects named group textfiles to have the correct zero padding

"""

#Imports Here

import os
import glob
cur = os.getcwd()
for readfile in glob.glob(os.path.join(cur,'*.txt')):
    print(readfile)
    filename = os.path.basename(readfile)
    startname = filename
    while(len(str(filename)) < 7):
        print("too short")
        filename = "0"+filename
        print(filename)
        
    os.rename(readfile, readfile.replace(startname, filename))
    
    
input()