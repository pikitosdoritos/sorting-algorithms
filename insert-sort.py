array = [3, 0, 1, 6, 9, 2, 4, 8, 5, 7]

def insert_sort(array):
    for i, item in enumerate(array):
        if i < len(array) - 1 and array[i+1] < item:
            array[i+1], array[i] = item, array[i+1]

            while True:
                if i == 0:
                    break
                if array[i] < array[i - 1]:
                    array[i], array[i - 1] = array[i - 1], array[i]
                    
                i -= 1
                

    return array              

print(insert_sort(array)) 