import java.awt.*;
import java.awt.geom.*;
import java.util.Random;

public class Point {
    Ellipse2D.Double body;
    double radius;
    double start_angle;
    double angle;
    int qt_points;
    Point[] orbit;
    double orbit_size = 50;
    double delta_angle;
    Random random = new Random();

    public Point(double x, double y, double r, double a, boolean gen_orbit) {
        this.radius = r;
        this.start_angle = a;
        this.qt_points = gen_orbit ? this.random.nextInt(1, 5) : 0;
        this.delta_angle = 0.1;//this.random.nextDouble(0.1, 0.5);
        this.orbit = new Point[this.qt_points];
        this.body = new Ellipse2D.Double(x - this.radius / 2, y - this.radius / 2, this.radius, this.radius);
        this.create_points();
    }

    void create_points() {
        for (int i = 0; i < this.qt_points; i++) {
            double a = 360 / this.qt_points * i;
            double x = this.body.x + (this.radius / 2) + (Math.cos(Math.toRadians(a)) * this.orbit_size);
            double y = this.body.y + (this.radius / 2) + (Math.sin(Math.toRadians(a)) * this.orbit_size);
            this.orbit[i] = new Point(x, y, this.radius / 2, a, false);
        }
    }

    void draw(Graphics2D g2d, Color c) {
        g2d.setPaint(c);
        g2d.fill(this.body);
        if (this.orbit.length > 0) {
            this.update_orbit();
            this.draw_orbit(g2d);
        }
    }

    void update_orbit() {
        this.angle += this.delta_angle;
        for (int i = 0; i < this.qt_points; i++) {
            Point point = this.orbit[i];
            double x = this.body.x + (this.radius / 2)
                    + (Math.cos(Math.toRadians(point.start_angle + this.angle * -1.5)) * this.orbit_size);
            double y = this.body.y + (this.radius / 2)
                    + (Math.sin(Math.toRadians(point.start_angle + this.angle * -1.5)) * this.orbit_size);
            point.body.setFrame(x, y, point.radius, point.radius);
        }
    }

    void draw_orbit(Graphics2D g2d) {
        for (Point p : this.orbit) {
            p.draw(g2d, Color.green);
        }
    }

}
