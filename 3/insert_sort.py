#挿入ソート
#列の先頭からソート済み部分が後方に広がっていく
#初期状態は先頭がソート済み部分。
#未ソート部分の先頭を、ソート済部分に順に適切な場所に挿入していく

import random

random.seed(1)
A = [random.randint(0,100) for _ in range(10)]

if __name__ == '__main__':
    
    print("input ", A)
    i = 0
    for i in range(1, len(A)):
        val = A[i] # 挿入対象の値
        j = i - 1
        while j >= 0 and A[j] > val:
            A[j + 1] = A[j]
            j -= 1
        A[j+1] = val
        print("trace ", A)
    print("result", A)
