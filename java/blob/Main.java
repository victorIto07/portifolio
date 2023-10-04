import javax.swing.*;

public class Main {
    public static void main(String[] args) {
        int width = 1000;
        int height = 1000;
        JFrame frame = new JFrame();
        Canvas canvas = new Canvas(width, height);
        frame.setSize(width, height);
        frame.setTitle("Boublesort");
        frame.add(canvas);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
}