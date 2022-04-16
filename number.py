import random
start = int(input('請決定隨機數字開始值: '))
end = int(input('請決定隨機數字結束值: '))
r = random.randint(start,end)
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