import time
import numpy as np
from funcs import RandomArray
from funcs import WriteToFile
import funcs
#Insertion Sort
def InsertionSort(arr,start,end):       
    for i in range(start+1,end):
        temp = arr[i]
        j= i-1
        while j >= 0 and arr[j]>temp:          #Checking for smaller number
                arr[j+1] = arr[j]      
                j= j-1                            
        arr[j+1] = temp
    return arr

if __name__ == "__main__":
    n = 30000
    arr = RandomArray(n)                       #generating Random array 
    start_time = time.perf_counter()            
    final_arr = InsertionSort(arr,0, n)
    end_time = time.perf_counter()              
    runtime = end_time - start_time            #calculating runtime
    print("Runtime of InsertionSort : ",runtime)
    WriteToFile(final_arr, "SortedInsertionSort.csv")
    