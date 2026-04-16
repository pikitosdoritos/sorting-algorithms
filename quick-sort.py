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

def quick_sort_youtube(array, start=0, end=len(array) - 1):
    if end - start < 2:
        return array
    
    i = start
    j = end - 1 
    
    pivot = array[end]
    
    while pivot >= array[i] and i < end:
        i += 1
        
    while pivot <= array[j] and j > start:
        j -= 1
        
    if i > j:        
        array[len(array) - 1], array[i] = array[i], pivot
        
        quick_sort_youtube(array, start, i - 1)
        quick_sort_youtube(array, i + 1, end)
        
        return array
    
    array[i], array[j] = array[j], array[i]

start = time.time() 
 
for _ in range(100):
    quick_sort(array)

print(time.time() - start)

start = time.time() 
 
for _ in range(100):
    quick_sort_youtube(array)

print(time.time() - start)