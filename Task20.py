import time


def measure_sort_time(sorting_function, arr):
    start = time.time()
    result = sorting_function(arr)
    end = time.time()
    if is_ascending(result) or is_descending(result):
        print("Sorted")
    return end - start


def is_sorted(elements, key=lambda x: x, reverse=False):
    order = lambda x, y: x <= y
    if reverse:
        order = lambda x, y: x >= y

    for idx in range(len(elements) - 1):
        x, y = elements[idx], elements[idx + 1]
        if not order(key(x), key(y)):
            return False
    return True


def is_ascending(elements):
    return is_sorted(elements)


def is_descending(elements):
    return is_sorted(elements, reverse=True)


def first_sorting():
    return lambda l: sorted(l)


def second_sorting():
    return lambda l: sorted(l)[::-1]


if __name__ == '__main__':
    table1 = [20, 19, 17, 18, 13, 14, 15, 16, 12, 10, 11, 8, 9, 3, 1, 2, 4, 5, 6, 7]
    print(measure_sort_time(first_sorting(), table1))
    print(measure_sort_time(second_sorting(), table1))
