import javax.swing.*;

public class Main {
    public static void main(String[] args) {
        int width = 950;
        int height = 950;
        JFrame frame = new JFrame();
        CanvasPong canvas = new CanvasPath(width, height);
        frame.setSize(width, height);
        frame.setTitle("Teste");
        frame.add(canvas);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
}
