def forward_substitution():
    
    return



def backward_substitution():

    return 



def pivot(A, n):
    for k in range(n, len(A)):
        if A[k][n] != 0:
            temp = A[n]
            A[n] = A[k]
            A[k] = temp
    
    return A