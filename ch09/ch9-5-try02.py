def div(n1,n2):
  try:
    res=n1/n2
    print("除法結果=",res)
  except Exception as e:
    print("除法錯誤:", e)
  finally:
    print("除法運算結束")
    

div(8,0)
div(8,5)      