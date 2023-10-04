import javax.swing.*;

/*
 * ---------------------------------------------------------|                                              |
 *                                                          |
 *   A n POINT SISTEM TRYING TO FIND IT'S SHORTEST PATH     |
 *                                                          |
 * ---------------------------------------------------------|
 */


public class Main {
    public static void main(String[] args) {
        int width = 950;
        int height = 950;
        JFrame frame = new JFrame();
        CanvasPong canvas = new CanvasPong(width, height);
        frame.setSize(width, height);
        frame.setTitle("Teste");
        frame.add(canvas);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
}
