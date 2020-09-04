
def linear_search(arr, target):
    x = len(arr)
    for i in range(0, x):
        if arr[i] == target:
            return i

    return -1   



def binary_search(arr, target):
    start = 0
    end = len(arr) -1 

    while end >= start:
        midindex = (start + end) // 2
        midval = arr[midindex]
        if target == midval:
            return midindex

        if target > midval:
            start = midindex + 1
        if target < midval:
            end = midindex - 1

    return -1  