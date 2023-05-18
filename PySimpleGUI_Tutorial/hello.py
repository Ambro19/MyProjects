import PySimpleGUI as psg

layout = [[psg.Text(text='Hello World',font=('Arial Bold', 20),size=20, expand_x=True, justification='center')],
]

window = psg.Window('HelloWorld', layout, size=(715,250))

while True:
 event, values = window.read()
 print(event, values)
 if event in (None, 'Exit'):
    break
window.close()
