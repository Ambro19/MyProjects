"""This program check the language of string that contains, L(M)=.. """

import PySimpleGUI as sg

# Define the finite automaton M
Q = ['q0', 'q1', 'q2']
alphabet = ['0', '1']
delta = {
    ('q0', '0'): 'q1',
    ('q0', '1'): 'q0',
    ('q1', '0'): 'q2',
    ('q1', '1'): 'q1',
    ('q2', '0'): 'q1',
    ('q2', '1'): 'q2'
}
initial_state = 'q0'
accepting_states = {'q2'}

# Define the GUI layout
layout = [
    [sg.Text('Enter a binary string into Finite Automaton Machine:')],
    [sg.Input(key='input')],
    [sg.Button('Check'), sg.Button('Quit')],
    [sg.Text('', size=(35,2), key='output')]
]

# Create the window
window = sg.Window('Finite Automaton M', layout)

# Define the transition function
def transition(state, symbol):
    if (state, symbol) in delta:
        return delta[(state, symbol)]
    else:
        return None

# Define the main loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Quit':
        break
    elif event == 'Check':
        # Initialize the automaton
        state = initial_state
        # Iterate through the input string
        for symbol in values['input']:
            state = transition(state, symbol)
            if state is None:
                break
        # Check if the final state is accepting
        if state in accepting_states:
            window['output'].update('Accepted')
        else:
            window['output'].update('Rejected')

# Close the window
window.close()
