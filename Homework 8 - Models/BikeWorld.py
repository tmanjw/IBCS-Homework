import random

LocationA=[]
LocationB=[]
LocationC=[]
for i in range(1,15):
    if random.randint(1,2)%2==0:
        LocationA+=[str(i)]
    else:
        LocationB+=[str(i)]
print(LocationA)
print(LocationB)

ARent=3
BRent=4
ReturnRate=7
time=[]
first=True
for i in range(1,25):
    time+=[i]

    if ARent>len(LocationA):
        for j in range(0, len(LocationA)):
            var1 = LocationA.pop(0)
            LocationC.append(var1)
    else:
        for j in range(0,ARent):
            var1=LocationA.pop(0)
            LocationC.append(var1)

    if BRent > len(LocationB):
        for j in range(0, len(LocationB)):
            var1 = LocationB.pop(0)
            LocationC.append(var1)
    else:
        for j in range(0,BRent):
            var2=LocationB.pop(0)
            LocationC.append(var2)

    if first!=True:
        random.shuffle(LocationC)
        if ReturnRate > len(LocationC):
            for j in range(0,len(LocationC)):
                var3 = LocationC.pop(0)

                if random.randint(1, 2) % 2 == 0:
                    if len(LocationA) != 10:
                        LocationA.append(var3)
                    else:
                        LocationB.append(var3)

                else:
                    if len(LocationB) != 10:
                        LocationB.append(var3)
                    else:
                        LocationA.append(var3)

        else:
            for j in range(0,ReturnRate):
                var3=LocationC.pop(0)

                if random.randint(1,2)%2==0:
                    if len(LocationA)!=10:
                        LocationA.append(var3)
                    else:
                        LocationB.append(var3)

                else:
                    if len(LocationB)!=10:
                        LocationB.append(var3)
                    else:
                        LocationA.append(var3)
    first=False
    print()
    print(LocationA)
    print(LocationB)
    print(LocationC)
