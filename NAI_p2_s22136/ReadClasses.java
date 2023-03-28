import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class ReadClasses {

    private String trainPath;
    private String testPath;

    public ReadClasses(String trainPath, String testPath) {
        this.trainPath = trainPath;
        this.testPath = testPath;
    }

    private List<Numbers<Integer>> zwrotClassWrapper(String path, int ileZnikow) {
        List<String> l = readLines(path);
        List<Numbers<Integer>> listNumber = new ArrayList<>();
        for (int i = 0; i < l.size(); i++) {
            String x = l.get(i);
            Numbers<Integer> numbers = Numbers.creatNewFromString(x,ileZnikow);
            listNumber.add(numbers);
        }
        return listNumber;
    }

    public List<Numbers<Integer>> getNumbersTest() {
        return zwrotClassWrapper(testPath,2);
    }

    public List<Numbers<Integer>> getNumbersTrain() {
        return zwrotClassWrapper(trainPath,2);
    }

    public static void shuffle(List<Numbers> numbers){
        Collections.shuffle(numbers); //miesza kolejnosc podanej listy
    }

    public List<String> readLines(String path) {
        List<String> newLista = new ArrayList<>();
        try (BufferedReader reader = new BufferedReader(new FileReader(path))) {
            String line = null;
            while ((line = reader.readLine()) != null) {
                newLista.add(line);
            }

        } catch (IOException e) {
            throw new RuntimeException(e);
        }

        return newLista;
    }

}
