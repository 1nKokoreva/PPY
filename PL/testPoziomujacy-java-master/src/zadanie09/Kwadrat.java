package zadanie09;

public class Kwadrat implements Obliczanie {
    private double dlug;

    public Kwadrat(double dlug) {
        this.dlug = dlug;

    }

    @Override
    public double obliczPole() {
        return dlug*dlug;
    }

    @Override
    public double obliczObwod() {
        return dlug*4;
    }

    @Override
    public String toString() {
        return "Kwadrat:" + '\n'+
                "dlug=" + dlug + '\n'+
                "Pole ="+obliczPole()+ '\n'+
                "Obwod ="+ obliczObwod();
    }

}


