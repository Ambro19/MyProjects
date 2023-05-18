''''
To install Pyperclip module on Windows use: python3 -m pip install pyperclip. Do not use: pip install pyperclip
Using the pyperclip library to read and write to the clipboard.
'''

import webbrowser # Module to allow displaying web-based documents to user
import PySimpleGUI as psg
import pyperclip # Module to copy and paste to clipboard function

'''
# Open the VisualEditor page in Wikipedia
def open_visual_editor():
    url = 'https://en.wikipedia.org/wiki/Main_Page'

    #url = 'https://en.wikipedia.org/wiki/Special:VisualEditor'
    webbrowser.open_new_tab(url)
    #webbrowser.open_new(url)
'''

# Handle the Download button press event:
def download_text():
    editing_content = pyperclip.paste() # May replace this with the wikipedia link
    with open('user_article.txt', 'w') as file:
        file.write(editing_content)
        
# The PySimpleGUI layout with the Download button
layout = [[psg.Button('Download')]]  

#Create the PySimpleGUI window and add the layout to it
window = psg.Window('User Wikipedia Article', layout)

# The PySimpleGUI event loop to handle inputs from the user
while True:
    event, values = window.read()
    if event == psg.WIN_CLOSED:
        break
    elif event == 'Download':
        download_text()
    ''''  
    elif event == 'Upload':
        filepath = psg.popup_get_file('Select a file to upload')#Allow user to select a file to upload
        if filepath:
          upload_text(filepath)
    '''      

window.close() 
