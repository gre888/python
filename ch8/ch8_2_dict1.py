dict1={'一月':'正月', '二月':'二月','三月':'梅月'}
print(dict1)
print(dict1['三月'])
dict1['一月']='端月'
print(dict1['一月'])
print(dict1)
dict1['一月']='正月'
print(dict1['一月'])
print(dict1)
print('1月'in dict1)
del dict1['一月']
print(dict1)