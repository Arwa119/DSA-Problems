from Bubble import BubbleSort
from Insertion import InsertionSort
from MergeSort import MergeSort
from Selection import SelectionSort
from HybridMerge import HybridMergeSort
from funcs import WriteToFile,ReadFromFile_N,RandomArray,Merge
import time

def RunTime_Calculation():

    n_array = ReadFromFile_N("Nvalues.txt")
    Runtime = []

    for i in n_array:
        run = []
        run.append(i)

        arr = RandomArray(i)        #Random array generation

        #Insertion Sort
        start_time = time.perf_counter()
        final_array = InsertionSort(arr,0, i-1)
        end_time = time.perf_counter()
        runtime= end_time-start_time
        run.append(runtime)
        
        #MergeSort
        start_time = time.perf_counter()
        final_array = MergeSort(arr,0, i-1)
        end_time = time.perf_counter()
        runtime= end_time-start_time
        run.append(runtime)    

        #HybridMerge Sort
        start_time = time.perf_counter()
        final_array = HybridMergeSort(arr,0, i-1)
        end_time = time.perf_counter()
        runtime= end_time-start_time
        run.append(runtime)

        #Selection Sort
        start_time = time.perf_counter()
        final_array = SelectionSort(arr,0, i)
        end_time = time.perf_counter()
        runtime= end_time-start_time
        run.append(runtime)

        #Bubble Sort
        start_time = time.perf_counter()
        final_array = BubbleSort(arr,0, i-1)
        end_time = time.perf_counter()
        runtime= end_time-start_time
        run.append(runtime)

        Runtime.append(run)
        WriteToFile(Runtime, "RunTime.csv ")

if __name__ == "__main__":
    RunTime_Calculation()
    print("Results are saved in RunTime.txt file")       

        

