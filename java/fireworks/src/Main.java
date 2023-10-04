import javax.swing.*;

/*
 * ------------------------------------------------|
 *                                                 |
 *   TRYING TO MESS WITH PARTICLES AND VELOCITY    |
 *                                                 |
 * ------------------------------------------------|
 */

public class Main {
    public static void main(String[] args) {
        int width = 1900;
        int height = 1000;
        JFrame frame = new JFrame();
        Canvas canvas = new Canvas(width, height);
        frame.add(canvas);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setBounds(10, 0, width, height);
        frame.setResizable(false);
        frame.pack();
        frame.setVisible(true);
    }
}