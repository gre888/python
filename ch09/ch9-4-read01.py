import os
fName='c:/data/stu.txt'
if os.path.exists(fName):
  fr=open(fName,'r')
  str1=fr.read(7)
  print(str1)
  print(fr.read())
  fr.close()
else:
  print(f'{fName}路徑不存在,無法讀取檔案')  
  


with open('c:/data/stu.txt','r',encoding='utf-8') as fr:
  content=fr.read(7)
  content+=fr.read()
  print(content)  