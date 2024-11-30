'''Searching Algorithms'''


def linear_search(arr, target):
    '''This is a linear search algorithm.'''
    for i in arr:
        if arr[i] == target:
        #target found return index.
            return i
    return -1


def binary_search(arr, target):
    '''This is a binary search algorithm.'''
    low, high = 0, len(arr)
    while low <= high:
        mid = low + high // 2
        if arr[mid] == target:
            return target
        elif arr[mid] > target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

