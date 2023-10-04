import java.awt.*;
import java.awt.geom.*;
import java.util.Random;

public class Firework {

    double x_vel = 0;
    double y_vel = 0;
    double size = 10;
    boolean exploded = false;
    Color color;
    boolean finished = false;

    Ellipse2D.Double point;
    double lifetime;

    int qt_particles;
    Particle[] particles;
    Random random = new Random();

    Firework(double x, double y) {
        this.color = new Color(100 + this.random.nextInt(155), 100 + this.random.nextInt(155),
                100 + this.random.nextInt(155));
        this.lifetime = 5 + this.random.nextDouble() * 8;
        this.point = new Ellipse2D.Double(x - (this.size / 2), y - (this.size / 2), this.size / 2, this.size);
        this.qt_particles = 50 + this.random.nextInt(50);
        this.particles = new Particle[this.qt_particles];
    }

    void update() {
        if (!this.exploded) {
            this.lifetime -= 0.1;
            this.y_vel -= .1;
            this.point.x += this.x_vel;
            this.point.y += this.y_vel;
            if (this.lifetime < 0)
                this.explode();
        }
    }

    void draw(Graphics2D g2d) {
        g2d.setPaint(this.color);
        if (!this.exploded) {
            this.update();
            g2d.setComposite(AlphaComposite.getInstance(AlphaComposite.SRC_OVER, 1));
            g2d.fill(this.point);
        } else {
            boolean end = true;
            for (Particle p : this.particles) {
                if (!p.finished) {
                    p.draw(g2d);
                    end = false;
                }
            }
            if (end) {
                this.finished = true;
            }
        }
    }

    void explode() {
        this.exploded = true;
        for (int i = 0; i < this.qt_particles; i++) {
            this.particles[i] = new Particle(this.point.x, this.point.y, this.color);
        }
    }
}
