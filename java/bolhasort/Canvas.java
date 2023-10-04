import javax.swing.*;
import java.awt.geom.*;//formatos
import java.lang.reflect.Array;
import java.text.MessageFormat;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Random;
import java.awt.*; //cores e graficos e texto

public class Canvas extends JComponent {

    int targetFps = 1000;
    long targetTime = 1000000000 / targetFps;

    long startTime;

    float width, height;

    Rectangle2D.Double background;
    public Random random = new Random();

    int qt = 300;
    Float[] arr = new Float[qt];

    float col_width;
    float padd = (float) 0;
    float height_step;
    Boolean finish = false;
    int current_index = 0;
    boolean swaped = false;

    public Canvas(int w, int h) {
        this.width = w;
        this.height = h;
        this.setPreferredSize(new Dimension(w, h));
        this.background = new Rectangle2D.Double(0, 0, this.width, this.height);
        this.col_width = (this.width / this.qt) - this.padd;
        this.height_step = (this.height - 50) / this.qt;
        for (int i = 0; i < this.qt; i++) {
            Array.set(this.arr, i, (i + 1) * this.height_step);
        }
        this.Shuffle();
        this.startTime = System.nanoTime();
    }

    @Override
    protected void paintComponent(Graphics g) {
        Graphics2D g2d = (Graphics2D) g;
        long startTime = System.nanoTime();
        g2d.setPaint(Color.black);
        g2d.fill(this.background);
        this.DrawRects(g2d);
        if (this.current_index < this.arr.length - 1) {
            // last usable index
            float v1 = this.arr[current_index];
            float v2 = this.arr[current_index + 1];
            boolean swap = v1 > v2;
            if (swap) {
                float step = v1;
                this.arr[current_index] = this.arr[current_index + 1];
                this.arr[current_index + 1] = step;
                this.swaped = true;
            }
            this.current_index++;
        } else {
            if (!this.swaped) {
                this.finish = true;
            } else {
                this.current_index = 0;
                this.swaped = false;
            }
        }
        long totalTime = System.nanoTime() - startTime;
        this.WaitTime(totalTime);
        if (!this.finish) {
            this.repaint();
        } else {
            this.DrawRects(g2d);
            long total_time = System.nanoTime() - this.startTime;
            System.out.println(MessageFormat.format("Finished in {0}", total_time / 1000));
        }
    }

    void WaitTime(long totalTime) {
        if (totalTime < targetTime) {
            try {
                Thread.sleep((targetTime - totalTime) / 1000000);
            } catch (Exception e) {

            }
        }
    }

    void DrawRects(Graphics2D g2d) {
        Rectangle2D.Float rec = new Rectangle2D.Float(0, 0, 0, 0);
        for (int i = 0; i < this.arr.length; i++) {
            Color c = this.finish ? new Color(0, 255, 0)
                    : (this.current_index == i ? new Color(255, 0, 0) : new Color(255, 255, 255));
            g2d.setPaint(c);
            Float v = this.arr[i];
            rec.setFrame(i * (this.col_width + this.padd), this.height - v,
                    this.col_width, v);
            g2d.fill(rec);
        }
    }

    void Shuffle() {
        List<Float> floatlist = Arrays.asList(this.arr);
        Collections.shuffle(floatlist);
        floatlist.toArray(this.arr);
    }

}