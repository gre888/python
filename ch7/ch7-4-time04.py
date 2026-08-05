import time as T
t1=T.time()
print(f'暫停電腦前時間{t1}')
T.sleep(5)
t2=T.time()
print(f'暫停電腦後時間{t2}')
print(f'電腦暫停了{t2-t1:.7f}秒')

