#MyNegative8Ball

import random

def prediction():
    #write negative answers
    ans1="Don't bother."
    ans2="No way, never happening."
    ans3="Nope, don't think so."
    ans4="You will never know if you never tried, wait you have, ok yeah give up."
    ans5="You are delusional."
    ans6="Only you can save mankind! Not."
    ans7="You can do it! And fail, but no matter, try again! And fail again."
    ans8="Your choice, it doesn't matter, we all die in the end."

    print("Welcome to The Negative8Ball.\n")
    name=input("Let's get this over with... Name?",)
    print("Ok",name)
    #get the users question
    input("What do you want from me this time? \nOh and don't shake to hard or I'll puke\n")
    print("EVERYTHING IS SPINNINGGGGG!!!\n"*4)
    print("I think I'm going to be sick...\n")

    #use the randint() function to select the negative answer
    choice = random.randint(1,8)
    if choice == 1:
        answer=ans1
    elif choice == 2:
        answer=ans2
    elif choice == 3:
        answer=ans3
    elif choice == 4:
        answer=ans4
    elif choice == 5:
        answer=ans5
    elif choice == 6:
        answer=ans6
    elif choice == 7:
        answer=ans7
    else:
        answer=ans8

    #print the answer to the screen
    print(answer)
    input("\n\nSatisfied yet? Now leave me alone!.")
