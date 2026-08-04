import math
items=23
capacity_per_box=10
boxes_needed=math.ceil(items/capacity_per_box)
print(f'需要{boxes_needed}個箱子來裝{items}個物品')


rent_hours=50
days=math.floor(rent_hours/24)
print(f'滿天數{days}')