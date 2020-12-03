#!/bin/python3.8 

# Author: Carl-Be
# Name  : excludeHidden.py  

import sys 

data = sys.stdin.read()
line = ""
dotIndex = 0

for i in range(len(data)):
    
    line += data[i]
    

    if(data[i] == "\n"):
        
        if(dotIndex == 0):
            print(line, end="")
        
        line = ""
        dotIndex = 0

    elif(data[i].find(":") != -1 and data[i + 4] == "."):
        dotIndex = i + 4
        

