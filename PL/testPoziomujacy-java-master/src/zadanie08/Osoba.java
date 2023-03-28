package zadanie08;

import java.util.Comparator;
import java.util.function.Function;
import java.util.function.ToDoubleFunction;
import java.util.function.ToIntFunction;
import java.util.function.ToLongFunction;

public class Osoba implements Comparator<Osoba> {
    String ime;
    String nazwisko;
    double wysOplaty;

    public Osoba() {
    }
    public Osoba(String ime, String nazwisko, double wysOplaty) {
        this.ime = ime;
        this.nazwisko = nazwisko;
        this.wysOplaty = wysOplaty;
    }

    @Override
    public String toString() {
        return "Osoba{" +
                "ime='" + ime + '\'' +
                ", nazwisko='" + nazwisko + '\'' +
                ", wysOplaty=" + wysOplaty +
                '}';
    }

    public int compareTo(Osoba x) {
        if(nazwisko.compareTo(x.nazwisko) == 0) {
            return (int) (wysOplaty - x.wysOplaty);
        }
        return nazwisko.compareTo(x.nazwisko);

    }

    @Override
    public int compare(Osoba o1, Osoba o2) {
        return 0;
    }

    @Override
    public Comparator<Osoba> reversed() {
        return Comparator.super.reversed();
    }

    @Override
    public Comparator<Osoba> thenComparing(Comparator<? super Osoba> other) {
        return Comparator.super.thenComparing(other);
    }

    @Override
    public <U> Comparator<Osoba> thenComparing(Function<? super Osoba, ? extends U> keyExtractor, Comparator<? super U> keyComparator) {
        return Comparator.super.thenComparing(keyExtractor, keyComparator);
    }

    @Override
    public <U extends Comparable<? super U>> Comparator<Osoba> thenComparing(Function<? super Osoba, ? extends U> keyExtractor) {
        return Comparator.super.thenComparing(keyExtractor);
    }

    @Override
    public Comparator<Osoba> thenComparingInt(ToIntFunction<? super Osoba> keyExtractor) {
        return Comparator.super.thenComparingInt(keyExtractor);
    }

    @Override
    public Comparator<Osoba> thenComparingLong(ToLongFunction<? super Osoba> keyExtractor) {
        return Comparator.super.thenComparingLong(keyExtractor);
    }

    @Override
    public Comparator<Osoba> thenComparingDouble(ToDoubleFunction<? super Osoba> keyExtractor) {
        return Comparator.super.thenComparingDouble(keyExtractor);
    }
}
