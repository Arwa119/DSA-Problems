import numpy as np
from funcs import RandomArray
from funcs import WriteToFile
import time
import funcs
# Bubble sort
def BubbleSort(array,start,end):
    
    for i in range(start, end-1):
        for j in range(start,end-1-i):
            if array[j]>array[j+1]:       #Checking smaller values
                array[j], array[j+1] = array[j+1], array[j]     #Swapping of elements
    return array            


if __name__ == "__main__":
    n = 30000
    arr = RandomArray(n)    #Random array generation
    start_time = time.perf_counter()        
    final_arr = BubbleSort(arr,0, n)
    end_time = time.perf_counter()         
    runtime= end_time-start_time    #Runtime Calculation
    print("Runtime of Bubble Sort : ",runtime)
    WriteToFile(final_arr,"SortedBubbleSort.csv")   #writing to file
 