#選択ソート
# 先頭からソート済部分が広がる
# 未ソート部分から最少要素を特定し、未ソート部分の先頭に持ってくる。

import random

A_count = 10
A_min = 0
A_max = 100

random.seed(1)
A = [random.randint(0,100) for _ in range(10)]

if __name__ == '__main__':
    
    print("input ", A)
    N = len(A)
    for i in range(0, N):
        minj = i
        for j in range(i, N):
            if A[j] < A[minj]:
                minj = j
        A[i], A[minj] = A[minj], A[i]
        print("trace ", A)
    print("result", A)
