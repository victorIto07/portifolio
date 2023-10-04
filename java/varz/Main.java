import javax.swing.*;

public class Main {
    public static void main(String[] args) {
        int width = 1500;
        int height = 900;
        JFrame frame = new JFrame();
        MyCanvas canvas = new MyCanvas(width, height);
        frame.setSize(width, height);
        frame.setTitle("Varz");
        frame.add(canvas);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
}