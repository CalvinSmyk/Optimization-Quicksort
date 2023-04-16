

def insertion_sort(data_array, counter):
    for index_one in range(1, len(data_array)):
        index_two = index_one
        while index_two > 0 and data_array[index_two - 1] > data_array[index_two]:
            data_array[index_two], data_array[index_two - 1] = data_array[index_two - 1], data_array[index_two]
            counter = counter + 1
            index_two -= 1
    return data_array, counter