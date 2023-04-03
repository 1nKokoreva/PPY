import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import javax.swing.JFrame;
import javax.swing.JPanel;

public class Swing extends JPanel {
    private static final long serialVersionUID = 1L;

    private double a = Math.toRadians(45); // początkowy kąt odchylenia wahadła
    private double r = 100; // długość wahadła
    private double dt = 0.005f; // krok w czasie
    private double g = -10;
    private double m = 1; //masa
    private double w = 0; //początkowa prędkość kątowa wahadła

    public Swing() {
        setPreferredSize(new Dimension(600, 400));
    }

    public void start() {
        while (true) {
            // mid-point method implementation
            double e = (g / r) * Math.sin(a);

            double w_2 = w + e * dt / 2;
            double a_2 = a + w * dt / 2;
            double e_2 = g / r * Math.sin(a_2);

            double da = w_2 * dt;
            double dw = e_2 * dt;

            a += da;
            w += dw;

            // repaint the panel to show the updated position
            repaint();

            try {
                Thread.sleep(10);
            } catch (InterruptedException e1) {
                e1.printStackTrace();
            }
        }
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);

        int centerX = getWidth() / 2;
        int centerY = getHeight() / 2;

        double x = centerX + r * Math.sin(a);
        double y = centerY + r * Math.cos(a);

        g.setColor(Color.BLACK);
        g.drawLine(centerX, centerY, (int) x, (int) y);
        g.setColor(Color.RED);
        g.fillOval((int) x - 10, (int) y - 10, 20, 20);
    }

    public static void main(String[] args) {
        Swing pendulum = new Swing();
        JFrame frame = new JFrame("Pendulum");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setContentPane(pendulum);
        frame.pack();
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);
        pendulum.start();
    }
}

