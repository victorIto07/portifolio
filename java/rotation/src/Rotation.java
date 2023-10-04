import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

import javax.swing.*;

public class Rotation extends JFrame {
    int width = 900;
    int height = 900;

    MyCanvas canvas;

    Rotation() {
        this.canvas = new MyCanvas(this.width, this.height);
        this.setListeners();
        this.add(this.canvas);
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setResizable(false);
        this.pack();
        this.setVisible(true);
    }

    void setListeners() {
        this.addKeyListener(new KeyListener() {

            @Override
            public void keyTyped(KeyEvent e) {
            }

            @Override
            public void keyPressed(KeyEvent e) {
                int code = e.getKeyCode();
                switch (code) {
                    case 38:
                        canvas.p.move();
                        break;
                    case 87:
                        canvas.p.move();
                        break;
                    case 37:
                        canvas.p.turnLeft();
                        break;
                    case 65:
                        canvas.p.turnLeft();
                        break;
                    case 39:
                        canvas.p.turnRight();
                        break;
                    case 68:
                        canvas.p.turnRight();
                        break;
                    case 40:
                        canvas.p.break_();
                        break;
                    case 83:
                        canvas.p.break_();
                        break;
                }
            }

            @Override
            public void keyReleased(KeyEvent e) {
                int code = e.getKeyCode();
                switch (code) {
                    case 38:
                        canvas.p.stopMove();
                        break;
                    case 87:
                        canvas.p.stopMove();
                        break;
                    case 37:
                        canvas.p.stopTurnLeft();
                        break;
                    case 65:
                        canvas.p.stopTurnLeft();
                        break;
                    case 39:
                        canvas.p.stopTurnRight();
                        break;
                    case 68:
                        canvas.p.stopTurnRight();
                        break;
                    case 40:
                        canvas.p.stopBreak_();
                        break;
                    case 83:
                        canvas.p.stopBreak_();
                        break;
                }
            }

        });
    }
}
