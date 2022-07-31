A = [4,2,7,8,1,9,10]

def insertion_sort(A): 
   

        for i in range(1, len(A)): 
   
            a = A[i] 
   

            j = i - 1 
           
            while j >= 0 and a < A[j]: 
                A[j + 1] = A[j] 
                j -= 1 
                 
            A[j + 1] = a 
             
        return A
            
print(insertion_sort(A))
