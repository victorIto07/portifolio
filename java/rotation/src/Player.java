import java.awt.Graphics2D;
import java.awt.Color;

public class Player {

    int[] position = new int[2];
    double angle = 0;
    int width = 50;
    int height = 50;

    boolean turn_left = false;
    boolean turn_right = false;

    double acc = 0;
    double speed = 0;

    Player(int x, int y) {
        this.position[0] = x;
        this.position[1] = y;
    }

    public void draw(Graphics2D g2d) {
        this.update();
        g2d.translate(this.position[0], this.position[1]);
        g2d.rotate(Math.toRadians(this.angle));
        this.drawArrow(g2d);
        this.drawRect(g2d);
        g2d.translate(this.position[0] * -1, this.position[1] * -1);
    }

    void update() {
        this.speed += this.acc;
        this.position[0] += Math.cos(Math.toRadians(this.angle)) * this.speed;
        this.position[1] += Math.sin(Math.toRadians(this.angle)) * this.speed;
        if (this.turn_right)
            this.angle += 6;
        if (this.turn_left)
            this.angle += -6;

    }

    void drawRect(Graphics2D g2d) {
        g2d.setPaint(Color.red);
        g2d.drawRect(this.width / -2, this.height / -2, this.width, this.height);
    }

    public void drawArrow(Graphics2D g2d) {
        g2d.setPaint(Color.green);
        g2d.drawLine(0, 0, 50, 0);
    }

    public void move() {
        this.acc = .1;
    }

    public void stopMove() {
        this.acc = 0;
    }

    public void break_() {
        this.acc = -.1;
    }

    public void stopBreak_() {
        this.acc = 0;
    }

    public void turnRight() {
        this.turn_right = true;
    }

    public void turnLeft() {
        this.turn_left = true;
    }

    public void stopTurnRight() {
        this.turn_right = false;
    }

    public void stopTurnLeft() {
        this.turn_left = false;
    }

    double translate(double l1, double l2, double r1, double r2, double v) {
        double l_off = l2 - l1;
        double r_off = r2 - r1;

        double p = (v - l1) / l_off;

        return r1 + (p * r_off);
    }
}
