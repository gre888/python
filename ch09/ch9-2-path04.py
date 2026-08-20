import os
pName='c:/data/'
if os.path.exists(pName):
  print(f'{pName}路徑已存在')
  os.rmdir(pName)
  print(f'{pName}路徑已刪除')
else:
  print(f'{pName}路徑不存在,不必刪除')
