s1,s2='123','12.34'
print(int(s1),type(int(s1)))
print(float(s2),type(float(s2)))
print(float(s1),type(float(s1)))
# 123 <class
print(eval(s1),type(eval(s1)),eval(s2),type(eval(s2)))
print(eval('s1+s2'),type(eval('s1+s2')))
eval('print(s1+s2)')
eval('print(2+3)')