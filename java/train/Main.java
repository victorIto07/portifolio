import java.awt.event.*;

import javax.swing.*;

public class Main {
    public static void main(String[] args) {
        int width = 950;
        int height = 950;
        JFrame frame = new JFrame();
        Canvas canvas = new Canvas(width, height);
        frame.addKeyListener(new KeyListener() {

            @Override
            public void keyTyped(KeyEvent e) {
            }

            @Override
            public void keyPressed(KeyEvent e) {
                if (e.getKeyCode() == 40) {
                    canvas.CreateGrid();
                    canvas.repaint();
                }
            }

            @Override
            public void keyReleased(KeyEvent e) {
            }
        });
        frame.setSize(width, height);
        frame.setTitle("Teste");
        frame.add(canvas);
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setVisible(true);
    }
}