lines=[]
num_of_lines=int(input())
for i in range(num_of_lines):
    line=input().split(' ')
    lines.append((int(line[0]),line[1]))

for i in range(len(lines)):
    print(lines[i][0]*lines[i][1])