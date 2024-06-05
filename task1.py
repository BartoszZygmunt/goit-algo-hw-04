import random
import timeit
import pandas as pd

# Implementing merge sort
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# Implementing insertion sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Generating test data
def generate_data(size):
    return [random.randint(0, 100000) for _ in range(size)]

# Wrapper functions for timeit
def merge_sort_wrapper(arr):
    merge_sort(arr.copy())

def insertion_sort_wrapper(arr):
    insertion_sort(arr.copy())

def timsort_wrapper(arr):
    sorted(arr)

# Define data sizes to test
data_sizes = [100, 1000, 10000]

# Collecting execution times
execution_times = {"Merge Sort": [], "Insertion Sort": [], "Timsort": []}

print("Execution times for different data sizes: (be patient, it may take a while!)")
for size in data_sizes:
    print(f"Data size: {size} elements. Wait for the results...")
    data = generate_data(size)
    merge_time = timeit.timeit(lambda: merge_sort_wrapper(data), number=10)
    insertion_time = timeit.timeit(lambda: insertion_sort_wrapper(data), number=10)
    timsort_time = timeit.timeit(lambda: timsort_wrapper(data), number=10)
    
    execution_times["Merge Sort"].append(merge_time)
    execution_times["Insertion Sort"].append(insertion_time)
    execution_times["Timsort"].append(timsort_time)

# Display the results in a DataFrame
df = pd.DataFrame(execution_times, index=data_sizes)
df.index.name = 'Data Size'
print("\nExecution times for different data sizes:")
print(df)
