lines=[]
num_of_lines=int(input())
for i in range(num_of_lines):
    lines.append(input())

for i in lines:
    counter=0
    current=i[0]
    answer=''
    for j in i:
        if j==current:
            counter+=1
        else:
            answer+=str(counter)+' '+current+' '
            current=j
            counter=1
    answer += str(counter) + ' ' + current + ' '
    print(answer)