package org.example;

import java.io.FileWriter;
import java.io.IOException;
import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVParser;
import org.apache.commons.csv.CSVRecord;
import java.io.Reader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.List;

public class PerformanceTest {
    public static void main(String[] args) throws IOException, InterruptedException {
        // Datos de ejemplo - asegúrate de cambiar esto por la lectura de tu archivo CSV
        String filePath = "C:\\Users\\santi\\Documents\\GitHub\\SortAlgorithms\\src\\main\\java\\org\\example\\ResultadosSaberPro.csv";
        String columnName = "MOD_RAZONA_CUANTITAT_PUNT"; // Cambiar este nombre según la columna deseada
        int size = 100000; // Cambiar este tamaño según la cantidad de datos que desees cargar
        int[] data = loadDataFromCSV(filePath, columnName, size);
        int[] original = data.clone();
        FileWriter writerBubble = new FileWriter("bubble_results_"+size+".csv");
        FileWriter writerMerge = new FileWriter("merge_results_"+size+".csv");
        FileWriter writerQuick = new FileWriter("quick_results_"+size+".csv");
        FileWriter generalWriter = new FileWriter("general_results_"+size+".csv");
        // Encabezados para el archivo CSV
        writerMerge.append("Algorithm,Iteration,Execution Time (ms),Memory Usage (bytes)\n");
        writerBubble.append("Algorithm,Iteration,Execution Time (ms),Memory Usage (bytes)\n");
        writerQuick.append("Algorithm,Iteration,Execution Time (ms),Memory Usage (bytes)\n");
        generalWriter.append("Algorithm,Execution Time (ms)\n");
        // Realizar las pruebas 10,000 veces por algoritmo
        System.out.println("Running performance test...");
        long allStartTime = System.nanoTime();
        for (int i = 0; i < 1000; i++) {
            System.gc();
            Thread.sleep(10);
            System.arraycopy(original, 0, data, 0, original.length); // Reset data to original

            long startMemory = Runtime.getRuntime().totalMemory() - Runtime.getRuntime().freeMemory();
            long startTime = System.nanoTime();

            MergeSort.sort(data, 0, data.length - 1); // Perform sorting

            long endTime = System.nanoTime();
            long endMemory = Runtime.getRuntime().totalMemory() - Runtime.getRuntime().freeMemory();

            long durationMs = (endTime - startTime) / 1_000_000;
            long memoryUsed = endMemory - startMemory;

            writerMerge.append("MergeSort,").append(String.valueOf(i)).append(",")
                    .append(String.valueOf(durationMs)).append(",")
                    .append(String.valueOf(memoryUsed)).append("\n");
        }
        generalWriter.append("MergeSort,").append(String.valueOf((System.nanoTime() - allStartTime) / 1_000_000)).append("\n");
        System.out.println("MergeSort test completed");
        allStartTime = System.nanoTime();
        for (int i = 0; i < 1000; i++) {
            System.gc();
            Thread.sleep(10);
            System.arraycopy(original, 0, data, 0, original.length); // Reset data to original

            long startMemory = Runtime.getRuntime().totalMemory() - Runtime.getRuntime().freeMemory();
            long startTime = System.nanoTime();

            QuickSort.quickSort(data, 0, data.length - 1); // Perform sorting

            long endTime = System.nanoTime();
            long endMemory = Runtime.getRuntime().totalMemory() - Runtime.getRuntime().freeMemory();

            long durationMs = (endTime - startTime) / 1_000_000;
            long memoryUsed = endMemory - startMemory;

            writerQuick.append("QuickSort,").append(String.valueOf(i)).append(",")
                    .append(String.valueOf(durationMs)).append(",")
                    .append(String.valueOf(memoryUsed)).append("\n");
        }
        generalWriter.append("QuickSort,").append(String.valueOf((System.nanoTime() - allStartTime) / 1_000_000)).append("\n");
        System.out.println("QuickSort test completed");
        for (int i = 0; i < 1000; i++) {
            System.gc();
            Thread.sleep(10);
            System.arraycopy(original, 0, data, 0, original.length); // Reset data to original

            long startMemory = Runtime.getRuntime().totalMemory() - Runtime.getRuntime().freeMemory();
            long startTime = System.nanoTime();

            BubbleSort.bubbleSort(data, data.length); // Perform sorting

            long endTime = System.nanoTime();
            long endMemory = Runtime.getRuntime().totalMemory() - Runtime.getRuntime().freeMemory();

            long durationMs = (endTime - startTime) / 1_000_000;
            long memoryUsed = endMemory - startMemory;

            writerBubble.append("BubbleSort,").append(String.valueOf(i)).append(",")
                    .append(String.valueOf(durationMs)).append(",")
                    .append(String.valueOf(memoryUsed)).append("\n");
        }
        generalWriter.append("BubbleSort,").append(String.valueOf((System.nanoTime() - allStartTime) / 1_000_000)).append("\n");
        System.out.println("BubbleSort test completed");
        writerBubble.flush();
        writerQuick.flush();
        writerMerge.flush();
        generalWriter.flush();
        writerBubble.close();
        writerQuick.close();
        writerMerge.close();
        generalWriter.close();
        System.out.println("Performance test completed and data saved to bubble_results.csv, merge_results.csv, and quick_results.csv");
    }

    public static int[] loadDataFromCSV(String filePath, String columnName, int size) throws IOException {
        Reader in = new FileReader(filePath);
        CSVParser parser = new CSVParser(in, CSVFormat.DEFAULT.withFirstRecordAsHeader());
        List<Integer> scores = new ArrayList<>();

        for (CSVRecord record : parser) {
            String scoreStr = record.get(columnName);
            if (scoreStr != null && !scoreStr.isEmpty()) {
                scores.add(Integer.parseInt(scoreStr));
                if (scores.size() >= size) {
                    break; // Detener la lectura después de alcanzar el tamaño deseado
                }
            }
        }

        parser.close();
        in.close();

        return scores.stream().mapToInt(i -> i).toArray();
    }
}