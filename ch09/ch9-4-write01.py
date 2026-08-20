import os
pName='c:/data/'
if not os.path.exists(pName):
    os.makedirs(pName)

fw=open('c:/data/stu.txt','w')
fw.write('王一心,85,90\n')
fw.write('陳二心,75,80\n')
fw.write('林三心,65,70\n')
fw.flush()
fw.close()

with open('c:/data/stu.txt','w',encoding='utf-8') as fr:
  fr.write('王一心,85,90\n')
  fr.write('陳二心,75,80\n')
  fr.write('林三心,65,70\n')
  