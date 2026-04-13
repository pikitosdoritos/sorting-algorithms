array = [2, 4, 1, 98, 34, 3, 88]

def quick_sort(array, start=0, end=len(array) - 1):
    i = start
    j = end
    back = True
    
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
    
print(quick_sort(array))