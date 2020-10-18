import pickle

f=open('Full_text_without_emoji.pickle','rb')
fb=open('preprocessing.pickle','wb')

while 1:
    k=pickle.load(f)

    pickle.dump(k,fb)
    print("Done")
    
