from time import time
import insertion_sort_alg
import quicksort_alg
import median_of_three_alg
import access_file
import evaluation
import quicksort_rndm_pivot_alg

def hybrid_sort(data, counter):
    if len(data) <= 2500:
        # Use insertion sort for small arrays
        data, counter = insertion_sort_alg.insertion_sort(data, counter)
        return counter
    else:
        # Use quicksort for the rest
        counter = quicksort_rndm_pivot_alg.quicksort(data,0,len(data)-1,0)
        return counter


if __name__ == '__main__':
    results = {}
    for att in range(0,5):
        number_of_datapoints = [10,500,2500,10000,50000,100000,250000,500000,1000000]
        for idx,i in enumerate(number_of_datapoints):
            lecture_list = [7, 6, 3, 5, 1, 2, 4]
            data = access_file.read_list_from_file('datalists/{}_{}_datalist'.format(att,idx))
            size = len(data)
            t0 = time()
            count = hybrid_sort(data, 0)
            t1 = time()
            print("Datalength: {}, comparisions: {}, time: {}".format(len(data), count, t1 - t0))
            results['{}_with_{}'.format(att,i)] = {'length':len(data),'comparisions':count,'time':t1-t0}

    evaluation.evaluate(number_of_datapoints,results)