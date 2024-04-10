import sys

input = sys.stdin.readline

N = int(input())
meetings = [list(map(int, input().split())) for _ in range(N)]

meetings.sort(key = lambda x: (x[1], x[0]))

end_time = 0
cnt = 0

for meeting in meetings:
    if end_time <= meeting[0]:
        end_time = meeting[1]
        cnt += 1

print(cnt)