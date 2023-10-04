import java.awt.geom.*;
import java.awt.*;

public class Player {

    int max_width;
    int max_height;

    Rectangle2D.Double body;

    public double body_width = 20;
    public double body_height = 100;

    double speed;

    int points = 0;

    Player(boolean right, int w, int h) {
        this.max_width = w;
        this.max_height = h;
        this.body = new Rectangle2D.Double((right ? w - body_width : 0), this.max_height / 2 - body_height / 2,
                body_width, body_height);
    }

    boolean canMove() {
        if (this.body.y + this.body_height >= this.max_height && this.speed == 1)
            return false;
        if (this.body.y < 1 && this.speed == -1)
            return false;
        return true;
    }

    void update() {
        this.body.y += this.canMove() ? this.speed : 0;
    }

    public void draw(Graphics2D g2d) {
        this.update();
        g2d.setPaint(new Color(255, 255, 255));
        g2d.fill(this.body);
    }

    public void moveUp() {
        this.speed = -1;
    }

    public void moveDown() {
        this.speed = 1;
    }
    
    public void stopMoveUp() {
        this.speed = 0;
    }
    
    public void stopMoveDown() {
        this.speed = 0;
    }

    public void getPoints(){
        this.points++;
    }
}