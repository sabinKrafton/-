# day 1 / 03.22

# baek 10869 사칙연산

# A, B = map(int, input().split())

# print(A+B)
# print(A-B)
# print(A*B)
# print(int(A/B))
# print(A%B)

#--------------------------------

# baek 9498

# score = int(input())
# if 90 <= score <=100:
#     print('A')
# elif 80 <= score <90:
#     print('B')
# elif 70 <= score < 80:
#     print('C')
# elif 60<= score <70:
#     print('D')
# else:
#     print('F')

#--------------------------------

# Baek 2739

# N = int(input())

# for i in range(1, 10):
#     print('{} * {} = {}'.format(N, i, N*i))

#--------------------------------

# Baek 2562

# L =  []

# for i in range(9):
#     L.append(int(input()))

# print(max(L))
# print(L.index(max(L))+1)

#--------------------------------

# Baek 15596

# n = list(map(int, input().split()))

# def solve(a):
#     ans = 0
#     for i in a:
#         ans += i
#     return ans

# print(solve)

#--------------------------------

# Baek 11654

# n = input()

# print(ord(n))

#--------------------------------

# Baek 2675

# T = int(input())

# for i in range(T):
#     A = ''
#     R, S = input().split()
#     R = int(R)
#     for j in S:
#         A += j*R
#     print(A)

#--------------------------------

# Baek 1978

# N = int(input())
# arr = map(int, input().split())
# count = 0

# for i in arr:
#     L = []
#     if i > 1:
#         for j in range(1, i+1):
#             if i % j == 0:
#                 L.append(j)
#     if len(L) == 2:
#         count += 1

# print(count)

#--------------------------------

# Baek 10872

# N = int(input())

# def factorial(x):
#     if x == 0:
#         return 1
#     return x * factorial(x-1)

# print(factorial(N))

#--------------------------------

# Baek 1914
# start 에서 end로 x개의 원판을 옮기는 함수 (1에서 3으로 가는 함수정의가 아니다.)

# def hanoi(x, start, end):
#     if x == 1:
#         print(start, end)
#         return
#     hanoi(x - 1, start, 6 - start - end)
#     print(start, end)
#     hanoi(x - 1, 6 - start - end, end)
    
# n = int(input())

# print(2 ** n - 1)
# if n <= 20:
#     hanoi(n, 1, 3)

# def hanoi(x, a, b, c):
#     if x == 1:
#         print(a, c)
#         return 1
#     hanoi(x-1, a, c, b)
#     print(a, c)
#     hanoi(x-1, b, a, c)

# n = int(input())

# print(2 ** n - 1)
# if n <= 20:
#     hanoi(n, 1, 2, 3)

# honoi(n, 1, 3) 함수를 딸칵 하면 바로 3단계로 나눈다

# def hanoi(a, b, c) -> a 개의 원판을 b에서 c로 옮긴다.  

# 1 단계 :  1번에 꽂혀있는 n개의 원판중 n-1개의 원판을 2번에다가 꽂아야한다. hanoi(n-1, 1, 2) /  예를 들어 1 2 3 막대가 있고, 1 막대에서 3 막대로 n개의 원판을 보내고 싶으면 무조건 2 막대로 n-1개의 원판을 보내야 한다. 
# 2 단계 :  1번에 꽂혀있는 1개의 원판을 3번에다가 꽂는다.                   hanoi(1, 1, 3)
# 3 단계 :  2번에 꽂혀있는 n-1개의 원판을 3번에다가 꽂는다.                 hanoi(n-1, 2, 3)
    

# 예를 들어 1 2 3 막대가 있고, 1 막대에서 3 막대로 n개의 원판을 보내고 싶으면 무조건 2 막대로 n-1개의 원판을 보내야 한다. 

#--------------------------------

# Baek 2750
#(1) sorted 사용 : sorted(리스트명) 는 리스트 원본은 건들지 않고 정렬 값을 반환한다.
# N = int(input())
# L = []

# for i in range(N):
#     L.append(int(input()))

# for i in sorted(L):
#     print(i)

# or
#(2) sort 사용 : 리스트명.sort() 는 리스트 원본값을 직접 수정한다.
# N = int(input())
# L = []

# for i in range(N):
#     L.append(int(input()))

# L.sort()

# for i in L:
#     print(i)

#--------------------------------

# Baek 1181

# N = int(input())
# L = []

# for i in range(N):
#     word = input()
#     L.append(word)

# L = list(set(L))

# L.sort()         
# L.sort(key = len)

# for i in L:
#     print(i)

# # or

# N = int(input())
# L = []

# for i in range(N):
#     word = input()
#     L.append(word)

# L = list(set(L))

# L = sorted(L)         
# L = sorted(L, key = len)         


# for i in L:
#     print(i)

# -------------------------------------------------------------

# Baek 2309 일곱난쟁이

# L = [int(input()) for i in range(9)]
# L.sort()
# A = sum(L)

# for i in range(len(L)):
#     for j in range(i+1, len(L)):
#         if A - L[i] - L[j] == 100:
#             for k in range(len(L)):
#                 if k == i or k == j:
#                     pass
#                 else:
#                     print(L[k])
#             exit()

#------------------------------------

#Baek 1920 이분 탐색

# N = int(input())
# A = list(map(int, input().split()))
# M = int(input())
# B = list(map(int, input().split()))

# A.sort()

# for i in B:
#     left_index = 0
#     right_index = N-1
#     isExist = False

#     while left_index <= right_index:
#         mid_index = (left_index + right_index) //2
#         if i == A[mid_index]:
#             isExist = True
#             print(1)
#             break
#         elif i > A[mid_index]:
#             left_index = mid_index + 1
#         elif i < A[mid_index]:
#             right_index = mid_index -1
#     if isExist == False:
#         print(0)

# or

# N = int(input())
# A = set(map(int, input().split())) # set으로 중복제거
# M = int(input())
# B = list(map(int, input().split()))

# for i in B:
#     if i in A:
#         print(1)
#     else:
#         print(0)

#----------------------------------------------------

# Baek 2630

# N = int(input())
# A = []

# for i in range(N):
#     A.append(list(map(int, input().split())))

# blue = 0
# white = 0

# def cut(x, y, N):
#     global blue, white
#     first = A[x][y]

#     for i in range(x, x + N):
#         for j in range(y, y + N):
#             if first != A[i][j]:  # 다른 경우가 생기면 자른다.
#                 cut(x, y, N//2)
#                 cut(x, y + N//2, N//2)
#                 cut(x + N//2, y, N//2)
#                 cut(x + N//2, y + N//2, N//2)
#                 return

#     if A[x][y] == 1:
#         print("파랑색!")
#         blue += 1
#     else:
#         print("하얀색!")
#         white += 1

# cut(0, 0, N)

# print(white, blue, sep='\n')

#----------------------------------------------------------

# Baek 11279 최대 힙

# N = int(input())


# # 힙 라이브러리 사용 최소힙만 구현 되어있음 , 최소힙을 최대힙으로 바꿔야함. 마이너스
# import heapq
# import sys
# input = sys.stdin.readline
# heap = []

# for i in range(N):
#     x = int(input())

#     if x == 0:
#         if len(heap) != 0:
#             heapq.heappush(heap, -x)
#             temp = heapq.heappop(heap)
#             print(-temp)
#         else:
#             print(0)
#     else:
#         heapq.heappush(heap, -x)
 

# ------------------------------

# 피보나치

# def fibo(x):
#     if x==0:
#         return 0
#     if x==1 or x==2 :
#         return 1
#     return fibo(x-1) + fibo(x-2)


# def fibo(x):
#     if x==0:
#         return 0
#     if x==1 or x==2 :
#         return 1 
#     a = 1
#     b = 1
#     for i in range(1, x):
#         a, b = b, b+a
#     return a

# ----------------------------------

# Baek 1920 수찾기

# 재귀
# N = int(input())
# A = list(map(int, input().split()))
# M = int(input())
# B = list(map(int, input().split()))

# A.sort()

# def search(arr, object):
#     start_idx = 0
#     end_idx = len(arr)-1
#     mid = (start_idx + end_idx) // 2
#     if start_idx > end_idx:
#         return 0
    
#     if object == arr[mid]:
#         return 1
#     if object < arr[mid]:
#         return search(arr[:mid], object)
#     else:
#         return search(arr[mid+1:], object)
  
# for i in range(len(B)):
#     print(search(A, B[i]))

# or

# N = int(input())
# A = list(map(int, input().split()))
# M = int(input())
# B = list(map(int, input().split()))

# A.sort()



# for i in B:
#     left_idx = 0
#     right_idx = N - 1
#     isexist = False

#     while left_idx <= right_idx:
#         mid_idx = (left_idx + right_idx) // 2
#         if A[mid_idx]== i:
#             print(1)
#             isexist = True
#             break
#         elif A[mid_idx] > i:
#             right_idx = mid_idx-1
#         elif A[mid_idx] < i:
#             left_idx = mid_idx +1
#     if isexist != True:
#         print(0)

# ---------------------------------------------

# Baek 10828 스택
# import sys

# input = sys.stdin.readline

# N = int(input())
# A = []

# for _ in range(N):
#     word = input().split()
#     if word[0] == 'push':
#         A.append(int(word[1]))
#     if word[0] == 'pop':
#         if len(A) == 0:
#             print(-1)
#             continue
#         print(A.pop())
#     if word[0] == 'size':
#         print(len(A))
#     if word[0] == 'empty':
#         if len(A) == 0:
#             print(1)
#         else:
#             print(0)
#     if word[0] == 'top':
#         if len(A) == 0:
#             print(-1)
#         else:
#             print(A[-1])

#---------------------------------------

# Baek 11866 요세푸스 문제

# from collections import deque

# N, K = map(int, input().split())

# A = [i for i in range(1, N + 1)]
# B = []
# idx = 0

# while A:
#     idx += K - 1
#     if idx >= len(A):
#         idx %= len(A) # 나머지를 구하는 연산으로 인덱스를 넘긴다.
#     B.append(str(A.pop(idx)))

# print('<', ', '.join(B), '>', sep = '')

# or

# A = deque([i for i in range(1, N+1)])
# B = []

# while len(A) != 0:
#     for _ in range(K-1):
#         A.append(A.popleft())
#     B.append(str(A.popleft()))

# print('<', ', '.join(B), '>', sep = '')

# A.rotate(-1) 을 해도 가능 deque 에서 지원하는 함수로 배열을 회전 시킴

# -------------------------

# Baek 18258 큐 2 # 삼항 연산자

# from collections import deque
# import sys

# input = sys.stdin.readline

# N = int(input())
# A = deque([])

# for i in range(N):
#     word = input().split()
#     if word[0] == 'push':
#         A.append(word[1])
#     if word[0] == 'pop':
#         print(-1 if len(A) == 0 else A.popleft())
#     if word[0] == 'size':
#         print(len(A))
#     if word[0] == 'empty':
#         print(1 if len(A) == 0 else 0)
#     if word[0] == 'front':
#         print(-1 if len(A) == 0 else A[0])
#     if word[0] == 'back':
#         print(-1 if len(A) == 0 else A[-1])

#-------------------------------------------

# Baek 9020 골드바흐의 추측

# import sys

# input = sys.stdin.readline

# T = int(input())

# def prime_dicision(x):
#     for i in range(2, x):
#         if x % i == 0:
#             return False
#     return True

# for i in range(T):
#     n = int(input())
#     A = []
#     for j in range(2, n):
#         for k in range(2, n):
#             if j + k == n:
#                 if prime_dicision(j) and prime_dicision(k):
#                     A.append([j, k])
#     if len(A) > 1:
#         B = []
#         for l in A:
#             B.append(abs(l[0]-l[1]))
#         print(*A[B.index(min(B))], sep = ', ')
#     elif len(A) == 1:
#         print(*A, sep = ', ')
#     else:
#         print('입력하신 수가 짝수가 아닙니다.')

# for i in range(T):
#     n = int(input())

#     a,b = int(n/2), int(n/2)
#     while a > 0:
#         if prime_dicision(a) and prime_dicision(b):
#             print(a, b)
#             break
#         else:
#             a -= 1
#             b += 1

#----------------------------------


# Baek 9663 N - Queen
# 뭐가 열이고 뭐가 행인지 정확하게 인지하고
# 더이상 진행할 수 없다면 이전의 함수를 이어서 실행하고 반복.

# N = int(input())

# arr = [0] * N
# cnt = 0

# def decision(x):
#     for i in range(x):
#         if arr[x] == arr[i] or abs(arr[x] - arr[i]) == abs(x - i):
#             return False
#     return True

# def n_queen(x):
#     global cnt
#     if x == N:
#         cnt += 1
#         return
#     else:
#         for i in range(N):
#             arr[x] = i
#             if decision(x):
#                 n_queen(x+1)

# n_queen(0)
# print(cnt)

# -------------------------------------

# Baek 2751  수 정렬하기 2
# import sys

# input = sys.stdin.readline

# N = int(input())

# A = []

# for i in range(N):
#     A.append(int(input()))

# for i in sorted(A):
#     print(i)

# ----------------------------

# Baek 10971 외판원 순회 2

import sys


def dfs(start, now, value, cnt):
    global ans
    if cnt == N:
        if a[now][start]:
            value += a[now][start]
            if ans > value:
                ans = value
        return

    if value > ans:
        return

    for i in range(N):
        if not visited[i] and a[now][i]:
            visited[i] = 1
            dfs(start, i, value + a[now][i], cnt + 1)
            visited[i] = 0


N = int(input())
a = [list(map(int, input().split()))for _ in range(N)]
ans = sys.maxsize
visited = [0] * N

for i in range(N):
    visited[i] = 1
    dfs(i, i, 0, 1)
    visited[i] = 0
print(ans)