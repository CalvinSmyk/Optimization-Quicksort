

def insertion_sort(arr,counter):
    for i in range(1, len(arr)):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            counter = counter + 1
            j -= 1
    return arr,counter