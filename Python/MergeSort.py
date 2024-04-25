def merge(arr1, arr2):
    """Merge two sorted arrays into a single sorted array."""
    i, j = 0, 0
    result = []
    # Compare elements from arr1 and arr2 and add the smaller one to the result
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1
    
    # If there are remaining elements in arr1, add them to result
    result.extend(arr1[i:])
    # If there are remaining elements in arr2, add them to result
    result.extend(arr2[j:])
    
    return result
    
def mergeSort(arr):
    """Sort an array using the merge sort algorithm."""
    if len(arr) <= 1:
        return arr
    
    # Divide the array into halves
    mid = len(arr) // 2
    left = mergeSort(arr[:mid])
    right = mergeSort(arr[mid:])
    
    # Merge the sorted halves
    return merge(left, right)
import time
import tracemalloc
from tqdm import tqdm
import pandas as pd
def loadDataFromCSV(filePath, columnName, size):
    """Load data from a CSV file using pandas, extracting a specified column up to a specified number of rows."""
    return pd.read_csv(filePath, usecols=[columnName])[columnName].dropna().head(size).astype(int).tolist()
# Driver code to test the Bubble Sort implementation
def run_sort_test(data, name):
    """Run sorting test for a given sort function and write results to a DataFrame, with memory usage."""
    # Start tracing memory allocation
    tracemalloc.start()
    
    results = []
    total_duration_ms = 0
    
    for i in tqdm(range(1000), desc=f"Running {name}"):
        test_data = data[:]  # Reset data to original
        
        start_time = time.time()
        mergeSort(test_data)  # Perform sorting
        duration_ms = (time.time() - start_time) * 1000
        
        total_duration_ms += duration_ms
        # Capture memory usage for this iteration
        snapshot = tracemalloc.take_snapshot()
        stats = snapshot.statistics('lineno')
        mem_used = stats[0].size
        results.append([name, i, duration_ms, mem_used])
        
        # Reset memory tracking
        tracemalloc.clear_traces()

    # Stop tracing memory allocation
    tracemalloc.stop()

    return results, [name, total_duration_ms]
if __name__ == '__main__':
    filePath = "ResultadosSaberPro.csv"
    columnName = "MOD_RAZONA_CUANTITAT_PUNT"
    size = 100000

    data = loadDataFromCSV(filePath, columnName, size)
    results_dict = {}
    general_results = []
    name = 'MergeSort'
    print(f"Running {name} performance test...")
    detailed_results, general_result = run_sort_test(data, name)
    results_dict[name] = detailed_results
    pd.DataFrame(detailed_results, columns=['Algorithm', 'Iteration', 'Execution Time (ms)', 'Memory Usage (bytes)']).to_csv(f'{name.lower()}_results_{size}.csv', index=False)
    print(f"{name} test completed")
    print("Performance test completed and data saved to CSV files")