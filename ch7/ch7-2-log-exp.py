import math
print(f'數學常數π={math.pi}')
print(f'數學常數e={math.e}')
# 1000種狀態 需要多少位元bits
states=1000
bits_needed=math.ceil(math.log(states,2)) #9.96
print(f'存儲{states}需要的位數={bits_needed}')




principal=1000
rate=0.05
years=3
amount=principal*math.exp(rate*years)
print(f'連續複利後的總金額={amount:.2f}')