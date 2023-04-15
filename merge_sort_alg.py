import math  # to use math.inf


"""def mergeSort(arr,counter):
    if len(arr) > 1:

        # Create sub_array2 ← A[start..mid] and sub_array2 ← A[mid+1..end]
        mid = len(arr) // 2
        sub_array1 = arr[:mid]
        sub_array2 = arr[mid:]

        # Sort the two halves
        counter = mergeSort(sub_array1,counter)
        counter = mergeSort(sub_array2,counter)

        # Initial values for pointers that we use to keep track of where we are in each array
        i = j = k = 0

        # Until we reach the end of either start or end, pick larger among
        # elements start and end and place them in the correct position in the sorted array
        while i < len(sub_array1) and j < len(sub_array2):
            if sub_array1[i] < sub_array2[j]:
                counter = counter +1
                arr[k] = sub_array1[i]
                i += 1
            else:
                counter = counter + 1
                arr[k] = sub_array2[j]
                j += 1
            k += 1

        # When all elements are traversed in either arr1 or arr2,
        # pick up the remaining elements and put in sorted array
        while i < len(sub_array1):
            counter = counter + 1
            arr[k] = sub_array1[i]
            i += 1
            k += 1

        while j < len(sub_array2):
            counter = counter + 1
            arr[k] = sub_array2[j]
            j += 1
            k += 1
    return counter"""



"""def merge_lists(left_sublist,right_sublist,counter):
    i,j = 0,0
    result = []
    #iterate through both left and right sublist
    while i<len(left_sublist) and j<len(right_sublist):
    #if left value is lower than right then append it to the result
        if left_sublist[i] <= right_sublist[j]:
            counter = counter +1
            result.append(left_sublist[i])
            i += 1
        else:
            #if right value is lower than left then append it to the result
            counter = counter + 1
            result.append(right_sublist[j])
            j += 1
    #concatenate the rest of the left and right sublist
    result += left_sublist[i:]
    result += right_sublist[j:]
    #return the result
    return result,counter

def merge_sort(input_list,counter):
    #if list contains only 1 element return it
    if len(input_list) <= 1:
        return input_list,counter
    else:
        #split the lists into two sublists and recursively split sublists
        midpoint = int(len(input_list)/2)
        left_sublist,counter = merge_sort(input_list[:midpoint],counter)
        right_sublist,counter = merge_sort(input_list[midpoint:],counter)
        #return the merged list using the merge_list function above
        merged_list,counter = merge_lists(left_sublist,right_sublist,counter)
        return merged_list,counter"""


def merge_sort(seq,counter):
    if len(seq) == 1:
        return seq,counter
    left,counter  = merge_sort(seq[:len(seq) // 2],counter)
    right,counter = merge_sort(seq[len(seq) // 2:],counter)
    merged,counter = merge(left, right,counter)
    return merged,counter


def merge(left, right,counter):
    result = []
    left_count = 0
    right_count = 0
    try:
        while True:
            counter = counter + 1
            if left[left_count] > right[right_count]:
                result.append(right[right_count])
                right_count += 1
            else:
                result.append(left[left_count])
                left_count += 1
    except:
        return result + left[left_count:] + right[right_count:],counter

