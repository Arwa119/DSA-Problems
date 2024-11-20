# Problem 1
from random import randint
import random

def RandomArray(size):
    array = [randint(-15,15) for i in range(size)]
    return array

def WriteToFile(array,file_name):
    f = open(file=file_name, mode='w')
    for i in array:
        f.write(str(i) + "\n")
       
   
def ReadFromFile(file_name):
    file = open(file=file_name, mode="r")
    line = file.read()
    n_arr = []
    arr = line.split()
    for i in arr:
        n_arr.append(i)
    return n_arr   

def ReadFromFile_N(file_name):
    file = open(file=file_name, mode="r")
    line = file.read()
    n_arr = []
    arr = line.split()
    for i in arr:
        num = int(i)
        n_arr.append(num)
    return n_arr         

def Shuffle_arr(arr):
    return (random.shuffle(arr))
   

def Merge(array, p, q, r):
    left = array[p:q + 1]
    right = array[q + 1:r + 1]
    
    i = j = 0
    k = p
    
    while i < len(left) and j < len(right):     #Merging until the size of two arrays is same
        if left[i] <= right[j]:
            array[k] = left[i]
            i += 1
        else:
            array[k] = right[j]
            j += 1
        k += 1
    
    while i < len(left):        # Copies the left arrays remaining elements
        array[k] = left[i]
        i += 1
        k += 1

    while j < len(right):       #Copies the right arrays remaining elements
        array[k] = right[j]
        j += 1
        k += 1
