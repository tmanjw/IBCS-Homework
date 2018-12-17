start=[]
end=[]
buckets=[]
cows=0

dictionary={}
with open('blist.in','r') as f:
    lines = f.readlines()
    count=0
    for line in lines:
        if count==0:
            cows=line.strip().split()
            cows=int(cows[0])
            print(cows)
            count+=1
        else:
            s,e,b=line.strip().split()
            dictionary[int(s)]=[int(s),int(e),int(b)]

sortkeys=sorted(dictionary)
for i in range(len(dictionary)):
    start+=[dictionary[sortedkeys[i]][0]]
print(start)
# start+=[s]
# end+=[e]
# buckets+=[b]
print(dictionary)
# print(start)
# print(end)
# print(buckets)


# for i in range(cows):
#     if i == 0:
#         free+=[False]
#         for j in range(buckets[0]):
#             pass
