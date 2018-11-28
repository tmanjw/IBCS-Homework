import codecs
import pickle

f=open('movies.txt','r')

movies_attributes=[]
movies=[]

with codecs.open('movies.txt','r',encoding='utf-8') as f:
    count=0
    for line in f.readlines():
        line=line.strip()
        line=line.replace('\t',"")
        line=line.split(';')
        for i in range(len(line)):
            if line[i]=="":
                line[i]="N/A"
        line = list(line)

        if count==0:
            movies_attributes+=[line]
            count+=1
        elif count==1:
            count+=1
        else:
            if len(line)==10:
                movies+=[line]
            else:
                pass

# print(movies_attributes)

with codecs.open('movie.tsv','w',encoding='utf-8') as f:
    for i in movies:
        for j in i:
            f.write(j + '\t')
        f.write('\n')

by_year={}
for i in range(len(movies)):
    year=movies[i][0]
    by_year[year]=[]
for j in movies:
    by_year[j[0]]+=[j]

by_actor={}
for i in range(len(movies)):
    actor=movies[i][4]
    by_actor[actor]=[]
for j in movies:
    by_actor[j[4]]+=[j]

by_actress={}
for i in range(len(movies)):
    actress=movies[i][5]
    by_actress[actress]=[]
for j in movies:
    by_actress[j[5]]+=[j]

by_director={}
for i in range(len(movies)):
    director=movies[i][6]
    by_director[director]=[]
for j in movies:
    by_director[j[6]]+=[j]


with open('byyear.pickle','wb') as f:
    pickle.dump(by_year,f)

with open('byactor.pickle','wb') as f:
    pickle.dump(by_actor,f)

with open('byacress.pickle','wb') as f:
    pickle.dump(by_actress,f)

with open('bydirector.pickle','wb') as f:
    pickle.dump(by_director,f)

