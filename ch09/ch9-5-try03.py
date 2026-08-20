arr=[0 for x in range(5)]
try:
  arr[4]=40
  print("陣列元素arr[4]=",arr[4])
  arr[9]=90
  print("陣列元素arr[9]=",arr[9])
except ZeroDivisionError:
  print("陣列錯誤: 除數為零")
except IndexError:
  print("串列錯誤: 串列索引超出範圍")
except Exception as e:
  print("錯誤類型:", e)
finally:
  print("陣列運算結束")  
  