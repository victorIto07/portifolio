import javax.swing.*;

public class Main {
    public static void main(String[] args) {
        int width = 1500;
        int height = 900;
        JFrame frame = new JFrame();
        Canvas canvas = new Canvas(width, height);
        frame.setSize(width, height);
        frame.setTitle("Boublesort");
        frame.add(canvas);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.pack();
        frame.setResizable(false);
        frame.setVisible(true);
    }
}