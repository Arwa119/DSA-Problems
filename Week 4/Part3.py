#counting Sort

def CountingSort(arr):
    n = len(arr)
    Min = min(arr)
    shift = -Min 
    arr = [x + shift for x in arr]
    Max = max(arr)
    count = [0]*(Max+1)
    for i in range(n):
        count[arr[i]]+=1
    for i in range(Max+1):
        if i!=0:
            count[i]+=count[i-1]    
    sorted_a = [0]*n
    i = n-1
    while i>=0:
        indx = count[arr[i]]-1
        count[arr[i]]-=1
        sorted_a[indx] = arr[i]
        i-=1
    sorted_a = [x - shift for x in sorted_a]    
    for i in range(n):
        arr[i]=sorted_a[i]   
    return arr        


#radix sort

def RadixSort(arr):
    max_len = len(str(max(arr)))
    padded_arr = [str(num).zfill(max_len) for num in arr]
    for digit in range(max_len):
        padded_arr = CountingSort_R(padded_arr,digit)
    sorted_arr = [int(num) for num in padded_arr]    
    return sorted_arr


#Bucket sort 

def bucketSort(arr):
    n = len(arr)
    buckets = [[]for i in range(n)]
    sorted_list = []   
    for i in range(n):
        temp = int(arr[i]*n)
        buckets[temp].append(arr[i])
    for i in range(n):
      buckets[i] = InsertionSort(buckets[i])
    for i in range(n):
         sorted_list.extend(buckets[i])
    return sorted_list        



#Helping functions

def CountingSort_R(arr,digit):
    n = len(arr)
    count = [0]*10
    for i in range(n):
        indx = int(arr[i][-(digit+1)])
        count[indx]+=1
    for i in range(1,10):
        count[i]+=count[i-1]    
    sorted_a = ['']*n
    i = n-1
    while i>=0:
        indx = int(arr[i][-(digit+1)])
        count[indx]-=1
        sorted_a[count[indx]] = arr[i]
        i-=1  
    for i in range(n):
        arr[i]= sorted_a[i]   
    return arr  


def InsertionSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


if __name__ =="__main__":    
    arr_c = [-5, -10, 0, -3, 8, 5,  -1, 10]
    arr_r = [110, 45, 65,50, 90,602, 24, 2, 66]  
    arr_b = [0.897, 0.565, 0.656,0.1234, 0.665, 0.3434] 
    print(CountingSort(arr_c))
    print(RadixSort(arr_r))
    print(bucketSort(arr_b))



