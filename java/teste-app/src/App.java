import javax.swing.*;
import java.awt.*;
import java.util.function.Function;

class App extends JFrame {

	Dimension screen_size = Toolkit.getDefaultToolkit().getScreenSize();
	int n = 0;
	int max_width = (int) screen_size.getWidth();
	int max_height = (int) screen_size.getHeight();
	int width = 500;
	int height = max_height;

	public void run(){
		JFrame frame = new JFrame("My App");
		frame.setBounds(max_width-width, 0, this.width, this.height);
		frame.setResizable(false);
		frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

		Body content = new Body(this.width, this.height*.85, new Color(255,0,0));
		content.createButton(0,0,"teste", "AddOne");
		content.createButton(0,0,"teste2", "AddTwo");
		Function<Void, Integer> fn = (Void)->{return 0;};
		content.addAction("AddOne", fn);

		Body footer = new Body(this.width, this.height*.15, new Color(50,50,50));

		frame.add(content);
		frame.add(footer);
		frame.setVisible(true);
	}
}
