# 3.23 merge(병합) 정렬 파이썬 구현 코드

# def merge_sort(arr):
#     if len(arr) < 2:
#         return arr
    
#     mid = len(arr) // 2

#     low_arr = merge_sort(arr[:mid])
#     high_arr = merge_sort(arr[mid:])

#     merge_arr = []
#     l = h = 0
#     while l < len(low_arr) and h < len(high_arr):
#         if low_arr[l] < high_arr[h]:
#             merge_arr.append(low_arr[l])
#             l += 1
#         else:
#             merge_arr.append(high_arr[h])
#             h += 1
#     merge_arr += low_arr[l:]
#     merge_arr += high_arr[h:]
#     return merge_arr

# A = [21, 10, 12, 20, 25, 13 ,15 ,22]

# print(merge_sort(A))


# 힙 소트

# def heapify(unsorted, index, heap_size):
#   largest = index
#   left = 2 * index + 1
#   right = 2 * index + 2
  
#   if left < heap_size and unsorted[left] > unsorted[largest]:
#     largest = left
    
#   if right < heap_size and unsorted[right] > unsorted[largest]:
#     largest = right
    
#   if largest != index:
#     unsorted[largest], unsorted[index] = unsorted[index], unsorted[largest]
#     heapify(unsorted, largest, heap_size) # 필요가 없다. 어차피 자식이 있는 노드부터 시작

# def heap_sort(unsorted):
#   n = len(unsorted)
  
#   for i in range(n // 2 - 1, -1, -1):  # n//2-1 부터 -1전까지 역방향으로
#     heapify(unsorted, i, n)
    
#   for i in range(n - 1, 0, -1):
#     unsorted[0], unsorted[i] = unsorted[i], unsorted[0]
#     heapify(unsorted, 0, i)

#   return unsorted

# arr = [4,5,3,9,8,7]

# or 

# def heapify(unsorted, index, heap_size):
#     largest = index
#     left = 2 * index + 1
#     right = 2 * index + 2
    
#     if left < heap_size and unsorted[left] > unsorted[largest]:
#         largest = left
        
#     if right < heap_size and unsorted[right] > unsorted[largest]:
#         largest = right

#     if largest != index:    
#         swap(unsorted, largest, index)  
#         heapify(unsorted, largest, heap_size) 

# def swap(arr, a, b):
#     arr[a], arr[b] = arr[b], arr[a] 

# def heap_sort(unsorted):
#     n = len(unsorted)
    
#     for i in range(n//2, -1, -1): # i == 2 .. 1.. 0
#         heapify(unsorted, i, n)
        
#     for i in range(n - 1, 0, -1): # 5, 4, 3, 2, 1
#         swap(unsorted, 0, i)
#         heapify(unsorted, 0, i)

#     return unsorted

# A = [5,6,7,2,3,1]

# print(heap_sort(A))

# 해쉬 테이블 구현

# from __future__ import annotations
# from typing import Any, Type
# import hashlib

# class Node: 
#     """해시를 구성하는 노드"""

#     def __init__(self, key: Any, value: Any, next: Node) -> None:
#         self.key = key
#         self.value = value
#         self.next = next

# class ChainedHash:
#     """체인법으로 해시 클래스 구현"""

#     def __init__(self, capacity : int) -> None:
#         self.capacity = capacity
#         self.table = [None] * self.capacity

#     def hash_value(self, key : Any) -> int:
#         if isinstance(key, int):
#             return key % self.capacity
#         return(int(hashlib.sha256(str(key).encode()).hexdigest(), 16) % self.capacity)
# a = 1.2345

# print(type(str(a).encode()))

# print(int(hashlib.sha256(str(a).encode()).hexdigest(), 16))

# 퀵 정렬 구현

# def qsort(arr, start_idx, end_idx):
#     pivot = arr[(start_idx + end_idx) // 2]
#     pl = start_idx
#     pr = end_idx

#     while pl <= pr:
#         while arr[pl] < pivot:
#             pl += 1
#         while arr[pr] > pivot:
#             pr -= 1
#         if pl <= pr:
#             arr[pl], arr[pr] = arr[pr], arr[pl]
#             pl += 1
#             pr -= 1
#     if start_idx < pr:
#         qsort(arr, start_idx, pr)
#     if end_idx > pl:
#         qsort(arr, pl, end_idx)
#     return arr

# A = [3,5,1,2,7,6,4,8]

# print(qsort(A, 0, len(A)-1))
