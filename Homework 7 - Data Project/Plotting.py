import matplotlib.pyplot as plt
import random
from Analysis import genrecount, moviesbyactor, movielengthbyyear


#Movie Length By Year
xaxis1=sorted(movielengthbyyear)
movielength = []
for i in xaxis1:
    movielength+=[float(movielengthbyyear[i])]

movielength=tuple(movielength)

print(movielength)

fig, ax = plt.subplots()
bar_width = 0.5

bar1_index=[]
for i in range(0,len(movielength)):
    bar1_index += [i+0.5]
print(bar1_index)

rects1 = ax.bar(bar1_index, movielength, bar_width, color='b',  label='Time')


ax.set_xlabel('Year')
ax.set_ylabel('Movie Length')
ax.set_title('Average Length of Movies by Year')
ax.set_xticks(bar1_index)
ax.set_xticklabels(xaxis1)
ax.legend()

fig.tight_layout()
plt.show()

#Movies by Actor
xaxis2=sorted(moviesbyactor)
nummovies = []
for i in xaxis2:
    movielength+=[float(movielengthbyyear[i])]

movielength=tuple(movielength)

print(movielength)

fig, ax = plt.subplots()
bar_width = 0.5

bar1_index=[]
for i in range(0,len(movielength)):
    bar1_index += [i+0.5]
print(bar1_index)

rects1 = ax.bar(bar1_index, movielength, bar_width, color='b',  label='Time')


ax.set_xlabel('Year')
ax.set_ylabel('Movie Length')
ax.set_title('Average Length of Movies by Year')
ax.set_xticks(bar1_index)
ax.set_xticklabels(xaxis2)
ax.legend()

fig.tight_layout()
plt.show()
