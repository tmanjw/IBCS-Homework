#Conditional Statement HW
import math
import random

#1.
age=12
if age<18:
    print(False)
else:
    print(True)

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

#2.
sidea=4
sideb=5
sidec=8
istriangle=True

if sidea+sideb<sidec or sidea+sidec<sideb or sideb+sidec<sidea:
    istriangle=False

sidea*=sidea
sideb*=sideb
sidec*=sidec

if sidea+sideb==sidec and istriangle==True:
    print("Right Angle Triangle")
elif sidea+sideb>sidec and istriangle==True:
    print("Acute Triangle")
elif sidea+sideb<sidec and istriangle==True:
    print("Obtuse Triangle")
else:
    print("Not a Triangle")

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

#3.
number=1313
answer=""

if number%3==0:
    answer+="FIZZ "
if number%5==0:
    answer+="BUZZ"
if number%3!=0 and number%5!=0:
    answer+="Huh?"

print(answer)

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# #4.
# n=131313
# r=1
# def combination(n,r):
#     answer=(math.factorial(n))/(math.factorial(r)*math.factorial(n-r))
#     return answer
#
# output=combination(n,r)
#
# if output>1000000:
#     print("You have no chance")
# elif output>10000 and output<1000000:
#     print("Keep it up")
# else:
#     print("Possible")

# print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

# #5.
# print(random.random())
# print(random.randint(-10,10))
#
# print()
# from Negative8Ball import prediction
# prediction()

# print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')

#6.
def dicegame(guess1=1,guess2=2,guess3=3):
    die1=random.randint(1,3)
    die2=random.randint(1,3)
    die3=random.randint(1,3)
    guesses = [guess1, guess2, guess3]
    dicerolls=[die1,die2,die3]
    total=0
    for x in range(0,3):
        if guesses[x]==dicerolls[x]:
            total+=1
    print("[Correct guesses]:",total)
    print(dicerolls)

dicegame()