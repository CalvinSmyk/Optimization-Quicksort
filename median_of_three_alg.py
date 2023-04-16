def median(data_array, start, middle, end):
    if (data_array[start] - data_array[middle]) * (data_array[middle] - data_array[end]) >= 0:
        return middle
    elif (data_array[start] - data_array[end]) * (data_array[end] - data_array[middle]) >= 0:
        return end
    else:
        return start


def swap(data_array, first_elm, last_elm, counter):
    data_array[first_elm], data_array[last_elm] = data_array[last_elm], data_array[first_elm]
    counter = counter +1
    return counter

def qsort_mo3(data_array, beginning, end, counter):
    try:
        if beginning >= end:
            return counter
        mid = beginning + (end - beginning) // 2
        pivot = median(data_array, beginning, mid, end)
        counter = swap(data_array, beginning, pivot, counter)
        first_elm = data_array[beginning]
        limit = beginning
        end_place = end + 1
        while True:
            while True:
                limit += 1
                if limit >= end_place or data_array[limit] >= first_elm:
                    break
            while True:
                end_place -= 1
                if limit >= end_place or data_array[end_place] <= first_elm:
                    break
            if limit >= end_place:
                break
            counter = swap(data_array, limit, end_place, counter)

        counter = swap(data_array, beginning, limit - 1, counter)

        counter = qsort_mo3(data_array, beginning, limit - 2, counter)
        counter = qsort_mo3(data_array, limit, end, counter)
        return counter
    except RecursionError:
        print('Caught Recursion Error with datalength: {}'.format(len(data_array)))
        exit()