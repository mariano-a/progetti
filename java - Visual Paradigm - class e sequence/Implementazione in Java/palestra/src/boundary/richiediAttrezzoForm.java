package boundary;

import java.awt.BorderLayout;
import java.awt.EventQueue;

import javax.swing.JFrame;
import javax.swing.JPanel;
import javax.swing.border.EmptyBorder;

import controller.Controller;

import javax.swing.JTextField;
import javax.swing.JLabel;
import javax.swing.JButton;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import javax.swing.SwingConstants;

public class richiediAttrezzoForm extends JFrame {

	private JPanel contentPane;
	private JTextField textField;
	private JTextField textField_1;

	/**
	 * Launch the application.
	 */
	public static void main(String[] args) {
		EventQueue.invokeLater(new Runnable() {
			public void run() {
				try {
					richiediAttrezzoForm frame = new richiediAttrezzoForm();
					frame.setVisible(true);
				} catch (Exception e) {
					e.printStackTrace();
				}
			}
		});
	}

	/**
	 * Create the frame.
	 */
	public richiediAttrezzoForm() {
		setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
		setBounds(100, 100, 450, 300);
		contentPane = new JPanel();
		contentPane.setBorder(new EmptyBorder(5, 5, 5, 5));
		setContentPane(contentPane);
		contentPane.setLayout(null);
		
		textField = new JTextField();
		textField.setHorizontalAlignment(SwingConstants.CENTER);
		textField.setBounds(155, 70, 217, 20);
		contentPane.add(textField);
		textField.setColumns(10);
		
		textField_1 = new JTextField();
		textField_1.setBounds(155, 116, 217, 20);
		contentPane.add(textField_1);
		textField_1.setColumns(10);
		
		
		JLabel lblIdBadge = new JLabel("ID badge");
		lblIdBadge.setBounds(56, 72, 67, 17);
		contentPane.add(lblIdBadge);
		
		JLabel lblTipoAttrezzo = new JLabel("Tipo attrezzo");
		lblTipoAttrezzo.setBounds(55, 119, 103, 14);
		contentPane.add(lblTipoAttrezzo);
		
		JButton btnConferma = new JButton("Conferma");
		btnConferma.addMouseListener(new MouseAdapter() {
			@Override
			public void mouseClicked(MouseEvent e) {
				System.out.println("Controller");
				Controller controller = new Controller();
				
				controller.RichiestaAttrezzatura(Integer.parseInt(textField.getText()), textField_1.getText());
			}
		});
		btnConferma.setBounds(283, 197, 89, 23);
		contentPane.add(btnConferma);
	}
}
