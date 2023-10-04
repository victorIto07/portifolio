import java.awt.Graphics2D;
import java.awt.Color;
import java.awt.geom.Rectangle2D;

public class Player {

    int max_width;

    final Color body_color = Color.magenta;
    final int body_width = 220;
    final int body_height = 30;

    Rectangle2D.Double body;

    boolean move_right = false;
    boolean move_left = false;

    int points = 0;

    Player(int max_w, int max_h) {
        this.max_width = max_w;
        this.body = new Rectangle2D.Double(0, max_h - this.body_height, this.body_width, this.body_height);
    }

    public void Draw(Graphics2D g2d) {
        int speed = 0;
        if (this.move_right)
            speed += 1;
        if (this.move_left)
            speed += -1;
        if ((speed > 0 && this.body.x + this.body_width >= this.max_width) || (speed < 0 && this.body.x <= 0))
            speed = 0;
        this.body.x += speed;
        g2d.setPaint(this.body_color);
        g2d.fill(this.body);
    }

    public void MoveRight() {
        this.move_right = true;
    }

    public void MoveLeft() {
        this.move_left = true;
    }

    public void StopMoveRight() {
        this.move_right = false;
    }

    public void StopMoveLeft() {
        this.move_left = false;
    }
}
