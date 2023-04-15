import access_file
from time import time
import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def evaluate(number_of_datapoints,results):
    averaged = list()
    for average in number_of_datapoints:
        entries = {k: v for k, v in results.items() if k.endswith('_{}'.format(average))}
        avg_x = sum([x['length'] for x in entries.values()]) / len(entries)
        avg_y = sum([x['comparisions'] for x in entries.values()]) / len(entries)
        avg_z = sum([x['time'] for x in entries.values()]) / len(entries)
        averaged.append([avg_x,avg_y,avg_z])
    x = [length for length,_,_ in averaged]
    y = [count for _,count,_ in averaged]
    z = [time for _,_,time in averaged]

    df = pd.DataFrame({'Datalength':x,'comparisions':y,'Time':z})
    print(df)

    plt.scatter(x,y)
    z1 = np.polyfit(x,y,1)
    p1 = np.poly1d(z1)
    plt.plot(x,p1(x),'r--')
    for i, sublist in enumerate(averaged):
        plt.text(sublist[0],sublist[1], '({}, {})'.format(sublist[0],sublist[1]))
    plt.xlabel('Datasetsize')
    plt.ylabel('Number of comparisions')
    plt.title('Plot1')

    plt.figure()
    plt.scatter(x, z)
    z2 = np.polyfit(x,z,1)
    p2 = np.poly1d(z2)
    plt.plot(x,p2(x),'g--')
    for i, sublist in enumerate(averaged):
        plt.text(sublist[0],sublist[2], '({}, {})'.format(sublist[0],sublist[2]))
    plt.xlabel('Datasetsize')
    plt.ylabel('Time taken')
    plt.title('Plot2')
    plt.show()