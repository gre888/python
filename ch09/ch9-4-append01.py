import os
pName='c:/data/'
if not os.path.exists(pName):
    os.makedirs(pName)
fa=open('c:/data/stu.txt','a')
fa.write('\n趙七海,85,90')
fa.write('\n陳九東,75,80')    
fa.flush()
fa.close()
