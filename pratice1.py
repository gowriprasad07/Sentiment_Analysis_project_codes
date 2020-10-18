f='example.txt'
file=open(f,'w')
for i in range(1,11):
    print(file.write('this is line %i.\n'%i))
file.close()
