#mergeSort
from funcs import RandomArray
from funcs import WriteToFile
import time
import funcs
def MergeSort(array, start, end):
    if start < end:
        mid = (start + end) // 2  # Decide the midpoint
        MergeSort(array, start, mid)  # Recursive call 
        MergeSort(array, mid + 1, end) 
        funcs.Merge(array, start, mid, end)  # Merging
    return array




  
if __name__ == "__main__":
    n = 30000
    arr = RandomArray(n)    #Random array generation
    start_time = time.perf_counter()    
    final_arr = MergeSort(arr,0, n)
    end_time = time.perf_counter()      
    runtime = end_time - start_time          #Runtime Calculation
    print("Runtime of MergeSort : ",runtime)  
    WriteToFile(final_arr, "SortedMergeSort.csv")    #writing to file
    