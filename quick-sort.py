array = [2, 4, 1, 98, 34, 3, 88]

def quick_sort(array, i=0, j=len(array) - 1):
    while i < j:
        if array[i] > array[j]:
            x = array[i]
            array[i] = array[j]
            array[j] = x
            i += 1
            
        else:
            j -= 1
            
    return array
    
print(quick_sort(array))