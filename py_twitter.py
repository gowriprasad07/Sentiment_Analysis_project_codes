import pickle
import csv


t=[]
with open('tweets.csv','rt')as csvfile:
    a=csv.reader(csvfile)
    
    for i in a:
        
        try:
            
            z=open('total_data1.pickle','wb')
            #a=pickle.load(csvfile)
            t.append(a[0])
            pickle.dump(a,z)
        except EOFError:
            
            pass
d=api.statuses_lookup(t,tweet_mode='extended')
csvfile.close()
z.close()
