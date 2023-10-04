import javax.swing.*;
import java.awt.*; //cores e graficos
import java.awt.geom.*; //cores e graficos
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Canvas extends JComponent {

    int fps = 60;
    long target_time = 1000000000 / fps;

    Double width;
    Double height;
    int n_cols = 100;
    Double larg_cols;
    Double dt_altura;

    Double padding = (double) 1;

    Double[] cols = new Double[n_cols];

    Rectangle2D.Double background;

    public Canvas(int w, int h) {
        this.width = (double) w;
        this.height = (double) h;
        this.larg_cols = this.width / (double) this.n_cols;
        this.dt_altura = (this.height - 50) / this.n_cols;
        this.background = new Rectangle2D.Double(0, 0, this.width, this.height);
        this.CriarLista();
    }

    void CriarLista() {
        for (double i = 1; i <= this.n_cols; i++) {
            this.cols[(int) i - 1] = i;
        }
        List<Double> DoubleList = Arrays.asList(this.cols);
        Collections.shuffle(DoubleList);
        DoubleList.toArray(this.cols);
    }

    void Background(Graphics2D g2d) {
        g2d.setPaint(Color.black);
        g2d.fill(this.background);
    }

    @Override
    protected void paintComponent(Graphics g) {
        Graphics2D g2d = (Graphics2D) g;
        this.Background(g2d);
        // this.DesenharColunas(g2d);
        this.quickSort(this.cols, 0, this.cols.length - 1, g2d);
    }

    void swap(Double[] arr, int i, int j) {
        Double temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    int partition(Double[] arr, int low, int high, Graphics2D g2d) {
        Double pivot = arr[high];
        int i = (low - 1);

        for (int j = low; j <= high - 1; j++) {
            if (arr[j] < pivot) {
                i++;
                swap(arr, i, j);
            }
        }
        swap(arr, i + 1, high);
        return (i + 1);
    }

    void quickSort(Double[] arr, int low, int high, Graphics2D g2d) {
        long start = System.nanoTime();
        if (low < high) {
            int pi = partition(arr, low, high, g2d);
            this.DesenharColunas(g2d);
            this.WaitTime(System.nanoTime() - start);
            quickSort(arr, low, pi - 1, g2d);
            quickSort(arr, pi + 1, high, g2d);
        }
    }

    void DesenharColunas(Graphics2D g2d) {
        g2d.setPaint(Color.red);
        Rectangle2D.Double col = new Rectangle2D.Double(0, 0, 0, 0);
        for (int i = 0; i < this.n_cols; i++) {
            Double v = this.cols[i];
            Double col_h = v * this.dt_altura;
            col.setFrame(i * this.larg_cols, this.height - (col_h), this.larg_cols - this.padding, col_h);
            g2d.fill(col);
        }
    }

    void WaitTime(long totalTime) {
        if (totalTime < this.target_time) {
            try {
                Thread.sleep((this.target_time - totalTime) / 1000000);
            } catch (Exception e) {

            }
        }
    }
}