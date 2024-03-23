'''
Best Case: O(n + k) where n is the number of elements in the 
input array and k is the range of input.<=> max - min + 1
Average Case: O(n + k)
Worst Case: O(n + k)

Space complexity: O(k)
'''
def counting_sort(arr):
    # find max value
    max_val = max(arr)
    min_val = min(arr)

    temp_size = (max_val - min_val) + 1

    # initalize a count_arr to the size of the input arr + 1
    count_arr = [0] * (temp_size)

    # Set count_arr[i] to equal the number of elements equal to i
    for i in range(len(arr)):
        index = arr[i] - min_val
        count_arr[index] += 1

    temp_arr = [0] * (temp_size)

    # Set temp_arr[i] to equal the number of elements less than or equal to i
    for i in range(1, temp_size):
        temp_arr[i] = (count_arr[i] + count_arr[i - 1])

    # create sorted array
    sorted_arr = []

    # iterate over count array
    for i in range(min_val, max_val + 1):
        # check if value is in array
        if count_arr[i - min_val] > 0:
            # continue appending if element appears more than once
            while count_arr[i - min_val] > 0:
                sorted_arr.append(i)
                count_arr[i - min_val] -= 1

    return sorted_arr

def optimize_counting_sort(arr):
    # find max value
    max_val = max(arr)
    min_val = min(arr)

    temp_size = (max_val - min_val) + 1

    # initalize a count_arr to the size of the input arr + 1
    count_arr = [0] * (temp_size)

    # Set count_arr[i] to equal the number of elements equal to i
    for i in range(len(arr)):
        index = arr[i] - min_val
        count_arr[index] += 1

    # max position for each value
    for i in range(1, temp_size):
        count_arr[i] += count_arr[i-1]

    result = [0]*len(arr)

    for i in range(len(arr)-1, -1, -1):
        index = arr[i] - min_val
        pos = count_arr[index]-1
        result[pos] = arr[i]
        count_arr[index] -= 1

    return result

arr = [25, 12, 6, 10, 40, 28, 70]
res = optimize_counting_sort(arr)
print(res)