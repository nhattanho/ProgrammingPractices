################### Quick Sort #######################
'''
devide and conquer
Time Complexity: O(nlogn) - worst case in case of having sorted list already: O(n^2)
https://www.youtube.com/watch?v=-qOVVRIZzao
Space Complexity: O(logn) -> O(n)
'''
def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def new_partition(arr, low, high):
    pi = low
    while low <= high:
        if arr[low] <= arr[pi]:
            low += 1
        else:
            arr[low], arr[high] = arr[high], arr[low]
            high -= 1
    arr[pi], arr[low-1] = arr[low-1], arr[pi]
    return low-1


def run_quick_sort(arr, low, high):
    if low < high:
        pi = new_partition(arr, low, high)
        run_quick_sort(arr, low,
                       pi - 1)  # sorting everything to the left of the
        # pivot
        run_quick_sort(arr, pi + 1,
                       high)  # sorting everything to the right of the
        # pivot


def quick_sort(arr):
    run_quick_sort(arr, 0, len(arr) - 1)
    return arr

arr = [25, 12, 6, 10, 40, 28, 70, 34]
arr = [25, 12]
res = quick_sort(arr)
print(res)