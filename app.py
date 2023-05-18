import PySimpleGUI as sg
import sqlite3

# Function to execute SQL queries
def execute_query(query):
    conn = sqlite3.connect("sample.db")  # Replace "sample.db" with your own database file
    cursor = conn.cursor()
    cursor.execute(query)
    results = cursor.fetchall()
    conn.close()
    return results

# GUI layout
layout = [
    [sg.Text("Enter SQL query:"), sg.InputText(key="-QUERY-")],
    [sg.Button("Execute"), sg.Button("Exit")],
    [sg.Text("Query Results:")],
    [sg.Output(size=(80, 20), key="-OUTPUT-")]
]

# Create the window
window = sg.Window("SQL Query Tool", layout)

# Event loop
while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED or event == "Exit":
        break
    elif event == "Execute":
        query = values["-QUERY-"]
        results = execute_query(query)
        for row in results:
            print(row)

window.close()
