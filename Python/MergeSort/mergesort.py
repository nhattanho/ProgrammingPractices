'''
Time Complexity: O(nlogn)

+ Divide Step: Dividing the list into halves at each level of recursion takes O(log n) time, 
where n is the number of elements in the list.
+ Merge Step: Merging two sorted sub-lists into a single sorted list takes O(n) time, 
where n is the total number of elements in the two sub-lists.

Space Complexity: O(n) -  used for merge array + O(logn) - used for recursive on stack => finally: O(n)
    '''
def merge_sort(arr):
    len_arr = len(arr)
    if len_arr > 1:
        mid = len_arr//2
        Left = arr[:mid]
        Right = arr[mid:]
        merge_sort(Left)
        merge_sort(Right)

        l = r = i = 0
        while l < len(Left) and r < len(Right):
            if Left[l] > Right[r]:
                arr[i] = Right[r]
                r+=1
            elif Left[l] <= Right[r]:
                arr[i] = Left[l]
                l+=1
            i+=1
        
        while l < len(Left):
            arr[i] = Left[l]
            l+=1
            i+=1
        while r < len(Right):
            arr[i] = Right[r]
            r+=1
            i+=1
        
arr = [25, 12, 6, 10, 40, 28, 70, 34]
#arr = [25, 12]
merge_sort(arr)
print(arr)