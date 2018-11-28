import matplotlib.pyplot as plt
import random
from Analysis import genrecount, moviesbyactor, movielengthbyyear


#Movie Length By Year
movielength = []
for i in movielengthbyyear:
    movielength+=[movielengthbyyear[i]]

movielength=tuple(movielength)

print(movielength)

fig, ax = plt.subplots()
bar_width = 0.5

bar1_index=[]
for i in range(0,len(movielength)):
    bar1_index += [i+0.5]
print(bar1_index)

rects1 = ax.bar(bar1_index, movielength, bar_width, color='b',  label='Time')

xlabel=[]
for i in movielengthbyyear:
    xlabel+=[i]

ax.set_xlabel('Year')
ax.set_ylabel('Movie Length')
ax.set_title('Average Length of Movies by Year')
ax.set_xticks(bar1_index)
ax.set_xticklabels(xlabel)
ax.legend()

fig.tight_layout()
plt.show()