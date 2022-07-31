def Sort(A):
    n = len(A)

    

    for i in range(n-1):

        for j in range(0, n-i-1):
 
            if A[j] > A[j + 1]:
                
                A[j], A[j + 1] = A[j + 1], A[j]
         
       
    return A
 
 
A = [5,4,6,312,4,7,453,8]
 
Sort(A)

print(A)