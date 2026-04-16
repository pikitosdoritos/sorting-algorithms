array = [3, 0, 1, 6, 9, 2, 4, 8, 5, 7]

def selection_sort(arr):
    k = 0
    
    while k < len(arr) - 1:
        i = k 
        j = k + 1
        
        while j < len(arr):
            if  arr[j] < arr[i]:
                i = j
                
            j += 1
                           
            
        arr[k], arr[i] = arr[i], arr[k]
        
        k += 1
    
    return arr

print(selection_sort(array))           