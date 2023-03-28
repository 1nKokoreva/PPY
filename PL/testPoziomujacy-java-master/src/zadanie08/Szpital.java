package zadanie08;

import java.util.List;

public class Szpital <T extends Comparable> {
    Object[] arr;
    int dlug = 0;

    public Szpital(int i) {
    }

    public boolean add(T x) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i].equals(x)) {
                return false;
            }
        }
        if (dlug < arr.length) {
            arr[dlug++] = x;
        } else {
            Object[] arr1;
            arr1 = arr;
            arr = new Object[(arr.length + 1)];
            for (int i = 0; i < arr1.length; i++) {
                arr[i] = arr1[i];
            }
            arr[dlug++] = x;
        }
        return true;
    }

}
