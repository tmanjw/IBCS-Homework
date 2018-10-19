#Basic Loop HW
import random
import time

#1.
# count=8
# while count>-3:
#     print(count)
#     count -= 1
# print(count)

# count=8
# for x in range(12):
#     print(count-x)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

#2.
# def is_odd(integer):
#     if integer/2!=int(integer/2):
#         return(False)
#     else:
#         return(True)
#
# for x in range(1,11):
#     print(is_odd(x))
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# #3.
# def dice_roll():
#     rolls=random.randint(1,6)
#     print("-=( You rolled",rolls,")=-")
#     return(rolls)
#
# rolledtimes=13
# one=0
# two=0
# three=0
# four=0
# five=0
# six=0
# for x in range(0,rolledtimes):
#     die=dice_roll()
#     if die==1:
#         one+=1
#     elif die==2:
#         two+=1
#     elif die==3:
#         three+=1
#     elif die==4:
#         four+=1
#     elif die==5:
#         five+=1
#     else:
#         six+=1
#
# print("-=( The results have been tallied )=-")
# print("One:",one,"\nTwo:",two,"\nThree:",three,"\nFour:",four,"\nFive:",five,"\nSix:",six)
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

#4.
odd=[]
even=[]
def function(variable):
    list=[int(x) for x in str(variable)]
    for x in range(0,len(list)):
        if list[x]/2!=int(list[x]/2):
            odd.append(list[x])
        else:
            even.append(list[x])
    print("-=( There are",len(even),"even digits )=-")
    print(even)
    print("-=( There are",len(odd),"odd digits )=-")
    print(odd)
function(13131313131313131313131313)