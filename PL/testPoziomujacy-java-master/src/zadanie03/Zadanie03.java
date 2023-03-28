package zadanie03;

/**
 * Zsumuj wszystkie liczby od 0 do 997 i wyświetli wynik na konsoli. Zadanie zrób używając pętli
 * • for
 * • while
 * • do-while
 */
public class Zadanie03 {
    public static void main(String[] args) {

      System.out.println("Pętla for");
        int sum = 0;
        for(int i =0; i <998; i++){

            sum = sum + i;
        }
        System.out.println("Wynnik  - "+ sum+ '\n');


        System.out.println("Pętla while");
        int sum2 = 0;
        int k=1;
        while (k <998){
            sum2 =sum2+k;
            k++;
        }
          System.out.println("Wynnik  - "+ sum2+ '\n');


        System.out.println("Pętla do-while");
        int d=0;
        int sum3 = 0;
        do{
            sum3 = sum3+d;
            d++;
        }while (d <998);
        System.out.println("Wynnik  - "+ sum3+ '\n');

    }
}
