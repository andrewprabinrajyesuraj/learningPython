# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 14:34:27 2024

@author: araj2
"""

def position(x,y):
    #seat=arr[x][y]
  # print (f"<<--MAIN--->>x is -- {x} y is -- {y} | row is - {row} col is - {col}")
    if (x == 0 and y == 0):
        if(arr[x][y+1] == 0) and (arr[x+1][y] == 0) and (arr[x+1][y+1] == 0) :
            return "true"
        else:
            return "false" 
        
    elif (x != 0 and y != 0 and x < row - 1 and y < col - 1):
        if(arr[x][y+1] == 0) and (arr[x+1][y] == 0) and (arr[x+1][y+1] == 0) and (arr[x][y-1] == 0) and (arr[x-1][y] == 0) and (arr[x-1][y-1] == 0) :
            return "true"
        else:
            return "false" 
        
    elif (x == 0 and y != 0 and x < row - 1 and y < col - 1):
        if(arr[x][y+1] == 0) and (arr[x+1][y] == 0) and (arr[x+1][y+1] == 0) and (arr[x][y-1] == 0) :
            return "true"
        else:
            return "false" 
        
    elif (x != 0 and y == 0 and x < row - 1 and y < col - 1):
        if(arr[x][y+1] == 0) and (arr[x+1][y] == 0) and (arr[x+1][y+1] == 0) and (arr[x-1][y] == 0) :
            return "true"
        else:
            return "false" 
        
    elif (x != 0 and y != 0 and x == row - 1 and y < col - 1):
        if(arr[x][y+1] == 0) and (arr[x][y-1] == 0) and (arr[x-1][y] == 0) and (arr[x-1][y-1] == 0) :
            return "true"
        else:
            return "false" 
        
    elif (x != 0 and y != 0 and x < row - 1 and y == col - 1):
        if (arr[x+1][y] == 0) and (arr[x][y-1] == 0) and (arr[x-1][y] == 0) and (arr[x-1][y-1] == 0) :
            return "true"
        else:
            return "false" 
   
    
    elif (x != 0 and y != 0 and x == row - 1 and y == col - 1):
        if (arr[x][y-1] == 0) and (arr[x-1][y] == 0) and (arr[x-1][y-1] == 0) :
            return "true"
        else:
            return "false" 

row = int(input("enter the row size-- "))
col = int(input("enter the column size-- "))
if (row > 0 and col > 0):
    print ("valid")
    arr = [[0 for _ in range(col)] for _ in range(row)]
    # for line in arr:
    #     print(line)
else:
    print ("invalid input")



for row1 in range(int(len(arr))):
   for col1 in range(int(len(arr[row1]))):
       if(position(row1,col1) == "true"):
           arr[row1][col1]=9

for line in arr:
   print(line)
#print(position(3,0))
