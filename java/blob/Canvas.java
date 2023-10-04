import javax.swing.*;
import java.awt.geom.*;//formatos
import java.lang.reflect.Array;
import java.util.Random;
import java.awt.*; //cores e graficos e texto

public class Canvas extends JComponent {

    int targetFps = -1;
    long targetTime = 1000000000 / targetFps;

    double width, height;

    Rectangle2D.Double background;
    public Random random = new Random();

    int step = 12;
    double radius = 150;

    double[][] points = new double[360 / step][3];
    double[] center = new double[2];

    public Canvas(int w, int h) {
        this.width = w;
        this.height = h;
        this.center[0] = this.width / 2;
        this.center[1] = this.height / 2;
        this.background = new Rectangle2D.Double(0, 0, this.width, this.height);
        this.CreateBlob();
    }

    void CreateBlob() {
        for (int i = 0; i < this.points.length; i++) {
            double a = i * this.step;
            double r;
            if (i == 0) {
                r = this.radius + (this.random.nextFloat() < 0.5 ? this.random.nextDouble() * 25
                        : this.random.nextDouble() * -25);
            } else {
                r = this.points[i - 1][2] + (this.random.nextFloat() < 0.5 ? this.random.nextDouble() * 5
                        : this.random.nextDouble() * -5);
            }
            double[] pos = {
                    this.center[0] + (Math.cos(Math.toRadians(a)) * r),
                    this.center[1] + (Math.sin(Math.toRadians(a)) * r),
                    r
            };
            Array.set(this.points, i, pos);
        }
    }

    void UpdateBlob() {
        for (int i = 0; i < this.points.length; i++) {
            double a = i * this.step;
            double r;
            if (i == 0) {
                r = this.points[this.points.length - 1][2]
                        + (this.random.nextFloat() < 0.5 ? this.random.nextDouble() * 5
                                : this.random.nextDouble() * -5);
            } else {
                r = this.points[i - 1][2] + (this.random.nextFloat() < 0.5 ? this.random.nextDouble() * 5
                        : this.random.nextDouble() * -5);
            }
            double[] pos = {
                    this.center[0] + (Math.cos(Math.toRadians(a)) * r),
                    this.center[1] + (Math.sin(Math.toRadians(a)) * r),
                    r
            };
            Array.set(this.points, i, pos);
        }
    }

    @Override
    protected void paintComponent(Graphics g) {
        Graphics2D g2d = (Graphics2D) g;
        long startTime = System.nanoTime();
        g2d.setPaint(Color.black);
        g2d.fill(this.background);
        this.UpdateBlob();
        this.DrawBlob(g2d);
        this.WaitTime(startTime);
        this.repaint();
    }

    void DrawBlob(Graphics2D g2d) {
        g2d.setColor(Color.red);
        for (int i = 0; i < this.points.length; i++) {
            double[] p1 = this.points[i];
            double[] p2 = i == this.points.length - 1 ? this.points[0] : this.points[i + 1];
            Line2D.Double line = new Line2D.Double(p1[0], p1[1], p2[0], p2[1]);
            g2d.draw(line);
        }
    }

    void WaitTime(long startTime) {
        long totalTime = System.nanoTime() - startTime;
        if (totalTime < targetTime && this.targetFps > -1) {
            try {
                Thread.sleep((targetTime - totalTime) / 1000000);
            } catch (Exception e) {

            }
        }
    }

}