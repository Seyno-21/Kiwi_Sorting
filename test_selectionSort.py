from random import randint, random
import numpy as np
from SelectionSorting import selectionSort
from time import time

avgcase= [randint(1,10000) for _ in range(1000)]
bestcase= sorted(avgcase)
worstcase= sorted(avgcase, reverse=True) 


def test_SelectWorst():
    start= time()
    assert np.array_equal( selectionSort(np.copy(worstcase), len(worstcase)) , bestcase)
    print(str(time()-start))

def test_SelectBest():
    start= time()
    assert np.array_equal( selectionSort(np.copy(bestcase), len(bestcase)) , bestcase)
    print(str(time()-start))

def test_SelectAvg():
    start= time()
    assert np.array_equal( selectionSort(np.copy(avgcase), len(avgcase)) , bestcase)
    print(str(time()-start))