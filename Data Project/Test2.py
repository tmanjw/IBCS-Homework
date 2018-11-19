dict={'test':[1,2,3,4,5,6,7,8,9,0]}

count=0
for i in dict:
    for j in range(len(dict[i])):
        count+=1
print(count)