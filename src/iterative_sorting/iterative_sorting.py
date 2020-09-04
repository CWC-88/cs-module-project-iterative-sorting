

def selection_sort(arr):
    for i in range(0, len(arr) - 1):
        cur_index = i
        smallest_index = cur_index

        for checked in range(cur_index + 1, len(arr)):
            if arr[checked] < arr[smallest_index]:
                smallest_index = checked
 
        arr[smallest_index], arr[cur_index] = arr[cur_index], arr[smallest_index]

    return arr



def bubble_sort(arr):
    length = len(arr)

    for i in range(length-1):
        for checked in range(0, length-i-1):
            if arr[checked] > arr[checked+1]:
                arr[checked], arr[checked+1] = arr[checked+1], arr[checked]

    return arr


'''
STRETCH: implement the Count Sort function below
Counting sort is a sorting algorithm that works on a set of data where
we specifically know the maximum value that can exist in that set of
data. The idea behind this algorithm then is that we can create "buckets"
from 0 up to the max value. This is most easily done by initializing an
array of 0s whose length is the max value + 1 (why do we need this "+ 1"?).
Each buckets[i] then is responsible for keeping track of how many times 
we've seen `i` in the input set of data as we iterate through it.
Once we know exactly how many times each piece of data in the input set
showed up, we can construct a sorted set of the input data from the 
buckets. 
What is the time and space complexity of the counting sort algorithm?
'''
def counting_sort(arr, maximum=None):
    # Your code here


    return arr