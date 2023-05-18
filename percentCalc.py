import PySimpleGUI as sg

# Define the layout of the GUI
layout = [[sg.Text('Old Value: '), sg.InputText(key='old_value')],
          [sg.Text('New Value: '), sg.InputText(key='new_value')],
          [sg.Button('Calculate'), sg.Button('Exit')],
          [sg.Text('Percent Change: '), sg.Text('', key='percent_change')]]

# Create the GUI window
window = sg.Window('Percent Change Calculator', layout)

# Define the main event loop
while True:
    event, values = window.read()

    # Exit the program if the user closes the window or clicks the Exit button
    if event == sg.WINDOW_CLOSED or event == 'Exit':
        break

    # Calculate the percent change if the user clicks the Calculate button
    if event == 'Calculate':
        old_value = float(values['old_value'])
        new_value = float(values['new_value'])
        difference = new_value - old_value
        percent_change = (difference / old_value) * 100

        # Update the GUI with the percent change
        window['percent_change'].update(f'{percent_change:.2f}%')

# Close the GUI window
window.close()