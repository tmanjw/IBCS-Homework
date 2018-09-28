#Quadratic Formulas

import time
import math

print("The quadratic formula is ax^2+bx+c")
time.sleep(1)
print("Please input the variables a, b, and c in following order.")
time.sleep(0.5)
input("[ Press Enter to Continue ] : ")
a=int(input("[ Input value 'a' ] :"))
b=int(input("[ Input value 'b' ] :"))
c=int(input("[ Input value 'c' ] :"))

if b**2-4*a*c < 0:
    print("There is no solution for these set of values.")

elif b**2-4*a*c == 0:
    print("The values given create a perfect square, therefore we can use the perfect square formula")
    time.sleep(1)
    print("x=((a^1/2)x+(c^1/2))^1/2 or ((a^1/2)x-(c^1/2)^1/2")
    time.sleep(2)
    print("Now we get rid of the brackets and have it equal to 0.")
    time.sleep(1)
    print("If it is a fraction, make sure to simplify.")

    if b>0:
        print("x=("+str(math.sqrt(a))+"x+"+str(math.sqrt(c))+")^2")
        print("x="+str((c*-1)/a))

    elif b<0:
        print("x=("+str(math.sqrt(a))+"x-"+str(math.sqrt(c))+")^2")
        print("x="+str(c/a))

elif b**2-4*a*c > 0:
    print("The values given are not a perfect square therefore we can use the equation to solve.")
    time.sleep(1.5)
    print("x=(-b+-(b^2-4(a)(c))^1/2)/2a")
    time.sleep(1)
    print("There will be two answers to these set of variables")
    ans1=((b*-1)+math.sqrt(b**2-4*a*c))/(2*a)
    ans2=((b*-1)-math.sqrt(b**2-4*a*c))/(2*a)
    time.sleep(0.5)
    print("x="+str(ans1), "or x="+str(ans2))