import time
import tracemalloc
from tqdm import tqdm
import pandas as pd
from BubbleSort import bubbleSort
from QuickSort import quicksort
from MergeSort import mergeSort


def loadDataFromCSV(filePath, columnName, size):
    """Load data from a CSV file using pandas, extracting a specified column up to a specified number of rows."""
    return pd.read_csv(filePath, usecols=[columnName])[columnName].dropna().head(size).astype(int).tolist()

def run_sort_test(data, sort_function, name):
    """Run sorting test for a given sort function and write results to a DataFrame, with memory usage."""
    # Start tracing memory allocation
    tracemalloc.start()
    
    results = []
    total_duration_ms = 0
    
    for i in tqdm(range(1000), desc=f"Running {name}"):
        test_data = data[:]  # Reset data to original
        
        start_time = time.time()
        sort_function(test_data)  # Perform sorting
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
    size = 25000

    data = loadDataFromCSV(filePath, columnName, size)
    results_dict = {}
    general_results = []

    for sort_function, name in zip([bubbleSort,mergeSort, quicksort], [ 'BubbleSort','MergeSort', 'QuickSort']):
        print(f"Running {name} performance test...")
        detailed_results, general_result = run_sort_test(data, sort_function, name)
        results_dict[name] = detailed_results
        general_results.append(general_result)
        pd.DataFrame(detailed_results, columns=['Algorithm', 'Iteration', 'Execution Time (ms)', 'Memory Usage (bytes)']).to_csv(f'{name.lower()}_results_{size}.csv', index=False)
        print(f"{name} test completed")

    pd.DataFrame(general_results, columns=['Algorithm', 'Execution Time (ms)']).to_csv(f'general_results_{size}.csv', index=False)
    print("Performance test completed and data saved to CSV files")