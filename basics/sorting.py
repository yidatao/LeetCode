import heapq
def heapsort(array):
    res = []
    heapq.heapify(array)
    while len(array) > 0:
        x = heapq.heappop(array)
        res.append(x)
    return res

def bubblesort(array):
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]


def insertionsort(array):
    for i in range(1, len(array)):
        j = i
        while j > 0 and array[j-1] > array[j]:
            array[j-1], array[j] = array[j], array[j-1]
            j -= 1


def partition(array, low, high):
    index = (low + high) // 2
    pivot = array[index]
    while low < high:
        while array[low] < pivot:
            low += 1
        while array[high] > pivot:
            high -= 1
        if low < high:
            array[low],array[high] = array[high],array[low]
            low += 1
            high -= 1
    return index

def quicksort(array, low, high):
    if low < high:
        pivot = partition(array,low,high)
        quicksort(array,low,pivot-1)
        quicksort(array,pivot+1,high)

def mergesort(array):
    if len(array) == 1:
        return
    mid = len(array) // 2
    left = array[0:mid]
    right = array[mid:]

    mergesort(left)
    mergesort(right)

    #merge left and right parts
    i,j,k = 0,0,0
    while i<len(left) and j<len(right):
        if left[i]<right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1
    #deal with leftovers
    while i<len(left):
        array[k] = left[i]
        i += 1
        k += 1
    while j<len(right):
        array[k] = right[j]
        j += 1
        k += 1



array = [3,2,5,4,1,6,8,7]
print("heapsort:" + str(heapsort(array)))
array = [3,2,5,4,1,6,8,7]
bubblesort(array)
print("bubblesort:" + str(array))
array = [3,2,5,4,1,6,8,7]
insertionsort(array)
print("insertionsort:" + str(array))
array = [3,2,5,4,1,6,8,7]
quicksort(array,0,len(array)-1)
print("quicksort:" + str(array))
array = [3,2,5,4,1,6,8,7]
mergesort(array)
print("mergesort:" + str(array))