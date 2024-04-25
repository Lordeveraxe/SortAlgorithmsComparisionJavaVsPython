package org.example;

import org.apache.commons.csv.CSVFormat;
import org.apache.commons.csv.CSVParser;
import org.apache.commons.csv.CSVRecord;
import java.io.Reader;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.List;
import java.io.IOException;

public class CSVDataLoader {

    public static int[] loadDataFromCSV(String filePath, String columnName) throws IOException {
        Reader in = new FileReader(filePath);
        CSVParser parser = new CSVParser(in, CSVFormat.DEFAULT.withFirstRecordAsHeader());
        List<Integer> scores = new ArrayList<>();

        for (CSVRecord record : parser) {
            String scoreStr = record.get(columnName);
            if (scoreStr != null && !scoreStr.isEmpty()) {
                scores.add(Integer.parseInt(scoreStr));
            }
        }

        parser.close();
        in.close();

        return scores.stream().mapToInt(i -> i).toArray();
    }
}