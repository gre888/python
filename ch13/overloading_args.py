

class Calculator():
  def add(self, *args):
    if len(args) == 2:
      x, y = args[0], args[1]
      if isinstance(x,str) and isinstance(y,str):
        return f"{x}-{y}"
      return x+y
    elif len(args) == 1:
      x = args[0]
      return f'單一數字處理結果{x+10}'
    else:
      raise ValueError("Invalid number of arguments")
  
  
  
calc = Calculator()
print(calc.add(5))
print(calc.add(10,20))
print(calc.add("Hello","World"))