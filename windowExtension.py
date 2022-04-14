from tkinter import *
from turtle import title
from Core import *
# import graphics

# from arcade import Window

FlagsName = "Flags"
ActiveWindows = {
    "$Default": {
        "Value": "Not an actual window"
    }
}

class scriptWindow(list):
    def __init__(self, classObject=None):
        self.append(classObject)
        root = Tk()
        root.title(classObject[FlagsName]["Title"])
        root.geometry(classObject[FlagsName]["Size"])
        root.resizable(width=False, height=False)
        root.configure(background=classObject[FlagsName]["Background"])
        # root.protocol("WM_DELETE_WINDOW", self.on_closing) # For Onclose
        self.append(root)
        self.refresh()
    def refresh(self):
        # Window.title(classObject[FlagsName]["Title"])
        self[1].title(self[0][FlagsName]["Title"])
        pass

def windowExtensionRunLine(line, tempObject, attachedVariables):
    # Run Line As Window Extension


    # Initialise a new Window
    if line.startswith("makeWindow "):
        # input("c")
        # makeWindow Name: <WindowName.raw>, Title: <WindowName.raw>, Size: <Size.raw>;
        WindowVariables = grabValues(line)
        # input("b")
        print("[$Console$]-WindowVariables:", WindowVariables)
        # input("a")
        pass


    pass

# test = scriptWindow(
#     {
#         "Type": "Window",
#         "Flags": {
#             "Title": "Example Window",
#             "Size": "600x400",
#             "Background": "black"
#         }
#     }
# )
# *Hypothetically* Started From:
#var AppWindow window Size: 600x400, Title: Example Window;
#AppWindow.setBackground Background: black;


# test.refresh()

# # root.mainloop()
# mainloop()