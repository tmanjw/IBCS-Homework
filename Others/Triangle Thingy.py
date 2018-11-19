for x in range(2,7):
    total=0
    for y in range(1,x+1):
        for z in range(1,y+1):
            total+=z
    print(x-1, ":",total)