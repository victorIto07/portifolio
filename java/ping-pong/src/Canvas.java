import javax.swing.*;
import java.awt.*;
import java.awt.geom.*;
import java.util.Random;

public class Canvas extends JPanel {

    int width;
    int height;

    Graphics2D g2d;
    Player player;
    Ball ball;

    Random random = new Random();

    int max_points = 0;

    boolean cheat = false;

    Canvas(int w, int h) {
        this.width = w;
        this.height = h;
        this.setFont(new Font("Monospaced", Font.BOLD
                | Font.ITALIC, 30));
        this.setPreferredSize(new Dimension(this.width, this.height));
        this.player = new Player(this.width, this.height);
        this.CreateBall();
    }

    void CreateBall() {
        this.ball = new Ball(this.width, this.height);
    }

    void PaintBackground() {
        this.g2d.setPaint(Color.black);
        this.g2d.fillRect(0, 0, this.width, this.height);
    }

    boolean CheckCollision() {
        return (this.ball.body.y + this.ball.radius * 2 >= this.height - this.player.body_height &&
                this.ball.body.y <= this.height &&
                this.ball.body.x + this.ball.radius * 2 >= this.player.body.x &&
                this.ball.body.x <= this.player.body.x + this.player.body_width);
    }

    void DrawPoints() {
        Color c = this.player.points > this.max_points ? Color.green
                : (this.player.points < this.max_points ? Color.red : Color.white);
        this.g2d.setColor(c);
        this.g2d.drawString(String.valueOf(this.player.points), 0, 30);
        this.g2d.setColor(Color.white);
        this.g2d.drawString(String.valueOf(this.max_points), 0, 70);
    }

    @Override
    public void paint(Graphics g) {
        this.g2d = (Graphics2D) g;
        this.g2d.setFont(this.getFont());
        this.PaintBackground();
        this.player.Draw(this.g2d);
        this.ball.Draw(this.g2d);
        this.DrawPoints();
        if (this.cheat) {
            if (this.ball.body.x + this.ball.radius > this.player.body.x + this.player.body_width / 2
                    && this.player.body.x + this.player.body_width < this.width)
                this.player.body.x += 1;
            if (this.ball.body.x + this.ball.radius < this.player.body.x + this.player.body_width / 2
                    && this.player.body.x > 0)
                this.player.body.x += -1;
        }
        if (this.ball.y_vel > 0 && this.CheckCollision()) {
            if (this.random.nextInt(0, 2) == 0)
                this.ball.x_vel *= -1;
            this.ball.y_vel *= -1;
            this.player.points++;
            if ((this.player.points % 5) == 0)
                this.ball.x_vel += this.ball.x_vel < 0 ? -0.05 : 0.05;
        } else if (this.ball.body.y > this.height) {
            if (this.player.points > this.max_points)
                this.max_points = this.player.points;
            this.player.points = 0;
            this.CreateBall();
        }
        this.repaint();
    }
}
