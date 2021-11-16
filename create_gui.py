import PySimpleGUI as sg
import createoption


def create(public_key, private_key):
    layout = [
        [sg.Text("LEVERAGE")],
        [sg.Input(key="leverage")],
        [sg.Text("CAP")],
        [sg.Input(key="cap")],
        [sg.Text("STRIKE")],
        [sg.Input(key="strike")],
        [sg.Text("PRICE")],
        [sg.Input(key="price")],
        [sg.Button("CREATE", bind_return_key=True), sg.Button("CANCEL")],
    ]

    window = sg.Window("Create Options", layout)

    while True:
        event, values = window.read()
        print(event, values)
        if event == "CREATE":
            createoption.create(
                int(values["leverage"]),
                int(values["cap"]),
                int(values["strike"]),
                int(values["price"]),
                public_key,
                private_key,
            )
        else:
            break

    window.close()
