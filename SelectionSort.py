# -*- coding: utf-8 -*-
"""
Created on Thu Sep 12 02:10:19 2024

@shery: hp
"""

import random
import time
import csv

from BubbleSort import randomArray  

def SelectionSort(array, start, end):
    """Sort the array using the selection sort algorithm."""
    for i in range(start, end):
        mini_Index = i
        for j in range(i + 1, end):
            if array[mini_Index] > array[j]:
                mini_Index = j
        array[i], array[mini_Index] = array[mini_Index], array[i]

# Generate a random array of 30,000 integers
size = 30000
random_numbers = randomArray(size)

print(f"Generated random array of size {size}")

# Measure the runtime of the SelectionSort function
start_time = time.time()
SelectionSort(random_numbers, 0, size)
end_time = time.time()

# Print the sorted array and runtime
print("Sorted array:", random_numbers)
print("Runtime is", end_time - start_time, "seconds")

# Save the sorted array to a CSV file
with open("Selection_Sort.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Sorted Array"])
    for number in random_numbers:
        writer.writerow([number])
