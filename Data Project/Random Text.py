f=open('data.txt','r')

text =[]

with open('data.txt','r') as f:
    text=''
    for line in f.readlines():
        text+=line.strip()

    text=text.split('. ')
    for i in text:
        for j in i:
            pass
        if j =='.':
            print(i)
        else:
            print(i+'.')