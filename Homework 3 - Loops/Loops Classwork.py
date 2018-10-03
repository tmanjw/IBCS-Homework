#Loops
#print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
#Modify while loop

# #1.
# count=0
# while count<10:
#     print(count*10)
#     count+=1

# #2.
# count=0
# total=0.2
# print(0)
# while count<10:
#     total+=5.2/-10
#     print(total)
#     count+=1

#3.
# start=

print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
#Modify to for loop

#1.
# a=1
# b=2
# for i in range(0,5):
#     a=b*a+i
# print(a)

#2.
# for i in range(1,101):
#     print(i) if i%3 != 0 and i%8 !=0 else print("Is divisible by 3 or 8")

#3.
height=5
for i in range(0,height):
    if height / 2 - i == 0 or height / 2 - i == height / 2:
        print(" "*(int(height/2)-1),"*")