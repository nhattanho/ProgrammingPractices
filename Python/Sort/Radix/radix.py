################### Radix Sort #######################
# Time Complexity: O(k*n), where k is the number of digits in the largest number.
# Space complexity: O(n)
'''
Best Case: O(nk)
Average Case: O(nk)
Worst Case: O(nk)
'''

def counting_sort_helps_radix(arr, exp):
    arr_len = len(arr)
    # declare the output array
    output = [0] * (arr_len)
    # initialize array having 0
    count = [0] * (10) # stored the occurrence of digit

    # find min_val
    min_val = min(arr)

    # Store count of occurrences in count[]
    for i in range(0, arr_len):
        index = arr[i] // exp
        modulo = index % 10
        count[modulo] += 1

    # Get actual position for each digit
    # digit     [0] [1] [2] [3] [4] [5]      position [0] [1] [2] [3] [4] [5] [6] [7] [8] [9]
    # freq       2   1   3   1   2   1   <=> digit     0   0   1   2   2   2   3   4   4   5 
    # value 0 appears 2 times, 1 is 1 time, 2 is 3 times, 3 is 1 times, 4 is 2 times, 5 is 1 time
    # the max pos of 1 is 2 + 1 = 3 => index is 3-1 = 2
    # the max pos of 2 is 2+1+3 = 6 => index is 6-1 = 5 and so on
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build the output array
    # can go from the left to right,
    # but the direction from right to left
    # helps to keep the correct original order
    i = arr_len - 1
    while i >= 0:
        index = arr[i] // exp
        digit = index % 10
        output[count[digit] - 1] = arr[i]
        count[digit] -= 1
        i -= 1

    # Get the sorted array
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]

    return arr


def radix_sort(arr):
    # Find the maximum number
    max_num = max(arr)
    # determine if there are negative numbers in unsorted array
    min_num = min(arr)
    exp = 1
    # create sorted arr array
    sorted_arr = []
    # if there are negative values, split the array into positive and negative
    if min_num < 0:
        pos_unsorted_arr = []
        neg_unsorted_arr = []
        sorted_pos_arr = []
        sorted_neg_arr = []

        for i in arr:
            if i < 0:
                neg_unsorted_arr.append(i)
            else:
                pos_unsorted_arr.append(i)

        # convert negative elements to positive
        for i in range(len(neg_unsorted_arr)):
            neg_unsorted_arr[i] = neg_unsorted_arr[i] * (-1)

        # Find max value of the negative unsorted array
        max_num_negative = max(neg_unsorted_arr)
        # sort negative elements

        # O(d*n) with d is the number digit of max number
        while max_num_negative // exp >= 1: # O(d)
            sorted_neg_arr = counting_sort_helps_radix(neg_unsorted_arr, exp) # O(n)
            exp *= 10

        # Reverse the array and convert it back to negative
        sorted_neg_arr.reverse()
        for i in range(len(sorted_neg_arr)):
            sorted_neg_arr[i] = sorted_neg_arr[i] * (-1)

        # Reset the max number and exp for the unsorted positive array
        max_num = max(arr)
        exp = 1

        # sort positive array
        while max_num // exp >= 1:
            sorted_pos_arr = counting_sort_helps_radix(pos_unsorted_arr, exp)
            exp *= 10
        # concatenate the negative and positive sorted arrays
        sorted_arr = sorted_neg_arr + sorted_pos_arr
    else:
        while max_num // exp >= 1:
            sorted_arr = counting_sort_helps_radix(arr, exp)
            exp *= 10
    return sorted_arr

