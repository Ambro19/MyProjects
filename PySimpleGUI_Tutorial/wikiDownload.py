import PySimpleGUI as sg
import requests

def download_wiki():
    url = 'https://en.wikipedia.org/wiki/Python_(programming_language)'
    #url = 'https://en.wikipedia.org/wiki/Johnny_Depp'
    response = requests.get(url)
    with open('python_wiki.html', 'wb') as f:    #'python_wiki.html', 'wb'                
        f.write(response.content)
    sg.popup('Download complete!')

layout = [[sg.Button('Download Wikipedia Page')]]

window = sg.Window('Wikipedia Downloader', layout)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Download Wikipedia Page':
        download_wiki()

window.close()
