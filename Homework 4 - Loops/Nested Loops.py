#Nested Loops
import math
import pygame

#1.
for x in range(0,5):
    print()
    for x in range(0,10):
        print("*",end="")

print()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#2.
for x in range (0,5):
    print(" "*(4-x),end="*")
    for y in range(0,2):
       print("*"*((1+x)-1),end="")
    print()
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
# print()
#
# #3.
# length=7
# for x in range(0,length):
#     # print (x)
#     if x ==0 or x == length-1:
#         print("*" * length)
#     elif x==int(length-1)/2:
#         print("*"+"-"*math.floor(length/2-1)+"*"+"-"*math.floor(length/2-1)+"*")
#     elif x <= int(length - 1) / 2:
#
#     # elif x == int(length - 1) / 2:
#
#     else:
#         print("*" + "-"*(length-2) + "*")

#3.
def xbox(length):
    for x in range(0,length):
        for y in range(0,length):
            if x==0 or x==length-1:
                print("*",end="")
            elif x==y:
                print("*",end="")
            elif y+1==length-x:
                print("*",end="")
            elif y==0 or y==length-1:
                print("*",end="")
            elif x!=0 and x!=length-1:
                print(" ",end="")
        print()

xbox(13)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")