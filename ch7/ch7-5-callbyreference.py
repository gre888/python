# 呼叫函式時，傳遞參數的方式有兩種：傳值呼叫 (Call by Value) 與傳址呼叫 (Call by Reference)。
# 在 Python 中，所有的參數都是以「傳值呼叫」的方式傳遞，但對於可變物件 (如 list、dict 等) 的參數，函式內部對其進行修改時，會影響到原始物件，這種情況看起來像是「傳址呼叫」。
# 以下範例說明了傳值呼叫的概念，對於不可變物件 (如 int、float、str 等) 的參數，函式內部對其進行修改時，不會影響到原始物件。


def Triple(lst):
  for i in range(len(lst)):
     lst[i] = lst[i] * 3
  print('執行 Triple() 函式 ------')
  print(f'串列 lst = {lst}')
print()

 
arr = [2, 4, 6, 8, 10]
print('呼叫 Triple() 函式前 ------')
print(f'串列 arr = {arr}')
print()
Triple(arr)
print('呼叫 Triple() 函式後 ------')
print(f'串列 arr = {arr}')