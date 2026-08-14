

class Calculator():
  def add(self,x,y=None):
    if y is not None:
      if isinstance(x,str) and isinstance(y,str):
        return f"{x}-{y}"
      return x+y
    return f'單一數字處理結果{x+10}'
  
  
  
calc = Calculator()
print(calc.add(5))
print(calc.add(10,20))
print(calc.add("Hello","World"))
  