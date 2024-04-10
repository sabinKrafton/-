import sys

input = sys.stdin.readline

N, K = map(int, input().split())

bag = [[0, 0]] + [list(map(int, input().split())) for _ in range(N)]

DP = [[0] * (K + 1) for _ in range(N + 1)]


for i in range(1, N + 1): # i는 물건 번호
    for j in range(1, K + 1): # j는 가방 무게
        if bag[i][0] > j:
            DP[i][j] = DP[i - 1][j]
        else:
            DP[i][j] = max(DP[i - 1][j], DP[i - 1][j-bag[i][0]] + bag[i][1])
# print(DP)
print(DP[-1][-1])