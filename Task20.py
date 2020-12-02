import time


def measure_sort_time(sorting_function, arr):
    start = time.time()
    sorting_function(arr)
    number = 1
    if str(sorting_function).split(".")[0] == "<function first_sorting":
        for i in sorting_function(arr):
            if number == len(arr):
                break
            if i > sorting_function(arr)[number]:
                print("Not sorted")
                break
            number += 1
    if str(sorting_function).split(".")[0] == "<function second_sorting":
        for i in sorting_function(arr):
            if number == len(arr):
                break
            if i < sorting_function(arr)[number]:
                print("Not sorted")
                break
            number += 1
    end = time.time()
    return end - start


def first_sorting():
    return lambda l: sorted(l)


def second_sorting():
    return lambda l: sorted(l)[::-1]


if __name__ == '__main__':
    table1 = [20, 19, 17, 18, 13, 14, 15, 16, 12, 10, 11, 8, 9, 3, 1, 2, 4, 5, 6, 7]
    print(measure_sort_time(first_sorting(), table1))
    print(measure_sort_time(second_sorting(), table1))
