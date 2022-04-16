import random

# r = random.randint(1,3)
# i = int(input('輸入猜的數字: '))
# print('正確答案',r)

while True:
    r = random.randint(1,3)
    i = int(input('輸入猜的數字: '))
    print('正確答案',r)
    if r == i:
        print('猜對囉!!!')
        break
    else:
        print('答錯!')