import pickle
from nltk.stem import PorterStemmer
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
from nltk.stem.snowball import SnowballStemmer

f=open('Full_text_without_emoji.pickle','rb')
fb=open('preprocessing.pickle','wb')
st=set(stopwords.words('english'))
count=0

while 1:
    q=[]
    t=[]
    b=[]
    k=pickle.load(f)
    count+=1
    s=k[1].split()
    
    for j in s:
        if j not in st:
            q.append(j)
    ps=PorterStemmer()
    for i in q:
        r=ps.stem(i)
        t.append(r)

    stemmer = SnowballStemmer("english")
    for e in q:
        x=stemmer.stem(e)
        b.append(x)
    k.append(b)
    k.append(s)
    k.append(t)

    pickle.dump(k,fb)
    print("Done")

f.close()
fb.close()


        
        
            
            
            
