import datetime as DT
# 取得目前的日期與時間
nowTime = DT.datetime.now()
# 以不同方式格式化輸出日期與時間
print('{:%Y/%b/%d %A}'.format(nowTime))
# 使用 f-string 格式化
print(f'{nowTime:%Y/%b/%d %A}')
# 使用 strftime 方法格式化
print(nowTime.strftime("%Y/%b/%d %A"))