#Logic Gates Question

def AND(a,b):
    if a==1 and b==1:
        return 1
    else:
        return 0

def NAND(a,b):
    if a==1 and b==0:
        return 0
    else:
        return 1

def OR(a,b):
    if a==0 and b==0:
        return 0
    else:
        return 1

print("a","|","b","|","c","|","p","|","q","|","x")
for a in (0,1):
    for b in (0,1):
        for c in (0,1):
            p=AND(a,b)
            q=NAND(a,c)
            x=OR(p,q)
            print(a,"|",b,"|",c,"|",p,"|",q,"|",x)
