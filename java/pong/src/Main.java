
/*
 * ----------------------------|
 *                             |
 *   TWO PLAYER PONG GAME      |
 *                             |
 * ----------------------------|
 */

class Main {
    public static void main(String[] args) {
        int width = 800;
        int height = 800;
        Pong game = new Pong(width, height);
        game.run();
    }
}
