import random
import pickle
from Parsing import movies

with open('byyear.pickle','rb') as f:
    yeardict=pickle.load(f)

with open('byactor.pickle','rb') as f:
    actordict=pickle.load(f)

with open('byyear.pickle','rb') as f:
    actressdict=pickle.load(f)

with open('byyear.pickle','rb') as f:
    directordict=pickle.load(f)
    
# print('Year :',yeardict)
# print('Actor :',actordict)
# print('Actress :',actressdict)
# print('Director :',directordict)

# Movie Lengths by Year
totaltotal=0
movielengthbyyear={}
for i in yeardict:
    total=0
    less=0
    for j in range(len(yeardict[i])):
        if yeardict[i][j][1]=='N/A':
            less+=1
        else:
            total += int(yeardict[i][j][1])
            # print(yeardict[i][j][1])
    average=total/(len(yeardict[i])-less)
    movielengthbyyear[i]="%.2f"%average
    totaltotal+=total
totalaverage=totaltotal/len(movies)
movielengthbyyear["Total"]="%.2f"%totalaverage

# Number of Movies by Actor
moviesbyactor={}
for i in actordict:
    moviesbyactor[i]=len(actordict[i])

# Genre Count Per Decade
genrecount={}
for i in movies:
    try:
        decade=int(int(i[0])/10)*10
    except:
        decade="N/A"
    if decade not in genrecount:
        genrecount[decade]=[i[3]]
    else:
        if i[3] not in genrecount[decade]:
            genrecount[decade]+=[i[3]]
for i in genrecount:
    genrecount[i]=len(genrecount[i])