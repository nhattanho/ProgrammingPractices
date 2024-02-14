def bucket_sort(arr):
    max_value = max(arr)
    min_value = min(arr)
    range_arr = max_value - min_value + 1

    num_buckets = range_arr//len(arr) + 1
    
    buckets = []
    buckets = [[] for _ in range(0, num_buckets)]

    for i in arr:
        index = (i-min_value+1)//len(arr)
        buckets[index].append(i) # add single element

    res = []
    for bucket in buckets:
        res.extend(sorted(bucket)) # add elements into an array
    return res

my_array = [4, 2, 7, 1, 9, 5, 8, 4, 2]
sorted_array = bucket_sort(my_array)
print("Original Array:", my_array)
print("Sorted Array:", sorted_array)






