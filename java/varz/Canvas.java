import javax.swing.*;
import java.awt.geom.*;//formatos
import java.util.Random;
import java.awt.*; //cores e graficos e texto

public class Canvas extends JComponent {

    double width, height;

    Rectangle2D.Double background;
    public Random random = new Random();
    float angle = 0;
    float radius = 100;
    float delta_angle = (float) 0.05;
    float delta_radius = (float) 0.05;

    double[] center = new double[2];
    int qt_points = 5;
    Point[] points = new Point[qt_points];

    public Canvas(int w, int h) {
        this.width = w;
        this.height = h;
        center[0] = this.width / 2;
        center[1] = this.height / 2;
        this.background = new Rectangle2D.Double(0, 0, this.width, this.height);
        this.CreatePoints();
    }

    void CreatePoints() {
        for (int i = 0; i < this.qt_points; i++) {
            double a = 360 / this.qt_points * i;
            double y = this.center[1] + (Math.sin(Math.toRadians(a)) * 300);
            double x = this.center[0] + (Math.cos(Math.toRadians(a)) * 300);
            this.points[i] = new Point(x, y, 20, a, true);
        }
    }

    void UpdatePoints() {
        for (int i = 0; i < this.qt_points; i++) {
            Point point = this.points[i];
            double x = this.center[0] + (Math.cos(Math.toRadians(point.start_angle + angle)) * 300);
            double y = this.center[1] + (Math.sin(Math.toRadians(point.start_angle + angle)) * 300);
            point.body.setFrame(x, y, point.radius, point.radius);
        }
    }

    void Background(Graphics2D g2d) {
        g2d.setPaint(Color.black);
        g2d.fill(this.background);
    }

    void DrawPoints(Graphics2D g2d) {
        for (Point point : this.points) {
            point.draw(g2d, Color.blue);
        }
    }

    @Override
    protected void paintComponent(Graphics g) {
        Graphics2D g2d = (Graphics2D) g;
        this.Background(g2d);
        this.UpdatePoints();
        this.DrawPoints(g2d);
        this.angle += 0.1;
        repaint();
    }

}