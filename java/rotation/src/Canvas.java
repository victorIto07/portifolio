import javax.swing.*;
import java.awt.*;

public class Canvas extends JComponent {

    int width;
    int height;

    Graphics2D g2d;

    Player p;

    double angle = 0;

    int fps = 60;
    long waitTime = 1000 / fps;

    Canvas(int w, int h) {
        this.width = w;
        this.height = h;
        this.setPreferredSize(new Dimension(this.width, this.height));
        this.p = new Player(this.width / 2, this.width / 2);
    }

    @Override
    public void paint(Graphics g) {
        long startTime = System.nanoTime();
        this.g2d = (Graphics2D) g;
        // this.p.angle = (this.p.angle + 1) % 360;
        this.p.draw(this.g2d);
        long durationTime = (System.nanoTime() - startTime) / 1000000;
        long wait = this.waitTime - durationTime;
        this.waitTime(wait);
        this.repaint();
    }

    void waitTime(long time) {
        try {
            Thread.sleep(time);
        } catch (Exception e) {
        }
    }
}
