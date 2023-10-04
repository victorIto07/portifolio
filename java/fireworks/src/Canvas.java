import javax.swing.*;
import javax.swing.plaf.DimensionUIResource;

import java.awt.*;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.util.ArrayList;
import java.util.Random;

public class Canvas extends JComponent {

    int fps = 60;
    long expected_time = 1000000000 / fps;

    int width;
    int height;

    Random random = new Random();

    ArrayList<Firework> fireworks = new ArrayList<>();

    Rectangle background;
    int frame_count = 0;

    Canvas(int width, int height) {
        this.width = width;
        this.height = height;
        this.setPreferredSize(new DimensionUIResource(this.width, this.height));
        this.background = new Rectangle(0, 0, this.width, this.height);
        this.addListeners();
    }

    void addListeners() {
        this.addMouseListener(new MouseListener() {

            @Override
            public void mouseClicked(MouseEvent e) {
            }

            @Override
            public void mousePressed(MouseEvent e) {
                java.awt.Point p = e.getPoint();
                addFirework(p.x, p.y);
            }

            @Override
            public void mouseReleased(MouseEvent e) {
            }

            @Override
            public void mouseEntered(MouseEvent e) {
            }

            @Override
            public void mouseExited(MouseEvent e) {
            }

        });
    }

    void addFirework(int x, int y) {
        this.fireworks.add(new Firework((double) x, (double) y));
        this.repaint();
    }

    void drawFireworks(Graphics2D g2d) {
        long start = System.nanoTime();
        for (int i = this.fireworks.size() - 1; i > -1; i--) {
            Firework f = this.fireworks.get(i);
            if (f.finished)
                this.fireworks.remove(f);
            else
                f.draw(g2d);
        }
        long totalTime = System.nanoTime() - start;
        this.WaitTime(totalTime);
        this.repaint();
    }

    @Override
    public void paint(Graphics g) {
        this.frame_count++;
        if (this.frame_count % 10 == 0)
            this.addFirework(100 + this.random.nextInt(this.width - 100), this.height+10);
        Graphics2D g2d = (Graphics2D) g;
        g2d.setPaint(new Color(0, 0, 0));
        g2d.fill(this.background);
        this.drawFireworks(g2d);
    }

    void WaitTime(long totalTime) {
        if (totalTime < expected_time) {
            try {
                Thread.sleep((expected_time - totalTime) / 1000000);
            } catch (Exception e) {

            }
        }
    }
}
