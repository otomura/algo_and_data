#バブルソート
# 配列の末尾から隣接する要素を比べていき、大小関係が逆ならば交換する

import random

data_count = 10
data_min = 0
data_max = 100

random.seed(1)
data = [random.randint(data_min,data_max) for _ in range(data_count)]

if __name__ == '__main__':
    
    print("input ", data)
    sw = 0
    flag = True
    N = len(data)
    for i in range(0, N):
        if flag == False:
            break
        flag = False
        for j in range(N-1, i, -1):
            if data[j] < data[j-1]:
                temp = data[j-1]
                data[j-1] = data[j]
                data[j] = temp
                flag = True
        print("trace ", data)
    print("result", data)
