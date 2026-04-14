array = [1, 5, 9, 3, 6, 2, 4, 8, 7, 0]


def merge_sort(array):
    if len(array) < 2:
        return array
    
    mid_point = len(array) // 2
    head = array[:mid_point]
    tail = array[mid_point:]
    
    head = merge_sort(head)
    tail = merge_sort(tail)              
    
    result = []
    
    while True:
        if len(tail) == 0:
            result.extend(head)
            break
        
        if len(head) == 0:
            result.extend(tail)
            break
        
        if head[0] > tail[0]:
            result.append(tail.pop(0))
        elif head[0] < tail[0]:
            result.append(head.pop(0))
        
    return result

print(merge_sort(array))