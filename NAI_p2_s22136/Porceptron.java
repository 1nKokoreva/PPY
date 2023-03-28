public class Porceptron {
    int progu ;
    double kat;
    int wrtD;
    double[] w;
    double[] x;
    int epoka;
    private int cechy = 2;

    private double przesuniecie = 0.1;

    public Porceptron(int progu, double kat, int wrtD, double[] w, double[] x) {
        this.progu = progu;
        this.kat = kat;
        this.wrtD = wrtD;
        this.w = w;
        this.x = x;
    }


    public double predict(double[] waga, double[] testNumbers){
        double wtx = 0;
        for (int i = 0; i < waga.length; i++) {
            //[1,3,  0]
            //[8,5]
            wtx += waga[i]*testNumbers[i];
        }
        wtx += przesuniecie*waga[cechy];
        return wtx;
    }
    private int zeroLubJsedenY(){
        if(predict(w,x) >= progu){
            return 1;
        }else
            return 0;
    }
//W' = W + (d - y) * L*X
    public double[] wSecond(){
        if (epoka > 0) {
            double[] wSecond = new double[this.w.length];
            for (int j = 0; j < epoka; j++) {
                int y = zeroLubJsedenY();
                for (int i = 0; i < wSecond.length; i++) {

                }
            }
            // dostajemy wektor: [5,10,0] gdzie 0 to nasza klasa
            // skoro wektor ma dwa elementy nie liczc klasy
            // to waga ma tez dwa elementy
            // waga = 0
            // waga[0] = 0(waga[0]) + 0.2 * 5 * blad
            // waga[1] = waga[1] + 0.2 * 10 * blad
            // dane treiningowe [x,y]
            // waga = waga + (współczynnik_uczenia * błąd * wartość_wejścia)
            //wSecond[i] = this.w[i] + (wrtD - y) * kat * this.x[i];
            return wSecond;
        }
    }
}
