import java.lang.reflect.Array;
import java.util.Arrays;

public class Main {
    public static void main(String[] args) {


        double[] w  = {0,1};
        double[] x  = {1,2};

        Porceptron p = new Porceptron(3,0.5,1,w,x);

        System.out.println(p.WtX(w,x));
        System.out.println(Arrays.toString(p.wSecond()));
        System.out.println(p.WtX(p.wSecond(),x));
    }
}
