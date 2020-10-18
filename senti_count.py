f=open('Text_file9+results.txt','r',encoding='utf-8')

positive=0
negative=0
neutral=0

while 1:
    try:   
        fb=f.readline()
        s=fb.split('\t')
        i=int(s[3])+int(s[4])

        if i>0:
            positive+=1
        elif i<0:
            negative+=1
        else:
            neutral+=1
    except EOFError:
        break
    except:
        print(s)
f.close()

print('positive ',positive)
print('negative ',negative)
print('neutral ',neutral)

            
