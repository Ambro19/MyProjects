import PySimpleGUI as sg
from googletrans import LANGUAGES, Translator

# Define available language options
languages = [LANGUAGES[key] for key in LANGUAGES.keys()]

# Define GUI layout
layout = [
    [sg.Text("Select language:"), sg.Combo(languages, default_value="English", key="language")],
    [sg.Text("Select comparison tool:"), sg.Radio("Diff", "RADIO1", default=True, key="diff"), sg.Radio("Match", "RADIO1", key="match")],
    [sg.Text("Source article:"), sg.Multiline(key="source", size=(60, 10))],
    [sg.Text("Target article:"), sg.Multiline(key="target", size=(60, 10))],
    [sg.Button("Clear"), sg.Button("Compare"), sg.Button("Translate")],
    [sg.Text("Comparison result:"), sg.Multiline(key="result", size=(60, 10), disabled=True)]
]

# Create the GUI window
window = sg.Window("Article Comparison Tool", layout)

# Create a translator object for later use
translator = Translator()

# Define comparison function
def compare(source_text, target_text, tool):
    if tool == "Diff":
        # Perform comparison using difflib library
        import difflib
        result = difflib.ndiff(source_text.splitlines(), target_text.splitlines())
        result = "\n".join(list(result))
    elif tool == "Match":
        # Perform comparison using string matching
        result = ""
        for sentence in source_text.split("."):
            if sentence in target_text:
                result += sentence + ".\n"
    return result

# Event loop to process GUI events
while True:
    event, values = window.read()

    # Handle window closed event
    if event == sg.WINDOW_CLOSED:
        break

    # Handle clear button event
    elif event == "Clear":
        window["source"].update("")
        window["target"].update("")
        window["result"].update("")

    # Handle compare button event
    elif event == "Compare":
        source_text = values["source"]
        target_text = values["target"]
        tool = "Diff" if values["diff"] else "Match"
        result = compare(source_text, target_text, tool)
        window["result"].update(result)

    # Handle translate button event
    elif event == "Translate":
        source_text = values["source"]
        target_text = values["target"]
        source_lang = translator.detect(source_text).lang
        target_lang = values["language"]
        if source_lang != target_lang:
            # Translate target text to match source language
            translation = translator.translate(target_text, src=target_lang, dest=source_lang)
            window["target"].update(translation.text)
            window["result"].update("")

# Close the window when the event loop is exited
window.close()
