import os
fName='c:/data/stu.txt'
if os.path.exists(fName):
  fr=open(fName,'r')
  lst=fr.readlines()
  for lines in lst:
    print(lines.strip())
  fr.close()
else:
  print(f'{fName}路徑不存在,無法讀取檔案')
  