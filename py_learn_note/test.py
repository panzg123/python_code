myItems={1,2,3}
for item in myItems:
    f=open('test.txt','w+')
    f.write(item)
    f.close() 