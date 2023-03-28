import com.google.gson.Gson;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import org.json.simple.parser.ParseException;

import java.io.*;
import java.net.MalformedURLException;
import java.net.URL;
import java.nio.charset.StandardCharsets;
import java.util.List;
import java.util.stream.Collectors;

public class WeatherService {

    private final String urlString = String.format("https://api.openweathermap.org/data/2.5/weather?lat=44.34&lon=10.99&appid=%s","71170abf768266d0272d64a7cb0f7ba4");

    private Weather weather;

    public WeatherService() {
        try (InputStream inputStream = new URL(urlString).openConnection().getInputStream();
             BufferedReader bufferedReader = new BufferedReader(new InputStreamReader(inputStream))) {
            String jsonString = bufferedReader.lines().collect(Collectors.joining(System.lineSeparator()));
            System.out.println(jsonString);

            Gson gson = new Gson();
            weather = gson.fromJson(jsonString, Weather.class);
        } catch (IOException e) {
            throw new RuntimeException(e);
        }
    }

    public Weather getWeather() {
        return weather;
    }
}

class Currency{
    List<SingleCurrency> rates;
}
class SingleCurrency{
    String no;
    String effectiveDate;
    double mid;
}


class Weather {
    MainWeatherInfo main;
}

class MainWeatherInfo {
    double temp;
    int humidity;
}