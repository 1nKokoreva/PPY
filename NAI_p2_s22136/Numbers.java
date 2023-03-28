public class Numbers <T> {

    double wektor[];
    T etykieta;

    public Numbers(double[] wektor, T etykieta) {
        this.wektor = wektor;
        this.etykieta = etykieta;
    }

    private static boolean isNumber(String text){
        try{
            Integer.parseInt(text);
        }catch (NumberFormatException e){
            return false;
        }
        return true; //jesli etykieta jest int
    }

    public static Numbers creatNewFromString(String line, int ileZnakow){
    String[] parts = line.split(",");

    // pierwsze cztery znaki w stringu reprezentuja wektor
    int vectorParts = ileZnakow;
    double[] wektor = new double[vectorParts];
        for (int i = 0; i < vectorParts; i++) {
        wektor[i] = Double.parseDouble(parts[i]);
    }
    // nazwa naszej klasy znajduje sie na ostatnim miejscu wiec pobieramy stringa
    String className = "";
        if( parts.length > ileZnakow) {
        className = parts[parts.length - 1];
    }
        // "1" -> Intege,praseInt -> 1
        Object etykieta = isNumber(className) ? Integer.parseInt(className) : className;//
        return new Numbers(wektor,etykieta);
}
}
