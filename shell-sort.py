array = [1, 5, 9, 3, 6, 2, 4, 8, 7, 0]

def shell_sort(arr):
    gap = len(arr) // 2
    
    while gap > 0:
        i = 0
        j = i + gap
        
        while j < len(arr):
            if arr[j] < arr[i]:
                arr[i], arr[j] = arr[j], arr[i]
                
            i += 1
            j += 1
            
        gap = gap // 2
    
    return arr

print(shell_sort(array))