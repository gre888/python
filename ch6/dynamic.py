lst=[]
c=eval(input('串列元素'))
for i in range(c):
  print(f'輸入第{i+1}')
  num=eval(input())
  lst.append(num)
print(lst)
for x in lst:
  print(x,end='')