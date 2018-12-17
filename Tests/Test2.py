if capacity[step] > buckets[0]:
    var1 = buckets[0]
elif capacity[0] == buckets[0]:
    var1 = 0
else:
    var1 = capacity[step]
capacity[0] += var1
capacity[step] -= var1