#Lists class work
import random

# #1.
# list1=["a","z","d","g"]
# var1=list1[0]
# list1[0]=list1[3]
# list1[3]=var1
# print(list1)
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#
# #2.
# list1=["a","z","d","g"]
# sliced=list1[1:3]
# newlist=[]
# newlist+=sliced+list1+sliced
# print(newlist)
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#
# #3.
# list1=["a","z","d","g"]
# evenlist=list1[::2]
# oddlist=list1[1::2]
# newlist=oddlist+evenlist
# print(newlist)
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#
# #4.
# list1=["a","z","d","g"]
# for x in range(0, len(list1)):
#     print(list1[x]*5)
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#
# #5.
# list1=[]
# while len(list1)<100:
#     x=random.randint(1,100)
#     if x%2==1 and x%7!=0:
#         list1+=[x]
# print(list1)
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#
# #6.
# list1=[]
# for x in range(0,50):
#     list2 = []
#     for y in range(0,x+1):
#         if y==0:
#             pass
#         elif x%y==0:
#             list2+=[y]
#     list1+=list2
# print(list1)
# print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
#
# #7.
# dict1={}
# for x in "abcde":
#     dict1[random.randint(0,10)]=x
# print(dict1)

#8.
dict1={}
letters="abcdefghijklmnopqrstuvwxyz"
for x in range(0,100):
    key=(random.choice(letters)+random.choice(letters)+random.choice(letters))
    dict1[key]=random.randint(1,131)

print(dict1)
print(100-len(dict1),'% are invalid keys')