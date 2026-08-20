def div(n1,n2):
  try:
    res=n1/n2
    print("除法結果=",res)
  except ZeroDivisionError:
    print("除法錯誤: 除數不能為零")

div(8,0)
div(8,5)
  