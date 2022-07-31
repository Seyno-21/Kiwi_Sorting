from random import randint, random
import numpy as np
from BubbleSorting import Sort, A
from time import time

avgCase= [randint(1,10000) for _ in range(1000)]
bestcase= sorted(avgCase)
worstcase= sorted(avgCase, reverse=True) 


def test_BubbleWorst():
    start= time()
    assert np.array_equal( Sort(np.copy(worstcase)) , bestcase)
    print(str(time()-start))

def test_BubbleBest():
    start= time()
    assert np.array_equal( Sort(np.copy(bestcase)) , bestcase)
    print(str(time()-start))

def test_BubbleAvg():
    start= time()
    assert np.array_equal( Sort(np.copy(avgCase)) , bestcase)
    print(str(time()-start))