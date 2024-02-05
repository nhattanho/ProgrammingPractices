# A Max-Heap is defined as a type of Heap Data Structure completed binary tree in
# which each internal node is greater than or equal to its children. 
# A[(i-1)/2] returns the parent node
# A[2i + 1] returns the left child node
# A[2i + 2] returns the right child node
# Go from bottom to the top of the tree

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

# A Min-Heap is defined as a type of Heap Data Structure completed binary tree in
# which each internal node is less than or equal to its children. 
# A[(i-1)/2] returns the parent node
# A[2i + 1] returns the left child node
# A[2i + 2] returns the right child node
# Go from bottom to the top of the tree
def min_heapify(arr, n, i):
    root = i
    left = 2*i+1
    right = 2*i+2

    if left < n and arr[root] > arr[left]:
        root = left
    if right < n and arr[root] > arr[right]:
        root = right
    
    if root != i:
        arr[root], arr[i] = arr[i], arr[root]
        min_heapify(arr, n, root)

def build_min_heap(arr):
    n = len(arr)
    for i in range(n//2-1, -1, -1):
        min_heapify(arr, n, i)

build_min_heap(array)
for i in range(len(array)):
    print(f'{array[i]}', end=' ')


# Insert a new element in the max/min heap => added to the bottom left of the tree
#(or at the end of the array ensuring to keep the complete tree)
# then need to go upward and compare with its parent => time complexity will
# be equal the height of the tree => n is number of node => height = O(logn)
    

# If build the max/min heap from the empty array, we need to add each element into
# an array => will take n time. Each time to add a element, we also need to adjust
# to keep the max heap be correct, and each time of adjusting is move up to the tree
# that gonna take log(n) = height of the current tre. Totally, the time complexity
# for this case is O(nlogn)
    
# When we have already an max heap array. To sort the arr, we need to swap the first
# element to the end, since it is the maximum number. Then continue keeping the max heap
# for the array with out the current last one => need to adjust that takes O(logn)