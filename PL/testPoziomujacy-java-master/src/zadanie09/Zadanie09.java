package zadanie09;

/**
 * Stwórz interfejs Obliczanie, który będzie posiadał następujące metody
 *
 * • double obliczPole()
 * • double obliczObwod()
 *
 * Następnie zaimplementuj go w klasach:
 * • Kwadrat
 * • Prostokąt
 * • Koło.
 *
 * Niech każda klasa w konstruktorze przyjmuje niezbędne dane do obliczenia pola oraz obwodu. Stwórz po jednej
 * instancji każdej klasy, następnie za pomocą pętli wypisz pole i obwód każdej figury np.
 * ”Koło: obwód - X, pole - Y”
 *
 * Napisz metodę w interfejsie obliczanie, którą będzie można wywołać bez obiektu danej klasy.
 * Przyjmie ona listę dowolnych figur i zwróci tą, której pole jest największe.
 *
 * Do obliczenia pola koła będzie potrzebna liczba PI, użyj stałej dostępnej w bibliotece math.
 */
public class Zadanie09 {
    public static void main(String[] args) {

        Kolo ko1 = new Kolo(8);
        System.out.println(ko1);
        System.out.println();
        Prostokat pr1 = new Prostokat(2,5);
        System.out.println(pr1);
        System.out.println();
        Kwadrat kw1 = new Kwadrat(8);
        System.out.println(kw1);
        System.out.println();
    }


}
