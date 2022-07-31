import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.read_csv('data.csv')
height = data[['Height(cm)']]
height = np.array(height)
plt.plot(height)

heightSorted = height

def insertion_sort(A): 
   

        for i in range(1, len(A)): 
   
            a = A[i] 
   

            j = i - 1 
           
            while j >= 0 and a < A[j]: 
                A[j + 1] = A[j] 
                j -= 1 
                 
            A[j + 1] = a 
             
        return A
            
insertion_sort(heightSorted)

plt.plot(heightSorted)
plt.ylabel("Height (cm)")
plt.legend(["Unsorted","Sorted"])
plt.show()
