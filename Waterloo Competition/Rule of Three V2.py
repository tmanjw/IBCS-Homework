# rules=[["AA","AB"],['AB','BB'],['B',"AA"]]
rules=[]
for i in range(3):
    line=input().split(" ")
    rules.append([line[0],line[1]])
line=input().split(" ")
steps=int(line[0])
str1=line[1]
final=line[2]


counter=0
while counter!=steps:
    i = 0
    stringlist = []
    while i!=len(str1):
        # print('Index :',i)
        if rules[0][0] in str1[i:i+len(rules[0][0])]:
            # print(i,str1[i:i + len(rules[0][0])],"1")
            stringlist+=[rules[0][1]]
            i+=len(rules[0][0])
            counter+=1

            tempstring=''
            for k in stringlist:
                tempstring+=k
                tempstring+=str1[i:]
            print(1, int(i)+1, tempstring)

            if counter==steps:
                stringlist += str1[i:]
                break

        elif rules[1][0] in str1[i:i+len(rules[1][0])]:
            # print(i,str1[i:i + len(rules[1][0])],"2")
            stringlist += [rules[1][1]]
            i += len(rules[1][0])
            counter+=1

            tempstring=''
            for k in stringlist:
                tempstring+=k
                tempstring+=str1[i:]
            print(2, int(i)+1, tempstring)

            if counter==steps:
                stringlist+=str1[i:]
                break

        elif rules[2][0] in str1[i:i+len(rules[2][0])]:
            # print(i, str1[i:i + len(rules[2][0])], "3")
            stringlist += [rules[2][1]]
            i += len(rules[2][0])

            tempstring=''
            for k in stringlist:
                tempstring+=k
                tempstring+=str1[i:]
            print(3, int(i)+1, tempstring)

            counter+=1
            if counter==steps:
                stringlist += str1[i:]
                break
        else:
            stringlist += str1[i]
            i+=1

    newstring = ''
    for i in stringlist:
        newstring+=i
    str1=newstring