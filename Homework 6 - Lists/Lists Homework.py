#Lists
import random

print('1.')
def func1(lst):
    if lst[0] == 6 or lst[-1] == 6:
        return True
    else:
        return False

list1=[1,2,3,6]
print(func1(list1))

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

print('2.')
def func2(lst):
    lst=lst[::-1]
    return lst

list2=[1,2,3]
print(func2(list2))
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

print('3.')
def func3(lst):
    newlst=[lst[0],lst[-1]]
    return newlst

list3=[1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,13,3,1,3,1,3,1,3]
print(func3(list3))
#Where is the 13? >:3
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

print('4.')
def func4(lst):
    var=False
    for i in lst:
        if i==2 or i==3:
            var=True
    return var

list4=[1,2,3,4,5,6,7,8,9,0]
print(func4(list4))
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

print('5.')
def func5(lst):
    count=0
    for i in lst:
        if i%2==0:
            count+=1
    return count

list5=[1,2,3,4,5,6]
print(func5(list5))
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

print('6.')
def func6(lst):
    total=0
    if lst==[]:
        return 0
    else:
        for i in range(0,len(lst)):
            if lst[i] != 13 and lst[i-1]!=13:
                total+=lst[i]
        return(total)

list6=[1,2,13,3,4]
print(func6(list6))
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

print('7.')
def func7(lst):
    total=0
    for i in sorted(lst[1:-1]):
        total+=i
    mean=total/(len(lst)-2)
    return mean

list7=[1,2,3,4,100]
print(func7(list7))
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

print('8.')
def func8(lst):
    if lst==lst[::-1]:
        return True
    else:
        return False

list8=[1,2,3,2,1]
print(func8(list8))
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

print('9.')
# def func9(lst):
#     newlst=[]
#     repeat=False
#     for j in lst:
#         if repeat==False:
#             newlst+=[j]
#             print(j)
#             for k in lst:
#                 lst.remove(k)
#             repeat=False
#         else:
#             pass
#     return newlst

def func9(lst):
    newlist=[]
    for i in lst:
        newlist+=[i.lower()]
    return set(newlist)

list9=["ok","oK","Ok",'hello','Hello']
print(func9(list9))
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

print('10.')
def func10():
    global coordinates
    lst=[]
    for i in range(100):
        var1=random.randint(-100,100)
        var2=random.randint(-100,100)
        var3=random.randint(-100,100)
        lst+=[(var1,var2,var3)]
    return lst

def func11(lst):
    if len(lst)-len(set(lst))>=1:
        return 0

    else:
        newlst=[]
        for i in range(len(lst)):
            for j in range(len(lst)):
                distance=(((lst[i][0])-(lst[j][0]))**2 + ((lst[i][1])-(lst[j][1]))**2 + ((lst[i][2])-(lst[j][2]))**2)**0.5
                if distance!=0:
                    newlst+=[distance]

        return sorted(newlst)[0]


list10=func10()
print('%.2f' % func11(list10))
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

print('11.')
def func12(lst):
    newlist=[]
    for i in lst:
        count=0
        for j in lst:
            if abs(j-i)>20:
                count+=1
        if count==len(lst)-1:
            newlist+=[i]
    return newlist

list11=[]
for i in range(100):
    list11+=[random.randint(0,1000)]

print(list11)
print(func12(list11))