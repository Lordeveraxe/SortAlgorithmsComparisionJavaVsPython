def quicksort(array):
    def partition(low, high):
        pivot = array[high]
        i = low - 1
        for j in range(low, high):
            if array[j] <= pivot:
                i += 1
                array[i], array[j] = array[j], array[i]
        array[i + 1], array[high] = array[high], array[i + 1]
        return i + 1

    def quick_sort_recursive(low, high):
        if low < high:
            pi = partition(low, high)
            quick_sort_recursive(low, pi - 1)
            quick_sort_recursive(pi + 1, high)

    quick_sort_recursive(0, len(array) - 1)
    return array
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
        quicksort(test_data)  # Perform sorting
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
    size = 50000

    data = loadDataFromCSV(filePath, columnName, size)
    results_dict = {}
    general_results = []
    name = 'QuickSort'
    print(f"Running {name} performance test...")
    detailed_results, general_result = run_sort_test(data, name)
    results_dict[name] = detailed_results
    pd.DataFrame(detailed_results, columns=['Algorithm', 'Iteration', 'Execution Time (ms)', 'Memory Usage (bytes)']).to_csv(f'{name.lower()}_results_{size}.csv', index=False)
    print(f"{name} test completed")
    print("Performance test completed and data saved to CSV files")