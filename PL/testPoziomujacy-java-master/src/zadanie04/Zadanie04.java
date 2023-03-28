package zadanie04;

/**
 *  Dana jest tablica:
 *  int [] wszystkieLiczby = {23, 1, 92, -23, 123, 334, -231};
 *  1) wypisz tylko liczby większe niż 4
 *  2) znajdź największy element
 *  3) wypisz elementy na nieparzystych indeksach
 */
public class Zadanie04 {
    public static void main(String[] args) {
        int [] wszystkieLiczby = {23, 1, 92, -23, 123, 334, -231};
        System.out.println("1) wypisz tylko liczby większe niż 4");
        for (int i =0; i< wszystkieLiczby.length; i++){
            if (wszystkieLiczby[i] > 4) {
                System.out.print(wszystkieLiczby[i]+" ");
            }
        }
        System.out.println();

        System.out.println("2) znajdź największy element");
        int max =0;
        for (int i =0; i< wszystkieLiczby.length; i++){
            if (wszystkieLiczby[i]>max)
                max = wszystkieLiczby[i];
        }
        System.out.println(max);

        System.out.println("3) wypisz elementy na nieparzystych indeksach");
        for (int i =0; i< wszystkieLiczby.length; i++){
            if (i%2 != 0)
                System.out.println("Indeks num: "+i+", element: "+ wszystkieLiczby[i]);
        }

    }
}
