package zadanie09;

public class Prostokat implements Obliczanie {

    private double dlug, szer;

    public Prostokat(double dlug, double szer) {
        this.dlug = dlug;
        this.szer = szer;
    }
    @Override
    public double obliczObwod() {
        return (2*szer)+(2*dlug);
    }

    @Override
    public double obliczPole() {
        return szer*dlug;
    }

    @Override
    public String toString() {
        return "Prostokat: " + '\n'+
                "dlug=" + dlug + '\n'+
                "szer=" + szer +'\n'+
                "Pole ="+obliczPole()+ '\n'+
                "Obwod ="+ obliczObwod();
    }
}
