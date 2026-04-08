print("==" * 80)
print("Bubble Sort")
print("==" * 80)


array = [2, 4, 1, 98, 34, 3, 88]

def compare_numbers(a, b):
    return a > b     

def sort(array, compare):
    attempts = 0
    for j in range(len(array)):
        is_sorted = True
        attempts += 1
        for i, item in enumerate(array):
            if i < len(array) - 1 - j and compare(item, array[i+1]):
                array[i] = array[i + 1]
                array[i + 1] = item
                is_sorted = False
                 
        if is_sorted:
            break
        
    print(attempts)
    return array


print(sort(array, compare_numbers))
