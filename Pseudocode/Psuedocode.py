# Pseudocode

print('Question 1.')
binary = []
var1=15
while var1>1:
    var2=var1%2
    binary+=[var2]
    var1=(var1-var2)/2
    var1=int(var1)

eightbit=[]
for i in range(8-len(binary)):
    eightbit+=[0]

for i in binary:
    eightbit+=[i]
print(eightbit)

'''
Web Pseudocode Version
Var1=15

Binary=[]
Count=0
loop while Var1>1
    Var2=Var1%2
    Var1=(Var1-Var2)/2
    Binary[Count]=Var2
    Count=Count+1
end loop

Eightbit=[]
loop I from 0 to 8-Count-1
    Eightbit[I]=0
end loop

loop J from 0 to Count-1
    Eightbit[J+(8-Count)]=Binary[J]
end loop

output Eightbit
 
'''

print('Question 2.')
var1=13
while var1!=1:
    if var1%2==0:
        var1=var1/2
    else:
        var1=(var1*3)+1
    print(var1)
'''
Var1=8
Numbers=new Collection
Numbers.addItem(Var1)
loop while Var1!=1
    if Var1%2==0 then
        Var1=Var1/2
    end if
    if Var1%2==1 then
        Var1=(Var1*3)+1
    end if
    Numbers.addItem(Var1)
end loop
loop while Numbers.hasNext()
    Number = Numbers.getNext()
    output Number
end loop
'''
print('Question 3.')
