import random

r = random.randint(1,500)
num = 0
while True:
    num += 1
    print('進行第', num ,'次猜測!') 
    i = int(input('輸入猜的數字: '))
    if r == i:
        print('猜對囉!!!')
        break
    elif i < r :
        print('數字再大一點!')
    elif i > r :
        print('數字在小一點!')

print('在第', num ,'次終於猜對了!!!!!!!!')       