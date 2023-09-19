import random

from help_sorted import partition, marge, get_max_min


def counting_sort(unsorted_list):
    min, max = get_max_min(unsorted_list)
    arr = [0 for i in range(max - min + 1)]
    for call in unsorted_list:
        arr[call - min] += 1
    arr_return = []
    for index in range(len(arr)):
        call = arr[index]
        if call != 0:
            arr_return.extend([index + min for i in range(call)])
    return arr_return


def quick_sort(unsorted_list, start, end):
    if end >= len(unsorted_list):
        end = len(unsorted_list) - 1
    if start < end:
        x = partition(unsorted_list, start, end)
        quick_sort(unsorted_list, x + 1, end)
        quick_sort(unsorted_list, start, x - 1)


def bubble_sort(unsorted_list):
    for i in unsorted_list:
        for index in range(len(unsorted_list)):
            if unsorted_list[index] > unsorted_list[index + 1]:
                unsorted_list[index], unsorted_list[index + 1] = unsorted_list[index + 1] > unsorted_list[index]
    return unsorted_list


def marge_sort(unsorted_list, start, end):
    if end >= len(unsorted_list):
        end = len(unsorted_list) - 1

    middle = start + (end - start) // 2
    arrA, arrB = unsorted_list[start:middle], unsorted_list[start:middle + 1]
    if start < end:
        arrA = marge_sort(unsorted_list, start, middle)
        arrB = marge_sort(unsorted_list, middle + 1, end)
    return marge(arrA, arrB)


def radix_sort(unsorted_list):
    min, max = get_max_min(unsorted_list)
    new_arr = []
    for index in range(1, len(str(max)) + 1):
        unsorted_list = sorted_by_index(unsorted_list, index)
        new_arr = unsorted_list
    return new_arr


def sorted_by(fun, unsorted_list):
    return fun(unsorted_list)


def sorted_by_index(unsorted_list, ind, bace=10):
    """ """
    arr = [0 for _ in range(bace)]
    for val in unsorted_list:
        arr[module_by_base(bace, ind, val)] += 1
    for index in range(1, len(arr)):
        arr[index] += arr[index - 1]
    arr_return = [0 for _ in range(len(unsorted_list))]
    for index in range(len(unsorted_list) - 1, -1, -1):
        val = unsorted_list[index]
        a = arr[module_by_base(bace, ind, val)] - 1
        arr_return[a] = val
        arr[module_by_base(bace, ind, val)] -= 1

    return arr_return


def module_by_base(bace, ind, val):
    return (val % bace ** ind) // bace ** (ind - 1)


lst = [5, 4, 53, 61, 69, 6, 53, 0, 0, 0, 53, 8, 10]
lstd = [5, 3, 5, 5, 6, 0]
ls = [0, 1, 0, 1, 3, 3, 6]

random_list = [random.randint(0, 100) for _ in range(15)]

lst.extend(lstd)
if __name__ == '__main__':
    # print(random_list)
    a = sorted_by_index(random_list, 1)
    # print(a)
    # print(sorted_by_index(a, 2))
    # print(random_list)
    b = radix_sort(random_list)
    print(b)
