import javax.swing.*;
import java.awt.event.*;
public class Main extends JFrame {

    public static void main(String[] args) {
        int width = 960;
        int height = 540;
        JFrame frame = new JFrame();
        MyCanvas canvas = new MyCanvas(width, height);
        frame.addKeyListener(new KeyListener() {
            @Override
            public void keyTyped(KeyEvent e) {
            }

            @Override
            public void keyPressed(KeyEvent e) {
                int k = e.getKeyCode();
                if (k == 32) {
                    canvas.CreateCols();
                } else if (k == 39) {
                    canvas.Sort();
                }
                // System.out.println(k);
            }

            @Override
            public void keyReleased(KeyEvent e) {
            }
        });
        frame.setTitle("Inserirsort");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setResizable(false);
        frame.setBounds(960, 0, width, height);

        frame.add(canvas);
        frame.pack();
        frame.setVisible(true);
    }
}