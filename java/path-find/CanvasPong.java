import javax.swing.*;
import java.awt.geom.*;//formatos
import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Random;
import java.awt.*; //cores e graficos e texto

public class CanvasPong extends JComponent {

    int width, height;
    int qt_points = 10;
    Float[][] points = new Float[qt_points][2];
    Float[][] best_points = new Float[qt_points][2];
    float best_length = -1;
    public int tries = 0;

    Rectangle2D.Double background;
    public Random random = new Random();

    public CanvasPong(int w, int h) {
        this.width = w;
        this.height = h;
        this.background = new Rectangle2D.Double(0, 0, this.width, this.height);
        for (int i = 0; i < this.qt_points; i++) {
            Array.set(this.points, i, new Float[2]);
        }
        for (Float[] pos : this.points) {
            Array.set(pos, 0, this.random.nextFloat() * this.width);
            Array.set(pos, 1, this.random.nextFloat() * this.height);
        }
    }

    @Override
    protected void paintComponent(Graphics g) {
        Graphics2D g2d = (Graphics2D) g;
        g2d.setPaint(Color.black);
        g2d.fill(this.background);
        this.Shuffle();
        float length = this.DrawLines(g2d);
        this.DrawBestLines(g2d);
        if (this.best_length == -1 || (length < this.best_length)) {
            this.best_length = length;
            this.best_points = this.points.clone();
        }
        this.DrawPoints(g2d);
        this.tries++;
        this.repaint();
    }

    void DrawPoints(Graphics2D g2d) {
        g2d.setPaint(Color.red);
        for (Float[] pos : this.points) {
            Ellipse2D.Float point = new Ellipse2D.Float(pos[0], pos[1], 10, 10);
            g2d.fill(point);
        }
    }

    float DrawLines(Graphics2D g2d) {
        float length = 0;
        for (int i = 0; i < this.qt_points - 1; i++) {
            Float[] p1 = this.points[i];
            Float[] p2 = this.points[i + 1];
            float dx = p1[0] > p2[0] ? p1[0] - p2[0] : p2[0] - p1[0];
            float dy = p1[1] > p2[1] ? p1[1] - p2[1] : p2[1] - p1[1];
            length += Math.sqrt((Math.pow(dx, 2) + Math.pow(dy, 2)));
            this.DrawLine(g2d, p1, p2);
        }
        return length;
    }

    void DrawBestLines(Graphics2D g2d) {
        for (int i = 0; i < this.qt_points - 1; i++) {
            Float[] p1 = this.best_points[i];
            Float[] p2 = this.best_points[i + 1];
            if (p1[0] == null) {
                return;
            }
            this.DrawBestLine(g2d, p1, p2);
        }
    }

    void DrawLine(Graphics2D g2d, Float[] p1, Float[] p2) {
        g2d.setPaint(Color.blue);
        Line2D.Float line = new Line2D.Float(p1[0] + 5, p1[1] + 5, p2[0] + 5, p2[1] + 5);
        g2d.draw(line);
    }

    void DrawBestLine(Graphics2D g2d, Float[] p1, Float[] p2) {
        g2d.setPaint(Color.MAGENTA);
        g2d.setStroke(new BasicStroke(3));
        Line2D.Float line = new Line2D.Float(p1[0] + 5, p1[1] + 5, p2[0] + 5, p2[1] + 5);
        g2d.draw(line);
    }

    void Shuffle() {
        List<Float[]> floatlist = Arrays.asList(this.points);
        Collections.shuffle(floatlist);
        floatlist.toArray(this.points);
    }

}