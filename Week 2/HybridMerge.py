from funcs import RandomArray
from Insertion import InsertionSort
from funcs import WriteToFile
import time
import funcs

def HybridMergeSort(array, start, end):
    n = 10  
    if start < end:  
        if (end - start + 1) > n:  
            mid = (start + end) // 2  # Calculate mid-point
            HybridMergeSort(array, start, mid) 
            HybridMergeSort(array, mid + 1, end)  
            funcs.Merge(array, start, mid, end)  # Merge both halves
        else:
            InsertionSort(array, start, end + 1)  # Sort small subarrays using insertion sort
    return array




if __name__ == "__main__":    
    n = 30000
    arr = RandomArray(n)                              #Random array generation
    start_time = time.perf_counter()                 
    final_arr = HybridMergeSort(arr,0, n-1)
    end_time = time.perf_counter()                    
    runtime = end_time - start_time                  #Runtime Calculation
    print("Runtime of HybridMergeSort : ",runtime)  
    WriteToFile(final_arr,"SortedHybridSort.csv")    #writing to file
   