package zadanie09;

public class Kolo implements Obliczanie {
    double radius;

    public Kolo(double radius) {
        this.radius = radius;
    }

    @Override
    public double obliczPole() {
        return (Math.PI * radius*radius);
    }

    @Override
    public double obliczObwod() {
        return 2*Math.PI*radius;
    }

    @Override
    public String toString() {
        return "Kolo:" +'\n'+
                "radius=" + radius +'\n'+
                "Pole ="+obliczPole()+ '\n'+
                "Obwod ="+ obliczObwod()
                ;
    }
}
