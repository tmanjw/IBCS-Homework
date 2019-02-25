apples=[]
bananas=[]
for i in range(6):
    if i<3:
        apples.append(int(input()))
    else:
        bananas.append(int(input()))

applescore=0
bananascore=0
for i in range(3):
    applescore += (3 - i) * apples[i]
for i in range(3):
    bananascore += (3 - i) * bananas[i]

if applescore>bananascore:
    print("A")
elif bananascore>applescore:
    print("B")
else:
    print("T")