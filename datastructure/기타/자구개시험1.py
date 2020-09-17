datalist=[]
for i in range(5):
    datalist.append(i)

print(datalist[0:3])

datalist1=datalist[0:3]
datalist2=datalist[3:]
datalist=datalist1+[12]+datalist2

print(datalist)

datalist.append('')
for i in range(3):
    datalist[6-i]=datalist[5-i]
datalist[3]=5

print(datalist)
    
