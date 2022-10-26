def linear_search(data, value):
    for index in range(len(data)):
        if value == data[index]:
            return index
    raise ValueError('Value not found in the list')

if __name__ == '__main__':
    try:
        n = 10
        value_to_look_for = 42500
        data = range(1, n)
        linear_search(data, value_to_look_for)
    except ValueError:
        print("Value is not in data")