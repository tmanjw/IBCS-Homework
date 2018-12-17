lst1=[1,-3,5,7,15,-4,0,-6,-10,-11,12]

odd=0
for i in lst1:
    if abs(i)%2!=0:
        odd+=1

run=True
while run==True:
    check=0
    for i in range(odd):
        if abs(lst1[i])%2==1:
            check+=1
    if check==odd:
        run=False

    for i in range(len(lst1)):
        if lst1[i] % 2 == 1 and lst1[i-1]%2==0:
            var1=lst1[i]
            lst1[i]=lst1[i-1]
            lst1[i-1]=var1


print(lst1)
