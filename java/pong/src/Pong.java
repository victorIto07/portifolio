import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

import javax.swing.*;

class Pong extends JFrame {
    int width;
    int height;

    MyCanvas canvas;

    Pong(int w, int h) {
        this.width = w;
        this.height = h;
        this.setTitle("My Pong");
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setResizable(false);
        this.canvas = new MyCanvas(this.width, this.height);
        this.add(this.canvas);
        this.setEventListener();
        this.pack();
        this.setVisible(true);
    }

    void setEventListener() {
        this.addKeyListener(new KeyListener() {

            @Override
            public void keyTyped(KeyEvent e) {
            }

            @Override
            public void keyPressed(KeyEvent e) {
                int code = e.getKeyCode();
                if (code == 87) {
                    canvas.player1.moveUp();
                }
                if (code == 83) {
                    canvas.player1.moveDown();
                }
                if (code == 38) {
                    canvas.player2.moveUp();
                }
                if (code == 40) {
                    canvas.player2.moveDown();
                }
                if (code == 32){
                    canvas.start();
                }
            }

            @Override
            public void keyReleased(KeyEvent e) {
                int code = e.getKeyCode();
                if (code == 87) {
                    canvas.player1.stopMoveUp();
                }
                if (code == 83) {
                    canvas.player1.stopMoveDown();
                }
                if (code == 38) {
                    canvas.player2.stopMoveUp();
                }
                if (code == 40) {
                    canvas.player2.stopMoveDown();
                }
            }

        });
    }

    public void run() {
        System.out.println("game is running");
    }
}