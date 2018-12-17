#Sorting Algorithms
# I am going to be annotating through my code again! So be prepared for some emojis d:

#Bubble Sorting algorithms
def bubble_sort(lst):

    #A while loop to check whether or not the list has finished sorted
    repeat=True
    while repeat == True:
        #This variable is reset if the list is not completely sorted
        change=False

        #Has to minus 1 from the range, otherwise an index error will, we do not need to go the full length
        for i in range(len(lst)-1):
            #The conditional statement, if the first variable in list is bigger then the next one
            if lst[i+1]<lst[i]:
                var1=lst[i]
                lst[i]=lst[i+1]
                lst[i+1]=var1
                #There has been a change to the list therefore it is not finished
                change=True

        print(lst)
        #Checks to see if list has been changed, if not then it has finished
        if change==False:
            '''Eat ass smke grass'''
            repeat=False

    return(lst)

list1=[1,3,4,6,5,2]
# print(bubble_sort(list1))

#Selection Sort! :D
def selection_sort(lst):

    #Runs through the length of the list -1
    for i in range(len(lst)-1):

        #Uses a nested loop to compare to other numbers, doesn't compare with self
        for j in range(i+1,len(lst)):

            #Conditional statement comparing the two variables
            if lst[j] < lst[i]:

                #Same code as bubble sort
                var1=lst[i]
                lst[i]=lst[j]
                lst[j]=var1

        print(lst)
    return(lst)

# selection_sort(list1)

#Insertion Sorting
def insertion_loop(lst):

    #Loop starts from 1 since we will be comparing 'i' to the one before (-1, 0 minus 1 is out of range)
    for i in range(1,len(lst)):
        var1 = lst[i]

        #Setting default position of 'j' to be one position before
        j=i-1

        #While loop ensures keeps comparing the values ahead of position 'i'
        while lst[j]>lst[j+1] and j >=0 :
            #Switching around the values if lst[i] is smaller
            lst[j+1]=lst[j]
            lst[j]=var1
            j-=1
        return(lst)

print('Done :',insertion_loop(list1))

'''
//Insertion Loop Pseudocode
//http://ibcomp.fis.edu/pseudocode/pcode.html

LST=[3,6,4,2,5,1]

loop INDEX from 1 to 6
   CURRENT = LST[INDEX]
   CHECK = INDEX - 1
   loop while LST[CHECK] > LST[CHECK+1] AND CHECK >= 0
      LST[CHECK+1] = LST [CHECK]
      LST[CHECK] = CURRENT
      CHECK = CHECK - 1
   end loop
end loop

output LST
'''