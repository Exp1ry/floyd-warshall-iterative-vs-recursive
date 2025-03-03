"""
This module contains a simple performance test which
compares the recursive version of Floyds algorithm with the
imperative version
"""

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from recursion.recursive_floyd import recursive_floyd_warshall
from iterative.iterative_floyd import iterative_floyd
from time import process_time

def performance_test(function_handle):
    """
    A function that performs a simple performance test
    function_handle -> The function which is being tested. 
                       It must take no parameters

    Please complete this function
    """
    start_time=process_time()
    function_handle()
    end_time=process_time()
    print(f"Execution Time: {end_time - start_time:.6f} seconds")

    pass
    

print ("Recursion Test Time")
performance_test(lambda: recursive_floyd_warshall(0,0,0))

print ("Iterative Test Time")
performance_test(iterative_floyd)

    


