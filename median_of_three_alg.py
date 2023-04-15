def median(lst, i, j, k):
    if (lst[i] - lst[j]) * (lst[j] - lst[k]) >= 0:
        return j
    elif (lst[i] - lst[k]) * (lst[k] - lst[j]) >= 0:
        return k
    else:
        return i


def swap(lst, i, j,counter):
    lst[i], lst[j] = lst[j], lst[i]
    counter = counter +1
    return counter

def qsort_mo3(lst, l, u,counter):
    try:
        # use median-of-3 instead of randomization
        if l >= u:
            return counter
        mid = l + (u - l) // 2
        r = median(lst, l, mid, u)
        counter = swap(lst, l, r,counter)
        m = lst[l]
        i = l
        j = u + 1
        while True:
            while True:
                i += 1
                if i >= j or lst[i] >= m:
                    break
            while True:
                j -= 1
                if i >= j or lst[j] <= m:
                    break
            if i >= j:
                break
            counter = swap(lst, i, j,counter)

        counter = swap(lst, l, i-1,counter)

        counter = qsort_mo3(lst, l, i-2,counter)
        counter = qsort_mo3(lst, i, u,counter)
        return counter
    except RecursionError:
        print('Caught Recursion Error with datalength: {}'.format(len(lst)))
        exit()