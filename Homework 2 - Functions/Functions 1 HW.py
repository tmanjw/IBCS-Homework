# Functionnnnnn Homeworkkk!!! EY EY OOOOOOOOOHHHH!!! why ;-;
import math
import time

#1.
'''
def mixeddiv(a,b):
    part=a//b
    if part==0:
        part=""
    mod=a%b
    if mod==0:
        print("You get ah",part)
    else:
        print("You get ah da",part,',',mod,"/",num2)

num1 = int(input("[Input da numbah]:"))
num2 = int(input("[Input anadah numbah]:"))

mixeddiv(num1,num2)

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


#2.

def vowelcount(a):
    print(a.lower().count("a")+(a.lower().count("i"))+(a.lower().count("u"))+(a.lower().count("o"))+(a.lower().count("e")))

var1=aieouaeooiuaeoiaoieuoaieuoaiueoiaueoiaueoiaueoaieuoaieuoaieuaoeiuaoeiuaoieuaoieuaoiueoiae

vowelcount(var1)


print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#3.
def vowelcount(a):
    print("[ A's ]", a.lower().count("a"))
    print("[ I's ]", a.lower().count("i"))
    print("[ U's ]", a.lower().count("u"))
    print("[ E's ]", a.lower().count("e"))
    print("[ O's ]", a.lower().count("o"))

vowelcount("aeuaiouoaieuoaieuoaiueoiaueaoieuaoeaiuoiuioaeuaoeiuaoieuaieueaiauaieuaoeiuaoeiuaoeaooaoaieuaoie")

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#4.

def vowelcount(a):
    print("[ A's ]:", int(a.lower().count("a")/5))
    print("[ I's ]:", int(a.lower().count("i")/5))
    print("[ U's ]:", int(a.lower().count("u")/5))
    print("[ E's ]:", int(a.lower().count("e")/5))
    print("[ O's ]:", int(a.lower().count("o")/5))

vowelcount("aeuaiouoaieuoaieuoaiueoiaueaoieuaoeaiuoiuioaeuaoeiuaoieuaieueaiauaieuaoeiuaoeiuaoeaooaoaieuaoie")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#5.

def volsphere(r):
    volume=4/3*r*math.pi**3
    return(volume)

def sasphere(r):
    sa=4*r*math.pi**2
    return(sa)

# radius=13
# print(volsphere(radius))
# print(sasphere(radius))

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#6.
def sphformula():
    print("-=( Choose a Sphere formula you would like to use )=-")
    time.sleep(0.5)
    print("{A} : Volume of Sphere = 4/3 x Pi x Radius^3")
    time.sleep(0.5)
    print("{B} : Surface Area of Sphere = 4 x Pi * Radius^2")
    time.sleep(0.5)
    formulachosen=input("[Enter \"A\" or \"B\"]:")
    while formulachosen != "A" and formulachosen != "B":
        print('-=( Choices can only be "A" or "B" )=-')
        formulachosen=input('[Enter "A" or "B"]:')
    print()
    radius=int(input("[Input a radius]:"))
    if formulachosen == "A":
        answer=volsphere(radius)
        print("-=( The volume with radius", radius, "is", round(answer,2),   ")=-")
    elif formulachosen=="B":
        answer=sasphere(radius)
        print("-=( The surface area with radius",radius,"is",round(answer,2),")=-")

sphformula()

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

#7
def function(name="Purplay",age=13135,weight=13131313131313131313131313):
    print("YOU KNEEL BEFORE THE KING OF",name.upper(),"\nTHE RULER OF COLOURS FOR",age,"YEARS\nKNOW THAT IF YOU CHALLENGE ME, YOU CHALLENGE THE MIGHT OF",weight,"MEN!!!")
    print()

function()
function(name='quoi')
function(age=17,weight=72)
function(name='orange',age=-1234567890,weight=-9876543210)
#Can be called with a variety of combinations due to parameters having a set value already, either 3 values, 2 values, 1 value, or none as shown above
#Does not need to be defined, can put in 

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
'''
#8
def rgbtohex(red=127,green=0,blue=255):
    rgb=[red,green,blue]
    colours=["R:","G:","B:"]
    printout=""
    for x in range(0,3):
        printout+=colours[x]
        printout+=str(hex(rgb[x]))[2:].upper()
        printout+=" "
    print(printout)

def hextorgb(red="7F",green="0",blue="FF"):
    rgb = [red, green, blue]
    colours = ["R:", "G:", "B:"]
    printout=""
    for x in range(0,3):
        printout+=colours[x]
        printout+=str(int(rgb[x],16))
        printout+=" "
    print(printout)

rgbtohex()
hextorgb()