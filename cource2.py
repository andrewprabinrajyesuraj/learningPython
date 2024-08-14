# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 14:17:57 2024

@author: araj2

"""
import random

# Generate a list of numbers between 1 and 1000 that are divisible by 35
valid_numbers = [num for num in range(35, 1001, 35)]

# Randomly select 5 numbers from the list
random_numbers = random.sample(valid_numbers, 5)

print(random_numbers)


# n=int(input("enter the number: "))
# total=0
# for i in range(1,n+1):
#     total=total+(i/(i+1))
# print(total)


# b=[12,24,35,70,88,120,155]
# a=[i for i in b if not (i % 5 == 0 and 1 % 7 == 0)]
# print(a)

# b=[12,24,35,70,88,120,155]
# a=[i for i in b if (i % 5 != 0 and 1 % 7 != 0)]
# print(a)

# a=[12,24,35,70,88,120,155]
# count=-1
# b=[]
# for i in a:
#     count=count+1
#     if (count not in {0,4,5}):
#         b.append(i)
# print(b)

# a=[12,24,35,24,88,120,155]
# arr=[i for i in a if i != 24]
# print(arr)

# b=[]
# a=[12,24,35,24,88,120,155,88,120,155]
# for i in a:
#     if i not in b:
#         b.append(i)

# print(b[::-1])
#for i in a:
    

# a=[1,3,6,78,35,55]
# b=[12,24,35,24,88,120,155]
# intersection=set(a) & set(b)
# print(intersection)

# a=input("enter the input->> ")
# for i in set(a):
#    print("count of "+str(i)+" is "+str(a.count(i)))

# a=input("enter the input->> ")
# print(a[::-1])

# a=input("enter the input->> ")
# out=""
# for i in a:
#     if(a.index(i)%2 == 0):
#         out=out+i
# print(out)
# a = [4,7,3,2,5,9]
# for i in a:
#     print("positing of" +str(i)+ "-->" +str(a.index(i)+1))


# def hi(value):
#   return ("Hi Function-"+value)

# #hi("cool")
# print("callingFun----"+hi("coooll"))

# class mat:
    
#     def __init__(self,a,b):
#         self.name=a
#         self.addr=b
        
#     def add(self):
#         print(int(self.name)+int(self.addr))
  
# b=[mat("1","1"),mat("2","2"),mat("3","3")]
# print("length--"+str(len(b)))
# b[2].name=20
# print(str(b[2].add())+"----")

# p=mat("1","1");
# q=mat("2","2");
# q.add()
# #print(q.addr)
# p.name="50"
# # p.add()
# import os
# # file = open('temp.txt','w')
# # file.write('hellow world123')
# # file.close()

# # file = open('temp.txt','r')
# # print(file.read(5))
# # file.close()

# # os.rename('temp.txt','temp2.txt')
# # file.close()

# # file = open('temp2.txt','r')
# # print(file.read())
# # file.close()

# os.remove('temp2.txt')

#a=(1,2,3)
# b=[]
# print(type(a))

# for i in a:
#     print(i)
# print(len(a))

# if(2 in a):
#     print("True")
    
# print(a[0:2])


# d=[1,2,3,4]
# d.pop(2)
# print(d)


# d = {"john":40, "peter":45}
# print(list(d.keys()))

# username=input("Enter the username: ")
# password=input("Enter the password")

# print(sum(1 for i in password if i.isdigit()))

# if((len(password) >= 6) and (len(password) <= 12) and (sum(1 for i in password if i.isdigit()) >= 1) and (sum(1 for i in password if i.islower()) >= 1) and ((sum(1 for i in password if i.isupper())) >= 1) and (sum(1 for i in password if i in {'$','#','@'}) >= 1)):
#         print("valid password")
# else:
#         print("in correct")
        




