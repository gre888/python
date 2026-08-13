from random import randint

pc=set()
while len(pc)<2:
    pc.add(randint(1,7))
print(pc,'請輸入1-7號碼 共三次機會')
count=3
while count>0:
  you=set()
  while len(you)<2:
    x= int(input('請輸入號碼:'))
    if(x<=7 and x>0):
      you.add(x)
  print('你輸入的兩個數字是:', you)
  if you==pc:
    print('恭喜你猜中')
    break
  count -= 1
else:
  print('很遺憾你沒有猜中,答案是:',pc)  
  