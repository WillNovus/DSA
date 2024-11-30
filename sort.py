'''Sorting Algorithms'''

def bubble_sort(arr):
    '''Bubble Sort Algorithm'''
    n = len(arr)
    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] =  arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break

def insertion_sort(arr):
    '''Insertion Sort Algorithm'''
    n = len(arr)
    for i in range(n):
        current_element = arr[i]
        j = i - 1
        while j >= 0 and current_element < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current_element

def selection_sort(arr):
    '''Selection Sort Algorithm'''
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]

def merge(arr, left_half, right_half):
    '''Helper function for merge sort algorithm'''
    i = j = k = 0

    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k] = left_half[i]
            i += 1
        else:
            arr[k] = right_half[i]
            j += 1
        
        k += 1

    while i < left_half[i]:
        arr[k] = left_half[i]
        i += 1
        k += 1

    while j < right_half[j]:
        arr[k] = right_half[j]
        j += 1
        k += 1


def merge_sort(arr):
    '''Merge Sort Algorithm'''
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        #Recursive call to the left and right halves.  
        merge_sort(left_half)
        merge_sort(right_half)

        #Merge the two sorted halves. 
        merge(arr, left_half, right_half)
