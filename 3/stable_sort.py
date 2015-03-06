#3.5 安定なソート

import random
import itertools
import collections

#構造体
Card = collections.namedtuple("Card", "suit, value")

# カードを作成
data = list(map(Card._make,itertools.product("SHCD",range(1,10))))
random.seed(2)
random.shuffle(data)

# バブルソート
def bubble_sort(C):
    N = len(C)
    for i in range(N):
        for j in range(N-1, i-1, -1):
            if C[j].value < C[j-1].value:
                C[j], C[j-1] = C[j-1], C[j]

# 選択ソート
def selection_sort(C):
    N = len(C)
    for i in range(N):
        minj = i
        for j in range(i, N):
            if C[j].value < C[minj].value:
                minj = j
        C[i], C[minj] = C[minj], C[i]
            
if __name__ == '__main__':
    
    C1 = list(data)
    C2 = list(data)
    
    # バブルソートは安定
    bubble_sort(C1)
    print("bubble sort result", C1)
    print("stable")
    
    # 選択ソートが安定かどうか判定
    selection_sort(C2)
    print("selection sort result", C2)
    if(C1 == C2):
        print("stable")
    else:
        print("unstable")

