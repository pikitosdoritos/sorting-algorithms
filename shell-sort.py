array = [1, 5, 9, 3, 6, 2, 4, 8, 7, 0]

def shell_sort(arr):
    gap = len(arr) // 2
    
    while gap > 0:
        i = 0
        j = i + gap
        
        while j < len(arr):
            k = j
            
            while k - gap >= 0 and arr[k] < arr[k - gap]:
                arr[k], arr[k - gap] = arr[k - gap], arr[k]
                k -= gap
                
            i += 1
            j += 1
            
        gap = gap // 2
    
    return arr

print(shell_sort(array))