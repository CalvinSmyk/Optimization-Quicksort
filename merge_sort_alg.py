import math  # to use math.inf



def merge_sort(subarray, counter):
    length_of_array = len(subarray)
    splitpoint = length_of_array // 2
    if length_of_array == 1:
        return subarray, counter
    left,counter  = merge_sort(subarray[:splitpoint], counter)
    right,counter = merge_sort(subarray[splitpoint:], counter)
    merged,counter = merge(left, right,counter)
    return merged,counter


def merge(left, right,counter):
    result = []
    l_idx,r_idx = 0,0
    try:
        while True:
            counter = counter + 1
            if left[l_idx] > right[r_idx]:
                result.append(right[r_idx])
                r_idx += 1
            else:
                result.append(left[l_idx])
                l_idx += 1
    except:
        return result + left[l_idx:] + right[r_idx:],counter

