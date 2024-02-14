# Time Complexity: O(nlogn)
# Space Complexity: O(1)

''' Time Complexity
Best Case: O(n log n)
Average Case: O(n log n)
Worst Case: O(n log n)
'''
# O(logn) - adjust value to keep maxheap
# Went down the tree from i position 
# <=> height of the tree
def max_heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[largest] < arr[left]:
        largest = left
    if right < n and arr[largest] < arr[right]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)

# O(nlogn)
def build_max_heap(arr):
    n = len(arr)
    for i in range(n//2-1, -1, -1):
        max_heapify(arr, n, i)

# 2*O(nlogn) <=> O(nlogn)
def heap_sort(arr):
    n = len(arr)
    build_max_heap(arr) #O(nlogn)

    #O(nlogn)
    for i in range(n-1, 0,-1):
        arr[i], arr[0] = arr[0], arr[i] #n
        max_heapify(arr,i,0) #O(logn)