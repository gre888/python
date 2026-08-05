import random

dice_result=random.randint(1,6)
print(f'骰子點數：{dice_result}')

even_num=random.randrange(0,10,2)
print("2. randrange案例抽0-8之間的偶數",even_num)

chance=random.random()
print("3. random案例抽機率/百分比",chance)

temperature=random.uniform(36.0,37.5)
print(f'4. uniform案例 隨機體溫 {temperature:.2f}度')

pets=['貓咪','狗狗','兔子',"倉鼠"]
my_pet=random.choice(pets)
print(f'5. choice案例 隨機選擇寵物 {my_pet}')

lottery_pool=[1,2,3,4,5,6,7,8,9,10]
winning_numbers=random.sample(lottery_pool,3)
print(f'6. sample案例 抽三個不重複獎號 {winning_numbers}')

poker_cards=['A','J','Q','K','10'] #
random.shuffle(poker_cards)
print(f'7. shuffle案例 洗牌後的撲克牌順序 {poker_cards}')