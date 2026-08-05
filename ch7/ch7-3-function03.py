def progress(a1,d,n):
  an=a1+(n-1)*d
  sn=n*(a1+an)/2
  return an,sn

a1=eval(input("請輸入首項:"))
d=eval(input("請輸入公差:"))
n=eval(input("請輸入第n項:"))

an,sn=progress(a1,d,n)
print(f"第{an}項為:{an},前{an}項和為:{sn}")
