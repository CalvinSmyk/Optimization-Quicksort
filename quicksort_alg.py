

def partition_step(sorting_data, start, end, counter):
    position = start
    for i in range(start, end):
        counter += 1
        if sorting_data[i] < sorting_data[end]:
            sorting_data[i], sorting_data[position] = sorting_data[position], sorting_data[i]
            position += 1
    sorting_data[position], sorting_data[end] = sorting_data[end], sorting_data[position]
    return position, counter

def quicksort_algorithm(sorting_data_list, beginning, end, counter):
    try:
        if beginning < end:
            pos, counter = partition_step(sorting_data_list, beginning, end, counter)
            counter = quicksort_algorithm(sorting_data_list, beginning, pos - 1, counter)
            counter = quicksort_algorithm(sorting_data_list, pos + 1, end, counter)
        return counter
    except RecursionError:
        print('Caught Recursion Error with datalength: {}'.format(len(sorting_data_list)))
        exit()
