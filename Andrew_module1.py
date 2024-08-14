# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#4. Write a program that accepts a sentence and calculate the number of letters and digits.


string=input("enter the input value here:  ")
print(string)
alphacount=0
numbercount=0
for i in string:
    if(i.isalpha()):
        alphacount=alphacount+1
    elif(i.isalnum()):
        numbercount=numbercount+1
    else:
        continue

print("LETTERS--" +str(alphacount))
print("DIGITS--" +str(numbercount))

#5. Design a code which will find the given number is Palindrome number or not.

palin=input("enter the input value here:  ")
iteration=len(palin)//2
flag="T"
first=0
last=len(palin)-1
while(iteration >= 0):
    if(palin[first]==palin[last]):
        first=first+1
        last=last-1
        iteration=iteration-1
        continue
    else:
        flag="F"
        break
    
if(flag=="F"):
  print("NOT a Palindrome")
else:
  print("palindrome")

# 2. Write a code which accepts a sequence of words as input and prints the words in a sequence after sorting them alphabetically. 

input_string = input("Enter a sequence of words: ")
words = input_string.split()
sorted_words = sorted(words)
print(sorted_words)
print("Sorted words: ", " ".join(sorted_words))

    