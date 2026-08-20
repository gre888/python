import os
fName='c:/data/stu.txt'
if os.path.exists(fName):
  with open(fName,'r',encoding='utf-8') as fr:
    str1=fr.readlines()
    print(str1,end='')
    str2=fr.readline(7)
    print(str2)
    print(fr.read())
else:
  print(None)
  
