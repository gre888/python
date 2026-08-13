dates={'A001':['汽水',25],
       'A005':['公主麵',10],
       'A006':['口香糖',8],
       'A003':['冰棒',20]
}

num=input('請輸入商品編號:')
if num not in dates:
    print(num,'查無此商品')
    id=input('請輸入商品名稱:')
    money=input('請輸入商品金額:')
    dates[num]=[id,money]
print(num,dates[num])    
d=dates.get(num)
print(num,d)