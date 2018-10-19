#Perfect numeber finder
def func(num):
    total=0
    for x in range(1,num):
        if num%x==0:
            total+=x
    if total==num:
        return num
    else:
        return 0


count=0
num=1
while count<10:
    number=(func(num))
    if number>0:
        print(number)
        count+=1
        num+=1
    else:
        num+=1