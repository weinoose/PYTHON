def binary_search(data, value):
    n = len(data)
    left = 0
    right = n - 1
    while left <= right:
        middle = (left + right) // 2
        if value < data[middle]:
            right = middle - 1
        elif value > data[middle]:
            left = middle + 1
        else:
            return middle
    raise ValueError('Value is not in the list')

if __name__ == '__main__':
    try:
        n = 10
        value_to_look_for = 42500
        data = range(1, n)
        binary_search(data, value_to_look_for)
    except ValueError:
        print("Value is not in data")