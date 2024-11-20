import time
import numpy as np
from funcs import RandomArray
from funcs import WriteToFile
import funcs

def SelectionSort(array,start,end):
    for i in range(start,end):
        min = i
        for j in range(i+1, end):
            if array[j]< array[min]:            #finding minimum index
                min = j                
        array[i],array[min]=array[min],array[i]        #swapping
    return array


if __name__ == "__main__":
    n = 30000
    arr = RandomArray(n)        #Random array generation
    start_time = time.perf_counter()           
    final_array = SelectionSort(arr,0, n)
    end_time = time.perf_counter()      
    runtime= end_time-start_time        #Runtime Calculation
    print("Runtime of Selection Sort : ",runtime)       

    WriteToFile(final_array,"SortedSelectionSort.csv")   #writing to file
  