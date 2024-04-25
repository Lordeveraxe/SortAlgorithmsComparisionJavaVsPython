def bubbleSort(arr):
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        swapped = False  # This flag is used to detect if any swap has occurred

        # Last i elements are already sorted
        for j in range(0, n-i-1):

            # Compare the current element with the next one
            if arr[j] > arr[j+1]:
                # Swap if the current element is greater than the next
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True  # Set the flag to True indicating a swap occurred

        # If no two elements were swapped by inner loop, then break
        if not swapped:
            break

    return arr  # Return the sorted array
import pandas as pd
def loadDataFromCSV(filePath, columnName, size):
    """Load data from a CSV file using pandas, extracting a specified column up to a specified number of rows."""
    return pd.read_csv(filePath, usecols=[columnName])[columnName].dropna().head(size).astype(int).tolist()
# Driver code to test the Bubble Sort implementation
if __name__ == "__main__":
    for i in range(1000):
        filePath = "ResultadosSaberPro.csv"
        columnName = "MOD_RAZONA_CUANTITAT_PUNT"
        size = 10000
        data = loadDataFromCSV(filePath, columnName, size)
        test_data = data[:]  # Reset data to original
        print(f"Original data")
        sorted_data = bubbleSort(test_data)
        print(f"Sorted data")

    