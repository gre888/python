import os
fName='c:/data/stu.txt'
if os.path.isfile(fName):
  with open(fName,'a+') as fa:
    fa.seek(16)
    str1=fa.readline()
    print(str1,end=" ")
    fa.seek(0)
    str2=fa.readline()  
    print(str2,end=" ")
else:
  print("檔案不存在")    