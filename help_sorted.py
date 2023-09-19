import sys


def partition(arr, start, end):
    pivot = arr[end]
    i = start - 1

    for j in range(start, end):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[end], arr[i + 1] = arr[i + 1], arr[end]
    return i + 1


def marge(arrA, arrB):
    max = 99999999999999
    new_arr = []
    j = 0
    k = 0
    arrA.append(max)
    arrB.append(max)
    for i in range(len(arrA) + len(arrB) - 2):
        if arrA[k] < arrB[j]:
            new_arr.append(arrA[k])
            k = k + 1
        else:
            new_arr.append(arrB[j])
            j = j + 1
    return new_arr


def get_max_min(unsorted_list):
    """:return min , max"""
    min, max = unsorted_list[0], unsorted_list[0]
    for call in unsorted_list:
        if call > max:
            max = call
        if call < min:
            min = call
    return min, max
