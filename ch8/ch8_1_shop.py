
data = (('香蕉', 34, 2), ('芭樂', 28, 3), ('水梨', 50, 2))
total = []
# 印出表格的標題列，使用 \t (Tab) 進行欄位分隔與對齊
print ('品  名\t數  量\t單  價\t小  計')
for t1 in data:
    name,s1,s2 = t1
    total.append(s1 * s2)
    print(f'{name:>4}{s1:8}{s2:8}{s1*s2:8}')
    # print(f'{name:>4}{s1:8}{total[-1]:8}')  # 也可以使用 total[-1] 來印出最新的小計金額  字串預設向左靠 數值向右靠所以>4
# 使用 sum(total) 加總所有商品的小計，並靠右對齊格式化印出總金額（寬度占 23 個字元）
print(f'總  計:{sum(total):23}')