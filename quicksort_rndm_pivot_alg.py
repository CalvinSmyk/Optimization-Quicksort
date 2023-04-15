import random

def quicksort(sorting_data, beginning, stop, counter):
    if (beginning < stop):
        pos, counter = randomized_partition(sorting_data, beginning, stop, counter)
        last_element = pos - 1
        next_element = pos +1
        counter = quicksort(sorting_data, beginning, last_element, counter)
        counter = quicksort(sorting_data, next_element, stop, counter)
    return counter


def randomized_partition(arr, start, stop,count):
    random_pivot_element = random.randrange(start, stop)
    arr[start], arr[random_pivot_element] = arr[random_pivot_element], arr[start]
    result = partition_step(arr, start, stop,count)
    return result


def partition_step(data_to_sort, beginning, stop, counter):
    pivot = beginning
    next_element = beginning + 1
    for j in range(beginning + 1, stop + 1):
        counter = counter + 1
        if data_to_sort[j] <= data_to_sort[pivot]:
            data_to_sort[next_element], data_to_sort[j] = data_to_sort[j], data_to_sort[next_element]
            next_element = next_element + 1
    data_to_sort[pivot], data_to_sort[next_element - 1] = \
        data_to_sort[next_element - 1], data_to_sort[pivot]
    pivot = next_element - 1
    return pivot, counter