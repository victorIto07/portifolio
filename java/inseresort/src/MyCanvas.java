import javax.swing.*;

import java.awt.*;
import java.awt.geom.*;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class MyCanvas extends JComponent {

    int target_fps = 1000;
    long target_time = 1000000000 / target_fps;// NANOSECONDS

    double width;
    double height;

    Rectangle2D.Double background;
    Rectangle2D.Double col = new Rectangle2D.Double(0, 0, 0, 0);

    Double[] cols;
    int qt_cols = 300;
    double col_size;
    double ratio;

    boolean sort = false;
    int current_index = 1;
    int max_index = 1;
    boolean finished = false;

    public MyCanvas(int w, int h) {
        this.width = (double) w;
        this.height = (double) h;
        this.ratio = (this.height - 50) / this.qt_cols;
        this.col_size = this.width / this.qt_cols;
        this.setPreferredSize(new Dimension(w, h));
        this.background = new Rectangle2D.Double(0, 0, this.width, this.height);
        this.CreateCols();
    }

    public void CreateCols() {
        this.current_index = 1;
        this.max_index = 1;
        this.finished = false;
        this.cols = new Double[this.qt_cols];
        this.sort = false;
        for (int i = 0; i < this.qt_cols; i++) {
            this.cols[i] = (double) i + 1;
        }
        this.Shuffle();
        this.sort = true;
    }

    public void Shuffle() {
        List<Double> c = Arrays.asList(this.cols);
        Collections.shuffle(c);
        c.toArray(this.cols);
        repaint();
    }

    void DrawCols(Graphics2D g2d) {
        for (int i = 0; i < this.qt_cols; i++) {
            double v = this.cols[i] * this.ratio;
            g2d.setPaint(this.finished ? new Color(0, 255, 0)
                    : (i == this.current_index && this.sort) ? new Color(255, 0, 0) : new Color(255, 255, 255));
            this.col.setFrame(i * this.col_size, this.height - v, this.col_size, v);
            g2d.fill(this.col);
        }
    }

    void Sort() {
        // for (int i = 1; i < this.qt_cols; i++) {
        // this.SortStep(i);
        // }
        // System.out.println("Finish");
        this.sort = true;
        this.repaint();
    }

    boolean SortStep(int index) {
        // long start = System.nanoTime();
        double value = this.cols[index];
        double prev_value = this.cols[index - 1];
        boolean swap = value < prev_value;
        if (swap)
            this.Swap(this.cols, index, index - 1);
        return swap;
    }

    void Swap(Double[] arr, int i1, int i2) {
        double step = arr[i1];
        arr[i1] = arr[i2];
        arr[i2] = step;
    }

    @Override
    public void paint(Graphics g) {
        long start = System.nanoTime();
        Graphics2D g2d = (Graphics2D) g;
        g2d.setPaint(new Color(0, 0, 0));
        g2d.fill(this.background);
        this.DrawCols(g2d);
        if (this.sort) {
            boolean swapped = this.SortStep(this.current_index);
            if (swapped) {
                if (this.current_index < 2) {
                    this.max_index++;
                    this.current_index = this.max_index;
                } else
                    this.current_index--;
            } else {
                this.max_index++;
                this.current_index = this.max_index;
            }
            long total_time = System.nanoTime() - start;
            if (total_time < this.target_time)
                this.WaitTime((this.target_time - total_time) / 1000000);
            this.repaint();
            if (this.max_index == this.qt_cols) {
                System.out.println("Finish!");
                this.sort = false;
                this.finished = true;
                repaint();
            }
        }
    }

    void WaitTime(long time) {
        try {
            Thread.sleep(time);
        } catch (Exception e) {

        }
    }

}
