#Binary Searching
numbers=[2,4,8,10,15,16,19]

def binary_search(search,lst):
    half = int(len(lst) / 2)
    while half!=search:
        half=int(len(lst)/2)
        if lst[half]==search:
            return True
        elif lst[half]<search:
            lst=lst[half:]
        elif lst[half]>search:
            lst=lst[:half]

print(binary_search(3,numbers))