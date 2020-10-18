fb=open('Text_file2.txt','r',encoding="utf-8")


count=0
l=[]

while 1:
    try:
        a=fb.readline()
        count+=1
        if a[0]!='0':
            print(a)
            l.append(count)
    except EOFError:
        break
