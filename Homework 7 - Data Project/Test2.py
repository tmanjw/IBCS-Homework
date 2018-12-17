import matplotlib.pyplot as plt
from random import random

means_men = (20, 35, 30, 35, 30)

fig, ax = plt.subplots()
bar_width = 0.5

bar1_index = [0.5, 1.5, 2.5, 3.5, 4.5]

rects1 = ax.bar(bar1_index, means_men, bar_width, color='b',  label='Men')

ax.set_xlabel('Group')
ax.set_ylabel('Scores')
ax.set_title('Scores by group and gender')
ax.set_xticks(bar1_index)
ax.set_xticklabels(('A', 'B', 'C', 'D', 'E'))
ax.legend()

fig.tight_layout()
plt.show()