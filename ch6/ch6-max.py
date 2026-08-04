lst=[8 for x in range(5) ]
print('請依序輸入5個整數')
for i in range(5):
  print(f'輸入{i+1}個元素',end='')
  lst[i]=int(input())
max=lst[0]
for item in lst:
  if item>max:
    max=item  
print(f'最大值{max}')    