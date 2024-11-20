from funcs import WriteToFile,ReadFromFile,Shuffle_arr
from Insertion import InsertionSort
from MergeSort import MergeSort,Merge
import time

if __name__ == "__main__":
    words = ReadFromFile("words.txt")
    orinial =[]
                                    
    start_time = time.time()           #insertionSort on original Array
    InsertionSort(words, 0, len(words)-1)
    end_time = time.time()
    run_time = end_time - start_time
    orinial.append(run_time)
    
    start_time = time.time()            #MergeSort on original Array
    MergeSort(words, 0, len(words)-1)
    end_time = time.time()
    run_time = end_time - start_time
    orinial.append(run_time)
    
    Shuffle_arr(words)
    
    shuffled=[]

    start_time = time.perf_counter()            #InsertionSort on shuffled Array
    InsertionSort(words, 0, len(words)-1)
    end_time = time.perf_counter()
    run_time = end_time - start_time
    shuffled.append(run_time)
    
    start_time = time.perf_counter()             #MergeSort on shuffled Array
    MergeSort(words, 0, len(words)-1)
    end_time = time.perf_counter()
    run_time = end_time - start_time
    shuffled.append(run_time)
    
    print("RunTime on orginal array:  ",orinial)
    print("RunTime on shuffled array:  ",shuffled)