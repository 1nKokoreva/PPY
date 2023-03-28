package zadanie07;

/**
 * Przygotuj klasę Osoba definiującą pola:
 * <p>
 * • String imie,
 * • int rokUrodzenia
 * <p>
 * Klasa będzie również definiować:
 * <p>
 * • dwuargumentowy konstruktor, inicjujący pola klasy;
 * • jednoargumentowy konstruktor, przyjmujący jako parametr String imie, natomiast jako pole rokUrodzenia
 * przypisujący wartość 1990;
 * • metodę zwrocImie() zwracającą wartość pola imie;
 * • metodę zwrocWiek() zwracającą wiek osoby;
 * • metodę zwrocStarszaOsobe przyjmującą w liście argumentów dwa obiekt klasy Osoba
 * i zwracającą starszą osobę;
 * • statyczną metodę zwrocNajstarszaOsobe przyjmującą jako argument tablicę obiektów klasy Osoba
 * i zwracającą najstarszą osobę.
 * <p>
 * W klasie Main stwórz kilka obiektów i przetestuj wszystkie metody.
 */
public class Zadanie07 {
    public static void main(String[] args) {

        Osoba[] tab = new Osoba[4];
        tab[0] = new Osoba("Mariana", 2000);
        tab[1] = new Osoba("Adam", 1899);
        tab[2] = new Osoba("Roxan");
        tab[3] = new Osoba("Aid", 1957);

       for(int i=0; i<tab.length; i++){
           System.out.println(tab[i]);
       }

        System.out.println(tab[0].zwrocImie());
        System.out.println(tab[2].zwrocWiek());
        System.out.println("STARSZA OSOBA: " + zwrocStarszaOsobe(tab[0], tab[2]));
        System.out.println("NAJSTARSA OSOBA: "+ zwrocNajstarszaOsobe(tab));
    }

    public static Osoba zwrocStarszaOsobe(Osoba osoba1, Osoba osoba2) {
        if (osoba1.zwrocWiek() > osoba2.zwrocWiek()) {
            return osoba1;
        } else
            return osoba2;
    }

    public static Osoba zwrocNajstarszaOsobe(Osoba[] tab){
        int maxwiek =0;                                             //-
        int max = tab[0].zwrocWiek();
        for (int i = 0; i < tab.length; i++) {
            if (tab[i].zwrocWiek() > max)
                max = tab[i].zwrocWiek();
               maxwiek = i;
        }
        return tab[maxwiek];
    }

}

class Osoba {

    String ime;
    int rokUrodzenia;

    public Osoba(String ime, int rokUrodzenia) {
        this.ime = ime;
        this.rokUrodzenia = rokUrodzenia;
    }

    public Osoba(String ime) {
        this.ime = ime;
        this.rokUrodzenia = 1990;
    }

    public String zwrocImie() {
        return this.ime;
    }

    public int zwrocWiek() {
        return 2022 - this.rokUrodzenia;
    }


    @Override
    public String toString() {
        return "Osoba{" +
                "ime='" + ime + '\'' +
                ", rokUrodzenia=" + rokUrodzenia +
                '}';
    }
}