import javax.swing.*;

public class Main {
    public static void main(String[] args) {
        int width = 960;
        int height = 540;
        JFrame frame = new JFrame();
        Canvas canvas = new Canvas(width, height);
        frame.setSize(width, height);
        frame.setTitle("Boublesort - 2");
        frame.add(canvas);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setBounds(0, 0, width, height);
        frame.pack();
        frame.setResizable(false);
        frame.setVisible(true);
    }
}