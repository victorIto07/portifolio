import javax.swing.*;
import java.awt.*;
import java.awt.event.*;
import java.util.ArrayList;
import java.util.function.Function;

class Body extends JPanel implements ActionListener{
	double width;
	double height;
	Color background_color;

	ArrayList<MyAction> actions = new ArrayList<>();

	int n = 0;

	Body(double width, double height, Color color){
		this.width = width;
		this.height = height;
		this.background_color = color;
		this.setPreferredSize(new Dimension((int) this.width, (int) this.height));
		this.setSize(new Dimension((int) this.width,(int) this.height));
		this.setBackground(this.background_color);
		this.setLayout(new BoxLayout(this, BoxLayout.PAGE_AXIS));
	}

	public JButton createButton(double x, double y, String text, String action){
		JButton b = new JButton(text);
		b.addActionListener(this);
		b.setActionCommand(action);
		this.add(b);
		return b;
	}

	public void addAction(String name, Function<Void,Integer> action){
		this.actions.add(new MyAction(name,action));
	}

	@Override
	public void actionPerformed(ActionEvent e) {
		try {
			String name = e.getActionCommand();
			System.out.println(name);
			this.actions.forEach(action->{
				if(action.name==name){
				}
			});
		} catch (Exception exception) {
			System.out.println(exception.toString());
		}
	}

}
