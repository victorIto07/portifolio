import java.awt.Graphics2D;
import java.awt.Color;
import java.awt.geom.Ellipse2D;
import java.util.Random;

public class Ball {
    final int radius = 10;

    Color color = Color.cyan;

    int max_width;
    int max_height;

    Ellipse2D.Double body;

    double x_vel;
    double y_vel = -.8;

    double gravity = 0.001;

    Random random = new Random();

    Ball(int max_w, int max_h) {
        this.max_width = max_w;
        this.max_height = max_h;
        this.body = new Ellipse2D.Double(this.max_width / 2 - this.radius, this.max_height / 2 - this.radius,
                this.radius * 2, this.radius * 2);
        double xv = 0.2;
        this.x_vel = random.nextBoolean() ? xv : xv * -1;
    }

    void Update() {
        if (this.body.x <= 0 || this.body.x + this.radius * 2 >= this.max_width)
            this.x_vel *= -1;
        this.y_vel += this.gravity;
        this.body.x += this.x_vel;
        this.body.y += this.y_vel;
    }

    public void Draw(Graphics2D g2d) {
        this.Update();
        g2d.setPaint(this.color);
        g2d.fill(this.body);
    }

}
