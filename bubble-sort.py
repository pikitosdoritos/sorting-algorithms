print("==" * 80)
print("Bubble Sort")
print("==" * 80)


array = [2, 4, 1, 98, 34, 3, 88]


def sort(array):
    for _ in range(len(array)):
        for i, item in enumerate(array):
            if i < len(array) - 1 and item > array[i+1]:
                array[i] = array[i + 1]
                array[i + 1] = item

    return array

print(sort(array))