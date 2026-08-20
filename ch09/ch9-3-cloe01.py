import os
pName='c:/data/'
if not os.path.exists(pName):
    os.makedirs(pName)
# fw=open('c:/data/file01.txt','w')
fName=open('c:\\data\\file02.txt','w')
fName.close()    

with open('c:/data/file02.txt','r') as fName:
    print(fName.read())