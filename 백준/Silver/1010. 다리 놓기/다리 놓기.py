import sys

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    A = 1
    B = 1
    for i in range(N):
        A *= M
        M -= 1
    for j in range(2, N+1):
        B *= j
    print(A//B)