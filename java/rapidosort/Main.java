import javax.swing.*;

public class Main {
    public static void main(String[] args) {
        int width = 1000;
        int height = 900;
        JFrame frame = new JFrame();
        Canvas canvas = new Canvas(width, height);
        frame.setSize(width, height);
        frame.setTitle("Rapidosort");
        frame.add(canvas);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
}