#挿入ソート
#列の先頭からソート済み部分が後方に広がっていく
#初期状態は先頭がソート済み部分。
#未ソート部分の先頭を、ソート済部分に順に適切な場所に挿入していく

import random

data_count = 10
data_min = 0
data_max = 100

random.seed(1)
data = [random.randint(data_min,data_max) for _ in range(data_count)]

if __name__ == '__main__':
    
    print("input ", data)
    i = 0
    for i in range(1, len(data)):
        val = data[i] # 挿入対象の値
        j = i - 1
        while j >= 0 and data[j] > val:
            data[j + 1] = data[j]
            j -= 1
        data[j+1] = val
        print("trace ", data)
    print("result", data)
