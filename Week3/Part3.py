import numpy as np
# 1
def printMatrix(A, starting_index, rows, columns):#starting index is a tuple
    array = [[0 for _ in range(columns)] for _ in range(rows)]
    inx_row = 0
    for i in range(starting_index[0],rows+starting_index[0]):
        indx_col = 0
        for j in range(starting_index[1],columns+starting_index[1]):
            array[inx_row][indx_col]=A[i][j]
            indx_col += 1
        inx_row +=1
    return array


# 2
def MatAdd(A,B):
    if len(A) != len(B) or len(A[0]) != len(B[0]):
        return None
    else:
        array = [[0 for i in range(len(A[0]))]for i in range(len(A))]
        for i in range(len(A)):
            for j in range(len(A[0])):
                array[i][j]=A[i][j]+B[i][j]
    return array

#3
def MatAddPartial(A, B, start, size):
    if start[0]+size > len(A) or start[1]+size > len(A[0]):
        return None
    else:    
        array = [[0 for _ in range(size)] for _ in range(size)]
        inx_row = 0
        for i in range(start[0],size+start[0]):
            indx_col = 0
            for j in range(start[1],size+start[1]):
                array[inx_row][indx_col]=A[i][j]+B[i][j]
                indx_col += 1
            inx_row +=1
    return array

#4
def  MatMul(A,B):
    if len(A[0]) != len(B):
        return None
    else:
        result = [[0 for i in range(len(A))]for i in range(len(B[0]))]
        indx_row = 0
        for i in range(len(A)):
            indx_col = 0
            for j in range(len(B[0])):
                sum = 0
                for k in range(len(B)):
                    mul = A[i][k]*B[k][j]
                    sum += mul
                result[indx_row][indx_col] = sum
                indx_col+=1
            indx_row+=1
    return result        
    
####### NEEDED FUNCTIONS FOR THE NEXT QUESTIONS
def subtract_matrices(A, B):
    n = len(A)
    C = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            C[i][j] = A[i][j] - B[i][j]
    return C
###############    

# 5
def MatMulRecursive(A, B):
    n = len(A)
    if n == 1:      #base condition
        return [[A[0][0] * B[0][0]]]
    mid = n // 2
    A11 = [[A[i][j] for j in range(mid)] for i in range(mid)]    # Dividing the matrices into 4 submatrices
    A12 = [[A[i][j] for j in range(mid, n)] for i in range(mid)]
    A21 = [[A[i][j] for j in range(mid)] for i in range(mid, n)]
    A22 = [[A[i][j] for j in range(mid, n)] for i in range(mid, n)]
    B11 = [[B[i][j] for j in range(mid)] for i in range(mid)]
    B12 = [[B[i][j] for j in range(mid, n)] for i in range(mid)]
    B21 = [[B[i][j] for j in range(mid)] for i in range(mid, n)]
    B22 = [[B[i][j] for j in range(mid, n)] for i in range(mid, n)]

    C11 = MatAdd(MatMulRecursive(A11, B11), MatMulRecursive(A12, B21))  #Recusive calls
    C12 = MatAdd(MatMulRecursive(A11, B12) , MatMulRecursive(A12, B22))
    C21 = MatAdd(MatMulRecursive(A21, B11) , MatMulRecursive(A22, B21))
    C22 = MatAdd(MatMulRecursive(A21, B12) , MatMulRecursive(A22, B22))

    C = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(mid):        #Combining the submatrices
        for j in range(mid):
            C[i][j] = C11[i][j]
            C[i][j + mid] = C12[i][j]
            C[i + mid][j] = C21[i][j]
            C[i + mid][j + mid] = C22[i][j]
    return C        

#6
def  MatMulStrassen(A, B):
    n = len(A)
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    mid = n // 2
    A11 = [[A[i][j] for j in range(mid)] for i in range(mid)]    # Dividing the matrices into 4 submatrices
    A12 = [[A[i][j] for j in range(mid, n)] for i in range(mid)]
    A21 = [[A[i][j] for j in range(mid)] for i in range(mid, n)]
    A22 = [[A[i][j] for j in range(mid, n)] for i in range(mid, n)]
    B11 = [[B[i][j] for j in range(mid)] for i in range(mid)]
    B12 = [[B[i][j] for j in range(mid, n)] for i in range(mid)]
    B21 = [[B[i][j] for j in range(mid)] for i in range(mid, n)]
    B22 = [[B[i][j] for j in range(mid, n)] for i in range(mid, n)]
    
    M1 =  MatMulStrassen(MatAdd(A11, A22), MatAdd(B11, B22))   #Recusive calls
    M2 =  MatMulStrassen(MatAdd(A21, A22), B11)
    M3 =  MatMulStrassen(A11, subtract_matrices(B12, B22))
    M4 =  MatMulStrassen(A22, subtract_matrices(B21, B11))
    M5 =  MatMulStrassen(MatAdd(A11, A12), B22)
    M6 =  MatMulStrassen(subtract_matrices(A21, A11), MatAdd(B11, B12))
    M7 =  MatMulStrassen(subtract_matrices(A12, A22), MatAdd(B21, B22))

    C11 = MatAdd(subtract_matrices(MatAdd(M1, M4), M5), M7) #resultant submatrices
    C12 = MatAdd(M3, M5)
    C21 = MatAdd(M2, M4)
    C22 = MatAdd(subtract_matrices(MatAdd(M1, M3), M2), M6)

    C = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(mid):    #Combining the submatrices
        for j in range(mid):
            C[i][j] = C11[i][j]
            C[i][j + mid] = C12[i][j]
            C[i + mid][j] = C21[i][j]
            C[i + mid][j + mid] = C22[i][j]
    return C


#Driver code
if __name__=="__main__":
    A = [
        [1, 4],
        [2, 5]
    ]

    B = [
        [7, 8],
        [10, 11]
    ]
    
    print(printMatrix(A, (0,1), 2, 2))
    print(MatAdd(A,B))
    print(MatAddPartial(A,B,(0,1),2))
    print(MatMul(A,B))
    print( MatMulRecursive(A, B))
    print(MatMulStrassen(A, B))