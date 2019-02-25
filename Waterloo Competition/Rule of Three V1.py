rules=[['AAA','AB'],['AB','BB'],['B','AA']]
# line=input().split(' ')
# data.append(int(line[0]),line[1],line[2])


str1="ABABABAAA"
stringlist=[]
for i in str1:
    stringlist+=[i]
print(stringlist)
for i in range(len(stringlist)):
    for j in range(0,3):
        print("Rule",j+1)
        tempstring=''
        if i+len(rules[j][0])-1!=len(stringlist):
            for k in range(len(rules[j][0])):
                tempstring+=stringlist[i+k]
            print(tempstring)
        else:
            break

# for i in str1:
#     stringlist+=[i]
#
# print(stringlist)


