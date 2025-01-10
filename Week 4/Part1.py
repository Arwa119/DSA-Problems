def Partition(Arr, l, h):
    pivot = Arr[h]
    i = l - 1
    for j in range(l, h):
        if Arr[j] <= pivot:
            i += 1
            Arr[i], Arr[j] = Arr[j], Arr[i]
    Arr[i + 1], Arr[h] = Arr[h], Arr[i + 1]
    return i + 1

def QUICKSORT(Arr, l, h):
    if l < h:
        p = Partition(Arr, l, h)
        QUICKSORT(Arr, l, p - 1)
        QUICKSORT(Arr, p + 1, h)
    return Arr

arr = [-21,98,3,0,0,2,4,-21]
print(QUICKSORT(arr,0,7))