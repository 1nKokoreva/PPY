import javafx.application.Platform;
import javafx.embed.swing.JFXPanel;
import javafx.scene.Scene;
import javafx.scene.web.WebView;

import javax.swing.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class WeatherGUI extends JFrame {
    private JButton getWeatherButton;
    private JLabel tempValue;
    private JLabel humidityValue;
    private JPanel mainPanel;
    private JPanel webPanel;
    private JFXPanel jfxPanel;
    private JFrame mainFrame;

    public WeatherGUI(WeatherService weatherService) {
        this.mainFrame = this;
        this.setVisible(true);
        this.setDefaultCloseOperation(EXIT_ON_CLOSE);
        this.add(mainPanel);
        jfxPanel = new JFXPanel();
        Platform.runLater(this::createJFXContent);
        webPanel.add(jfxPanel);
        this.pack();

        getWeatherButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                tempValue.setText(String.valueOf(weatherService.getWeather().main.temp));
                humidityValue.setText(String.valueOf(weatherService.getWeather().main.humidity));
                mainFrame.pack();
            }
        });
    }

    private void createJFXContent() {
        WebView webView = new WebView();
        webView.getEngine().load("http://stackoverflow.com/questions/42297864/javafx-webview-in-java-project");
        Scene scene = new Scene(webView);
        jfxPanel.setScene(scene);
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            new WeatherGUI(new WeatherService());
        });
    }
}
