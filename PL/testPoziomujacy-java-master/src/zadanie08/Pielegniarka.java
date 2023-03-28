package zadanie08;

public class Pielegniarka extends Osoba{
    int overtime;

    public Pielegniarka(String ime, String nazwisko, double wysOplaty) {
        super(ime, nazwisko, wysOplaty);
    }

    @Override
    public String toString() {
        return "Pielegniarka{" +
                "overtime=" + overtime +
                ", ime='" + ime + '\'' +
                ", nazwisko='" + nazwisko + '\'' +
                ", wysOplaty=" + wysOplaty +
                '}';
    }
}
