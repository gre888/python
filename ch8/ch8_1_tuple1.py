tuple1=('東','南','西',)
print(tuple1) # ('東', '南', '西')
east,south,west=tuple1 #解構
print(east) # 東
print(south) # 南 
tuple2=tuple1+('北',) # tuple1+('北',)
print(tuple2) # ('東', '南', '西', '北')
tuple1,tuple2=tuple2,tuple1 # tuple1,tuple2=tuple2,tuple1
print(tuple1) # ('東', '南', '西', '北')
print(tuple2) # ('東', '南', '西')
print(len(tuple1)) # 4
del(tuple2) # del(tuple2)

list1=list(tuple1)
print(list1) # ['東', '南', '西', '北']
list1.append('東北')
print(list1) # ['東', '南', '西', '北', '東北']
tuple1=tuple(list1) # tuple1=tuple(list1)
print(tuple1) # ('東', '南', '西', '北', '東北')
print(tuple1[0])
print('東北' in tuple1) # True
for t in tuple1:
    print(t,end=' ')# 東 南 西 北 東北