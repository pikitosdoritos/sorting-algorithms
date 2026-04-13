import time
import random

array = [random.randint(0, 1000) for _ in range(950)]

def quick_sort(array, start=0, end=len(array) - 1):
    i = start
    j = end
    back = True
    
    if start >= end:
        return array
    
    while i < j:
        if array[i] > array[j]:
            x = array[i]
            array[i] = array[j]
            array[j] = x
            back = not back
            
        else:
            if back:
                j -= 1
            else:
                i += 1
            
    if i - start > 1:    
        quick_sort(array, start, i-1)
    if end - i > 1:
        quick_sort(array, i+1, end)

    return array

def quick_sort_hoare(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    if left >= right:
        return arr

    pivot = arr[(left + right) // 2]

    i = left
    j = right

    while True:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1

        if i >= j:
            break

        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1  

    quick_sort_hoare(arr, left, j)
    quick_sort_hoare(arr, j + 1, right)

    return arr

start = time.time() 
 
for _ in range(100):
    quick_sort(array)

print(time.time() - start)

start = time.time() 
 
for _ in range(100):
    quick_sort_hoare(array)

print(time.time() - start)