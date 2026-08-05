import time as T
timer=T.localtime()
year=timer.tm_year
month=timer.tm_mon
day=timer.tm_mday
hour=timer.tm_hour
minute=timer.tm_min
sec=timer.tm_sec
print(f'{year}-{month}-{day} {hour}:{minute}:{sec}')