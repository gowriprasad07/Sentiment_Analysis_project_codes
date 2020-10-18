import pickle
f=open('consolidate_Twitter.pickle','rb')
count=0

while 1:
    try:
        pickle.load(f)
        count+=1
    except EOFError:
        print('Done')
        break
f.close()
    
        
    
