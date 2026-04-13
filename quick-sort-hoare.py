def quick_sort_hoare(arr, left=0, right=None):
    if right is None:
        right = len(arr) - 1

    if left >= right:
        return arr

    pivot = arr[(left + right) // 2]

    i = left
    j = right

    while True:
        while arr[i] < pivot:
            i += 1
        while arr[j] > pivot:
            j -= 1

        if i >= j:
            break

        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1  

    quick_sort_hoare(arr, left, j)
    quick_sort_hoare(arr, j + 1, right)

    return arr
