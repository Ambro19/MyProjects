import PySimpleGUI as sg

# Define the layout for the PySimpleGUI interface
layout = [
    [sg.Text("Product Name:"), sg.InputText(key="product_name")],
    [sg.Text("Manufacturer:"), sg.InputText(key="manufacturer")],
    [sg.Text("User Ratings:"), sg.InputText(key="user_ratings")],
    [sg.Button("Analyze")]
]

# Create the PySimpleGUI window
window = sg.Window("Product Quality Analyzer", layout)

# Run the PySimpleGUI event loop
while True:
    event, values = window.read()

    # If the "Analyze" button is clicked, perform the quality analysis
    if event == "Analyze":
        product_name = values["product_name"]
        manufacturer = values["manufacturer"]
        user_ratings = values["user_ratings"]

        # TODO: Perform quality analysis on the input data
        old_value = float(values['old_value'])
        new_value = float(values['new_value'])
        difference = new_value - old_value
        percent_change = (difference / old_value) * 100

        # Update the GUI with the percent change
        window['percent_change'].update(f'{percent_change:.2f}%')


        # TODO: Display the results of the analysis back to the user

    # If the user closes the window, exit the event loop
    if event == sg.WIN_CLOSED:
        break

# Close the PySimpleGUI window
window.close()