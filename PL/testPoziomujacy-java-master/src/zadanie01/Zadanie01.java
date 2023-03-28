package zadanie01;

import java.util.Scanner;

/**
 *
 * Napisz program wypisujący true, gdy wczytana od użytkownika liczba typu int jest większa niż 100 oraz mniejsza
 * bądź równa 500.
 */
public class Zadanie01 {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        int wartosc = scanner.nextInt();

       if(wartosc> 100 && wartosc <=500){
            System.out.println(true);}
            else {
                System.out.println(false);
            }

        }
}

