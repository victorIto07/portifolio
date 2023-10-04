import java.awt.*;
import java.awt.geom.*;
import java.util.Random;

public class Particle {

    double x_vel;
    double x_acc;
    double y_vel;
    double lifetime;
    double max_life;

    Ellipse2D.Double point;
    boolean finished = false;

    Random random = new Random();
    Color color;
    Transform t = new Transform();

    Particle(double x, double y, Color c) {
        this.max_life = 3 + this.random.nextDouble() * 4;
        this.lifetime = this.max_life;
        this.color = c;
        this.y_vel = -15 + this.random.nextDouble() * -10;
        this.x_vel = 5 + this.random.nextDouble() * 5;
        this.x_acc = this.random.nextDouble() * .05;
        this.point = new Ellipse2D.Double(x, y, 2, 2);
    }

    void update() {
        if (this.lifetime > 0) {
            this.lifetime -= .1;
            this.x_acc += 0.0015;
            this.x_vel += x_vel > 0 ? -x_acc : x_acc;
            this.y_vel += .5;
            this.point.x += this.x_vel;
            this.point.y += this.y_vel;
        } else
            this.finished = true;
    }

    void draw(Graphics2D g2d) {
        this.update();
        float alpha = (float) this.t.transform(0, this.max_life, 0, 1, this.lifetime);
        g2d.setComposite(AlphaComposite.getInstance(AlphaComposite.SRC_OVER, alpha < 0 ? 0 : alpha));
        g2d.fill(this.point);
    }
}
