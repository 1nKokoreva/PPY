package zadanie06;

/**
 * Napisz klasę Pracownik, która będzie przedstawiała pracownika dowolnej firmy. Każdy obiekt powinen przechowywać
 * takie informacje jak:
 * • imię
 * • nazwisko
 * • rok urodzenia
 * • staż pracy
 * • id, które będzie nadawane automatycznie począwszy od numeru 1
 *
 * W klasie Zadanie06 stwórz trzy obiekty reprezentujące pracowników, a następnie wypisz o nich informacje.
 */
public class Zadanie06 {
    public static void main(String[] args) {
        Pracownik p1 =new Pracownik("Ru","Sinert",2002,2);
        Pracownik p2 =new Pracownik("Kim","Evrig",1978,15);
        Pracownik p3 =new Pracownik("Piter","Parker",1995,7);
        System.out.println(p1);
        System.out.println(p2);
        System.out.println(p3);
    }
}

class Pracownik{

    String imie;
    String nazwisko;
    int rokUrodzenia;
    int stazPracy;
    int num;
    private static int id =1;

    public Pracownik(String imie, String nazwisko, int rokUrodzenia, int stazPracy) {
        this.imie = imie;
        this.nazwisko = nazwisko;
        this.rokUrodzenia = rokUrodzenia;
        this.stazPracy = stazPracy;
        this.num=id++;
    }

    @Override
    public String toString() {
        return "Pracownik{" +
                "imie='" + imie + '\'' +
                ", nazwisko='" + nazwisko + '\'' +
                ", rokUrodzenia=" + rokUrodzenia +
                ", stazPracy=" + stazPracy +
                ", id=" + num +
                '}';
    }
}
