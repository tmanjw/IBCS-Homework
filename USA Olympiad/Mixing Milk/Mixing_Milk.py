buckets = []
capacity = []

with open('mixmilk.in','r') as f:
    lines = f.readlines()

    for line in lines:
        c,m=line.strip().split()
        # print(c, m)
        c=int(c)
        m=int(m)
        buckets+=[c]
        capacity+=[m]

count=0
for i in range(0,100):
    count+=1
    step=i%3
    if step==0 or step==1:
        if capacity[step+1]==buckets[step+1]:
            var1=0
        elif capacity[step]>buckets[step+1]:
            var1=buckets[step+1]
        else:
            var1=capacity[step]
        capacity[step+1]+=var1
        capacity[step]-=var1

    if step==2:
        if capacity[0] == buckets[0]:
            var1 = 0
        elif capacity[step] > buckets[0]:
            var1 = buckets[0]
        else:
            var1 = capacity[step]
        capacity[0] += var1
        capacity[step] -= var1

#     print(capacity,step)
# print(count)

with open('mixmilk.out','w') as f:
    for i in range(0,3):
        f.write(str(capacity[i])+'\n')
