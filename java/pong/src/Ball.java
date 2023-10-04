import java.awt.*;
import java.awt.geom.*;
import java.util.Random;

public class Ball {

    int max_width;
    int max_height;

    Ellipse2D.Double body;
    double radius = 10;

    double x_vel;
    double y_vel;

    Random random = new Random();

    Ball(int w, int h) {
        this.max_width = w;
        this.max_height = h;
        this.body = new Ellipse2D.Double(this.max_width / 2 - this.radius, this.max_height / 2 - this.radius,
                this.radius * 2, this.radius * 2);
        double xv = .2;
        double yv = this.random.nextDouble() * .5;
        if (this.random.nextBoolean())
            xv *= -1;
        if (this.random.nextBoolean())
            yv *= -1;
        this.x_vel = xv;
        this.y_vel = yv;
    }

    void update() {
        // if (this.body.x + this.radius * 2 > this.max_width - 1 || this.body.x < 1)
        // this.bounceX();
        if (this.body.y + this.radius * 2 > this.max_height - 1 || this.body.y < 1)
            this.bounceY();
        this.body.x += this.x_vel;
        this.body.y += this.y_vel;
    }

    void bounceX() {
        this.x_vel += this.x_vel < 0 ? -.05 : .05;
        this.x_vel *= -1;
    }

    void bounceY() {
        this.y_vel *= -1;
    }

    public void draw(Graphics2D g2d) {
        this.update();
        g2d.setPaint(new Color(255, 0, 0));
        g2d.fill(this.body);
    }
}
