import javax.swing.*;
import java.awt.geom.*;//formatos
import java.util.ArrayList;
import java.util.Random;
import java.awt.*; //cores e graficos

public class Canvas extends JComponent {

    private double width;
    private double height;
    private double cell_size = 50;
    private double rows;
    private double cols;
    private boolean draw_lines = true;

    private ArrayList<ArrayList<ArrayList<Double>>> grid = new ArrayList<>();
    // cel = [x, y, w, h, i, j, color, alpha]

    Rectangle2D.Double background;
    public Random random = new Random();

    public Canvas(int w, int h) {
        this.width = w;
        this.height = h;
        this.rows = this.height / this.cell_size;
        this.cols = this.width / this.cell_size;
        this.CreateGrid();
        this.background = new Rectangle2D.Double(0, 0, this.width, this.height);
    }

    @Override
    protected void paintComponent(Graphics g) {
        Graphics2D g2d = (Graphics2D) g;
        g2d.setPaint(Color.white);
        g2d.fill(this.background);
        this.DrawGrid(g2d);
    }

    public void CreateGrid() {
        this.grid.clear();
        for (int i = 0; i < this.rows; i++) {
            this.grid.add(new ArrayList<>());
            for (int j = 0; j < this.cols; j++) {
                this.grid.get(i).add(new ArrayList<>());
                ArrayList<Double> cell = this.grid.get(i).get(j);
                cell.add(Double.valueOf(j) * this.cell_size);
                cell.add(Double.valueOf(i) * this.cell_size);
                cell.add(this.cell_size);
                cell.add(this.cell_size);
                cell.add(Double.valueOf(i));
                cell.add(Double.valueOf(j));
                double v = 0;
                // if (i == (int) this.rows / 2 && j == (int) this.cols / 2)
                v = this.random.nextDouble();
                cell.add(v);
            }
        }
    }

    void DrawGrid(Graphics2D g2d) {
        for (int i = 0; i < this.rows; i++) {
            this.grid.add(new ArrayList<>());
            for (int j = 0; j < this.cols; j++) {
                this.grid.get(i).add(new ArrayList<>());
                ArrayList<Double> cell = this.grid.get(i).get(j);
                Rectangle2D.Double cel = new Rectangle2D.Double(cell.get(0), cell.get(1), cell.get(2), cell.get(3));
                int a = this.v_map(0, 1, 0, 255, cell.get(6));
                g2d.setPaint(new Color(255, 0, 0, a));
                g2d.fill(cel);
                if (this.draw_lines && j > 0) {
                    g2d.setPaint(Color.black);
                    Line2D.Double y_line = new Line2D.Double(this.cell_size * j, 0, this.cell_size * j, this.height);
                    g2d.draw(y_line);
                }
            }
            if (this.draw_lines && i > 0) {
                Line2D.Double x_line = new Line2D.Double(0, this.cell_size * i, this.width, this.cell_size * i);
                g2d.draw(x_line);
            }
        }
    }

    int v_map(double start_val1, double end_val1, double start_val2, double end_val2, double samp) {
        double leftSpan = end_val1 - start_val1;
        double rightSpan = end_val2 - start_val2;

        double valueScaled = (samp - start_val1) / (leftSpan);

        return (int) Math.round(start_val2 + (valueScaled * rightSpan));
    }
}