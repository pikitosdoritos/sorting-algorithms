print("==" * 80)
print("Bubble Sort")
print("==" * 80)

products = [
    {
        "title": "Apple Watch",
        "price": 300.00,
        "in_storage": 100
    },
    {
        "title": "iPhone 12",
        "price": 599.00,
        "in_storage": 200
    },
    {
        "title": "MacBook Air",
        "price": 999.00,
        "in_storage": 50
    },
    {
        "title": "AirPods Pro",
        "price": 249.00,
        "in_storage": 150
    }
]
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


print(sort(products, lambda a, b: a["price"] > b["price"]))
print(sort(products, lambda a, b: a["in_storage"] > b["in_storage"]))
