import time


def measure_sort_time(sorting_function, arr):
    start = time.time()
    sorting_function(arr)
    if is_sorted(sorting_function(arr)) is True or is_sorted2(sorting_function(arr)) is True:
        print("Sorted")
    else:
        print("Not sorted")
    end = time.time()
    return end - start


def is_sorted(lst, key=lambda x: x):
    for i, el in enumerate(lst[1:]):
        if key(el) < key(lst[i]):
            return False
    return True


def is_sorted2(lst, key=lambda x: x):
    for i, el in enumerate(lst[1:]):
        if key(el) > key(lst[i]):
            return False
    return True


def first_sorting():
    return lambda l: sorted(l)


def second_sorting():
    return lambda l: sorted(l)[::-1]


if __name__ == '__main__':
    table1 = [20, 19, 17, 18, 13, 14, 15, 16, 12, 10, 11, 8, 9, 3, 1, 2, 4, 5, 6, 7]
    print(measure_sort_time(first_sorting(), table1))
    print(measure_sort_time(second_sorting(), table1))
