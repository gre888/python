def d(n):
   if n <= 1:
       return 1
   else :            # n > 1        
       return n * d(n-1) 
 
while True:
   n = eval(input('n = '))
   if (n >= 1):
       break
   else:
       print('輸入資料不符, 請重新輸入...')
 
fac = d(n)
print (f'{n}! = {fac}')