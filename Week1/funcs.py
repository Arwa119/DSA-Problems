import numpy as np
# problem 1

x = [22,2,1,7,11,13,5,2,9]
def SearchA(Arr,x):
    ind = []
    for i in range(len(Arr)):
        if Arr[i]==x:
            ind.append(i)

    return ind
a = int(input("Enter a number: "))
print("Index: " , SearchA(x,a))

# Prblm 2
 
X = [1,2,2,5,7,9,11,13,22]

def SearchB(Arr, x):
    ind = []
    for i in range(len(Arr)):
        if Arr[i]==x:
            ind.append(i)
            if (i+1)<len(Arr) and Arr[i+1]!= x:
                    return ind
    return ind                         
# num = int(input("Enter a number: "))
print("Index: " , SearchB(X,22))


# Problem 3

def Minimum(Arr,starting ,ending):
    min = int(Arr[starting])
    ending +=1
    indx = starting
    for i in range(starting,ending):
        if min > Arr[i]:
            min = Arr[i]
            indx=i
    return indx

# Array = []
# n = int(input("Enter the number of indexes: "))
# for i in range(n):
#     a = int(input(f"Enter value for index {i}: "))
#     Array.append(a)
start = int(input("StartingIndex: "))
end = int(input("EndingIndex: "))    
# Hardcode 
Array =   [3,4,7,8,0,1,23,-2,-5]
print(Minimum(Array,start,end))

#problem 4
   

def Sort4(Arr):
    start = int(input("StartingIndex: "))
    end = int(input("EndingIndex: "))
    for i in range(len(Arr)):
        new = int(Minimum(Arr,start,end))
        prev = Arr[i]
        Arr[i] = Arr[new]
        Arr[new] = prev
        start += 1
    return Arr
print(Sort4(Array))        

#problem 5

def StringReverse(str,starting,ending):
    if starting>=ending:
        return "invalid starting"
    else:    
        new = str[starting:ending+1:1]
        return new[::-1]

s = "University of Engineering and Technology Lahore"
start = int(input("StartingIndex: "))
end = int(input("EndingIndex: "))
print(StringReverse(s,start,end))

#problem 6

def SumIterative(number):
    sum = 0 
    while number > 0:
        new = number%10
        sum += new 
        number //= 10
    return sum 
n = int(input("Enter a number: "))
print(SumIterative(n))    

def SumRecursive(number):
    sum = 0 
    if number==0:
        return sum
    else:
        new = number%10
        number = number//10
        sum = new + int(SumRecursive(number))  
        return sum  
print(SumRecursive(n))    

#problem 7

Mat = [[1,13,13],[5,11,6],[4,4,9]]

def ColumnwiseSum(mat):
    final = []
    for i in range(3):
        arr =[]
        Sum = 0
        for j in range(3):
            new = mat[j][i]
            arr.append(new)
        Sum = sum(arr)  
        final.append(Sum)     
    return final

#RowWise

def RowwiseSum(mat):
    final_r = []
    for i in range(3):
        arr_r =[]
        Sum = 0
        for j in range(3):
            new = mat[i][j]
            arr_r.append(new)
        Sum = sum(arr_r)  
        final_r.append(Sum)     
    return final_r
   

print(ColumnwiseSum(Mat))
print((RowwiseSum(Mat)))

#problem 8

A = [1,3,5,8,10] 
B = [2,4,6,9] 

def SortedMerge(Arr1, Arr2):
    for i in range(len(Arr2)):
        Arr1.append(Arr2[i])
    start = 0
    for i in range(len(Arr1)):
        new = int(Minimum(Arr1,start,len(Arr1)-1))
        prev = Arr1[i]
        Arr1[i] = Arr1[new]
        Arr1[new] = prev
        start += 1
    return Arr1         

print(SortedMerge(A, B))    
      
        
# prblm 9

string = 'radarer'
def PalindromRecursive(strg):
    i = 0
    j= -(i+1)
    # chec = 1
    size = len(strg)
    if size == 0 :
        return 1
    elif strg[i] != strg[j]:
        return 0
    else:
        i+=1
        new = strg[i:j:1]
        return PalindromRecursive(new)
    

check = PalindromRecursive(string)
if check == 1:
    print("Palindrom")
else:
    print("Not Palindrome")

# problem 10

array =  [10, -1, 9, 20, -3, -8, 22, 9, 7] 

def Sort10(Arr):
    arr_g = []
    arr_s = []
    for i in range(len(Arr)):
        if Arr[i]>=0:
            arr_g.append(Arr[i])
        if Arr[i]<0:
            arr_s.append(Arr[i])
            
    arr_g.sort()
    arr_s.sort()
    final = []  
    for i in range(len(Arr)):
        if i>len(arr_s) and i>len(arr_g):
            break
        if i<len(arr_s):
            final.append(arr_s[i])
        if i<len(arr_g):
            final.append(arr_g[i])
    return final

print(Sort10(array))

 
