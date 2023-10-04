import javax.swing.*;
import java.awt.*;
import java.awt.geom.*;

public class CanvasPong extends JPanel {

    int width;
    int height;

    Player player1;
    Player player2;

    Ball ball;

    Rectangle2D.Double background;

    int font_size = 30;
    Font monoFont = new Font("Monospaced", Font.BOLD
            | Font.ITALIC, font_size);

    CanvasPong(int w, int h) {
        this.width = w;
        this.height = h;
        this.setPreferredSize(new Dimension(this.width, this.height));
        this.setBounds(0, 0, this.width, this.height);
        this.background = new Rectangle2D.Double(0, 0, this.width, this.height);
        this.start();
        this.setFont(this.monoFont);
    }

    void start() {
        this.player1 = new Player(false, this.width, this.height);
        this.player2 = new Player(true, this.width, this.height);
        this.createBall();
    }

    void createBall() {
        this.ball = new Ball(this.width, this.height);
    }

    boolean checkColisions() {
        boolean collided = false;

        // collision for player 1
        if (this.ball.body.x < this.player1.body.x + this.player1.body_width
                && this.ball.body.x + this.ball.radius * 2 > this.player1.body.x
                && this.ball.body.y < this.player1.body.y + this.player1.body_height
                && this.ball.body.y + this.ball.radius * 2 > this.player1.body.y && this.ball.x_vel < 0) {
            double ball_center = this.ball.body.y + this.ball.radius;
            double p1_center = this.player1.body.x + this.player1.body_height * .5;
            if ((ball_center < p1_center && this.ball.y_vel < 0) || (ball_center >= p1_center && this.ball.y_vel > 0)) {
                this.ball.bounceY();
            }
            collided = true;
            this.ball.bounceX();
        }

        // collision for player 1
        if (this.ball.body.x + this.ball.radius * 2 > this.player2.body.x
                && this.ball.body.x < this.player2.body.x + this.player2.body_width
                && this.ball.body.y < this.player2.body.y + this.player2.body_height
                && this.ball.body.y + this.ball.radius * 2 > this.player2.body.y && this.ball.x_vel > 0) {
            double ball_center = this.ball.body.y + this.ball.radius;
            double p2_center = this.player2.body.x + this.player2.body_height * .5;
            if ((ball_center < p2_center && this.ball.y_vel < 0) || (ball_center >= p2_center && this.ball.y_vel > 0)) {
                this.ball.bounceY();
            }
            collided = true;
            this.ball.bounceX();
        }

        return collided;
    }

    void checkPoints() {
        if (this.ball.body.x < 0) {
            this.player2.getPoints();
            this.createBall();
        } else if (this.ball.body.x + this.ball.radius * 2 > this.width) {
            this.player1.getPoints();
            this.createBall();
        }
    }

    void drawPoints(Graphics g) {
        g.setFont(this.monoFont);
        String text = String.valueOf(this.player1.points);
        if (this.player2.points < this.player1.points)
            g.setColor(new Color(0, 255, 0));
        else if (this.player2.points > this.player1.points)
            g.setColor(new Color(255, 0, 0));
        else
            g.setColor(new Color(190, 190, 190));
        g.drawString(text, 0, this.font_size);
        text = String.valueOf(this.player2.points);
        if (this.player2.points > this.player1.points)
            g.setColor(new Color(0, 255, 0));
        else if (this.player2.points < this.player1.points)
            g.setColor(new Color(255, 0, 0));
        else
            g.setColor(new Color(190, 190, 190));
        g.drawString(text, this.width - font_size, this.font_size);
    }

    @Override
    public void paint(Graphics g) {
        Graphics2D g2d = (Graphics2D) g;
        this.PaintBackground(g2d);
        if (!this.checkColisions()) {
            this.checkPoints();
        }
        this.ball.draw(g2d);
        this.player1.draw(g2d);
        this.player2.draw(g2d);
        this.drawPoints(g);
        this.repaint();
    }

    void PaintBackground(Graphics2D g2d) {
        g2d.setPaint(new Color(0, 0, 0));
        g2d.fill(this.background);
    }
}
