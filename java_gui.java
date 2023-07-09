import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class ApplicationLogin {

    public static void main(String[] args) {
        SwingUtilities.invokeLater(() -> {
            createAndShowGUI();
        });
    }

    private static void createAndShowGUI() {
        // Create the main frame
        JFrame frame = new JFrame("Application Login");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(300, 200);

        // Create the panel for username and password
        JPanel panel = new JPanel(new GridLayout(3, 2));

        JLabel usernameLabel = new JLabel("Username:");
        JTextField usernameField = new JTextField();

        JLabel passwordLabel = new JLabel("Password:");
        JPasswordField passwordField = new JPasswordField();

        panel.add(usernameLabel);
        panel.add(usernameField);
        panel.add(passwordLabel);
        panel.add(passwordField);

        // Create the buttons for account creation and sign-in
        JButton createButton = new JButton("Create Account");
        JButton signInButton = new JButton("Sign In");

        createButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Handle create account button click
                // Add your logic here
                System.out.println("Creating a new account");
            }
        });

        signInButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                // Handle sign in button click
                // Add your logic here
                System.out.println("Signing in");
            }
        });

        // Create the main panel and add components
        JPanel mainPanel = new JPanel();
        mainPanel.setLayout(new BorderLayout());
        mainPanel.add(panel, BorderLayout.CENTER);
        mainPanel.add(createButton, BorderLayout.WEST);
        mainPanel.add(signInButton, BorderLayout.EAST);

        // Set the main panel as the content of the frame
        frame.getContentPane().add(mainPanel);

        // Show the GUI
        frame.setVisible(true);
    
    }//End createAndShowGUI function
    
}//End ApplicationLogin Class