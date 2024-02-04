# A Max-Heap is defined as a type of Heap Data Structure in
# which each internal node is greater than or equal to its children. 
# A[(i-1)/2] returns the parent node
# A[2i + 1] returns the left child node
# A[2i + 2] returns the right child node

#       [0] [1] [2] [3] [4] 
array = [4,  5,  6, 10,  1]

#             4      (1)         4     (2)       10               10    
#          5     6   ==>     10     6  ==>    4      6   &&    5      6   
#      10     1           5      1         5     1           4    1   

def heapify(arr, n, i):
    root = i
    left = 2*i+1
    right = 2*i+2
    print(f'i: {i}')

    if left < n and arr[root] < arr[left]:
        root = left # update the root pointer
    if right < n and arr[root] < arr[right]:
        root = right # update the root pointer
    if root != i:
        # updated the new root value, but kept
        # the root pointer to continue updating
        # for the childs
        arr[i], arr[root] = arr[root], arr[i]
        heapify(arr, n, root)


def build_max_heap(arr):
    n = len(arr)
    for i in range(n//2-1, -1, -1): # round floor
        heapify(arr, n, i)

build_max_heap(array)
for i in range(len(array)):
    print(f'{array[i]}', end=' ')