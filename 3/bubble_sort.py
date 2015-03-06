#バブルソート
# 配列の末尾から隣接する要素を比べていき、大小関係が逆ならば交換する

import random

random.seed(1)
A = [random.randint(0,100) for _ in range(10)]

if __name__ == '__main__':
    
    print("input ", A)
    sw = 0
    flag = True
    N = len(A)
    for i in range(0, N):
        if flag == False:
            break
        flag = False
        for j in range(N-1, i, -1):
            if A[j] < A[j-1]:
                A[j-1], A[j] = A[j], A[j-1]
                flag = True
        print("trace ", A)
    print("result", A)
