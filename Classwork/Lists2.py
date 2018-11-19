#Warmup Lists 2

#1.
list1=[1,2,3,4,1,3,4,5,1,5,6,7,1,2,6,9]
first=13131313131313131313131313
second=13131313131313131313131313

# for i in list1:
#     if i<first:
#         second=first
#         first=i
#     elif i==first:
#         pass
#     elif i<second:
#         second=i
# print(first,second)
print(sorted(list1[:2]))
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#2.
list2=[1,2,3,4,5,6,7,8,9]
for i in list2:
    if i%2==1:
        list2.remove(i)
print(list2)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#3.
list3=[1,2,3,4,"one","two","three","four"]
list4=[]
list5=[]
for i in list3:
    try:
        i%i==0
        list4+=[i]
    except:
        list5+=[i]
print(list4,list5)