import random  #Importing the random module
import os      #Importing the os module
import sys     #Importing the os module
import multiprocessing
import PySimpleGUI as sg

'''
num = multiprocessing.cpu_count()
print("Number of cpu: ", num)


file_path = random.__file__

dir = os.path.dirname(file_path)
#Printing the dierectories
print("Directories:\n" + dir)
print(help(os))
'''


#To run the list of all directories which will be serched fir the odeulw at runtime
#sys_path = sys.path
#print("System Path:\n" + sys_path)

'''To add a method that uses a PySimpleGUI button to download the link of the literal 
variable entered by the user, you can modify the existing code by adding a function called 
download_link that retrieves the entered link using the PySimpleGUI values dictionary and 
then downloads the link using the requests library. Here's an example implementation:
'''

import requests
entry = [[sg.Button("Download", key="DOWNLOAD"),]]

layout = [entry]
window = sg.Window(title="Wikipedia Download",layout=layout, element_justification="c", resizable = True, font=("Arial", 18)).Finalize()

# Function to download the link entered by the user
def download_link():
    # Retrieve the link entered by the user
    link = values['-LINK ENTERED-']
    # Download the link
    response = requests.get(link)
    # Save the downloaded file to disk
    with open('downloaded_file.html', 'wb') as f:
        f.write(response.content)

# Main event loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    elif event == 'Download':
        download_link()

'''
In this example, the download_link function retrieves the link 
entered by the user using the values dictionary and then uses the 
requests library to download the link. The downloaded file is saved to 
disk using the open function in binary mode ('wb'). The main event loop 
checks for the 'Download' button press event and calls the download_link 
function when the button is pressed.
'''