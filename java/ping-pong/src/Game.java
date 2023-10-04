import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;

import javax.swing.*;

public class Game extends JFrame {

    final int width = 800;
    final int height = 800;

    MyCanvas canvas;

    Game() {
        this.canvas = new MyCanvas(this.width, this.height);
        this.add(this.canvas);
        this.pack();
        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setTitle("Ping Pong");
        this.setResizable(false);
        this.setListeners();
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
                    case 68:
                        canvas.player.MoveRight();
                        break;

                    case 65:
                        canvas.player.MoveLeft();
                        break;
                    
                    case 32:
                        canvas.cheat = !canvas.cheat;
                }
            }

            @Override
            public void keyReleased(KeyEvent e) {
                int code = e.getKeyCode();
                switch (code) {
                    case 68:
                        canvas.player.StopMoveRight();
                        break;

                    case 65:
                        canvas.player.StopMoveLeft();
                        break;
                }
            }

        });
    }

    public void Run() {
    }
}
