array = [1, 5, 9, 3, 6, 2, 4, 8, 7, 0]

def merge_sort(array):
    mid_point = len(array) // 2
    arr1 = array[:mid_point]
    arr2 = array[mid_point:]
    
    return arr1, arr2

print(merge_sort(array))