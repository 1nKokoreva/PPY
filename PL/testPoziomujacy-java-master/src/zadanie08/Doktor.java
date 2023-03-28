package zadanie08;

public class Doktor extends Osoba {

    double bonus;

    public Doktor(String ime, String nazwisko, double wysOplaty, double bonus) {
        super(ime, nazwisko, wysOplaty);
        this.bonus= bonus;
    }

    @Override
    public String toString() {
        return "Doktor{" +
                "bonus=" + bonus +
                ", ime='" + ime + '\'' +
                ", nazwisko='" + nazwisko + '\'' +
                ", wysOplaty=" + wysOplaty +
                '}';
    }


}
