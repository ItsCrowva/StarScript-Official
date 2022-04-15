# from logging import root
from concurrent.futures.process import _RemoteTraceback
from tkinter import *
import tkinter

from arcade import RGB
# from turtle import title
import Core
# import graphics

# from arcade import Window

FlagsName = "Flags"
ActiveWindows = {
    "$Default": {
        "Value": "Not an actual window"
    }
}
Item = []

def addUIObject(Root, Object):
    global Item
    Object = Object.strip()
    #Examples:
    #   Text :: ExampleText, 12, Black, Arial
    #   Button :: ClickMe, 12, Black, Arial, FunctionToRun
    #   VList :: \[
    #    Text :: ExampleText, 12, Black, Arial
    #    Button :: ClickMe, 12, Black, Arial, FunctionToRun
    #   \]
    #   HList :: \[
    #    Text :: ExampleText, 12, Black, Arial
    #    Button :: ClickMe, 12, Black, Arial, FunctionToRun
    #   \]
    print("addUIObject:", Object)
    if Object.startswith("Background"):
        Child = Object.split(" :: ")
        Root.configure(bg=Child[1])
    if Object.startswith("hiii"):
        # input("-Pause-")
        Item.append(Label(Root, text=Object))
        Item[-1].pack()
    if Object.startswith("Text"):
        Child = Object.split(" :: ")[1]

        Child = Child.split(", ")
        Character = Label(Root, text=Child[0], font=Child[3], fg=Child[2])
        # Character = Label(Root, text=Child[0],font=Child[3], fg=Child[2])
        Item.append(Character)
        # Character = Label(Root, text="h")
        Item[-1].pack()
    if Object.startswith("VList"):
        # Tricky af---
        Child = Object.split("[", 1)[1]
        Script = Child.split("\n")
        Brackets = 1 # Starts at one as the above function, covered it
        tick = 1 # To start at the second line
        while Brackets > 0:
            # print(Brackets)
            if "[" in Script[tick]:
                Brackets += 1
            if "]" in Script[tick]:
                Brackets -= 1
            if not Brackets == 0:
                addUIObject(Root, Script[tick].strip())
            tick += 1
    # return Root




def RemoveLastUIItem():
    global Item
    Item[-1].destroy()



def WErunLine(lineScript, tempObject, attachedVariables):
    if lineScript.startswith("MakeWindow "):
        # MakeWindow @WindowName, @Window
        Child = lineScript.split(" ", 1)[1]
        Child = Child.split(",")
        window = Tk()
        window.title(Core.getBubble(Child[0], attachedVariables))
        addUIObject(window, Core.getBubble(Child[1], attachedVariables))
    if lineScript.startswith("ConstructWebsite "):
        # ConstructWebsite @Window
        Child = lineScript.split(" ", 1)[1]
        Child = Child.split(",")
        Operation = Core.getBubble(Child[0], attachedVariables)

        print("will do this later. smh.")
    if lineScript.startswith("ConstructWindow "):
        # ConstructWindow @Window
        Child = lineScript.split(" ", 1)[1]

        Child = Core.getBubble(Child, attachedVariables)
        # print(Child)

        ReturnV = []

        tick = 0
        while tick < len(Child):
            # If VList
            if Child[tick].startswith("VLStart"):
                ReturnV.append("VList :: [\n")
            if Child[tick].startswith("VLEnd"):
                ReturnV.append("]\n")
            # If Text:
            if Child[tick].startswith("Text:"):
                Operation = Child[tick].replace("Text:", "", 1)
                # input(Operation)
                ReturnV.append(f"Text :: {Operation}, 12, Black, Arial\n")
            tick += 1
        ReturnV = "".join(ReturnV)
        # Return
        # print(ReturnV)
        Core.setVreturn(ReturnV)
        tempObject.update({"return": ReturnV})
    return tempObject

if __name__ == "__main__": 
    root = Tk()
    root.title("StarScript")
    root.configure(bg="black")
    root.geometry("500x500")

    GUICode = """
VList :: [
    Background :: blue4
Text :: Welcome to the EPIC Star Script Example Program!, 12, cyan2, arial
Text :: ExampleText, 12, cyan2, arial
Text :: ExampleText, 12, cyan2, arial
Text :: ExampleText, 12, cyan2, arial
]
"""

    print("-", GUICode, "-")
    # Root = 
    addUIObject(root, GUICode.strip())
    tkinter.Label(root, text="Hello, world!").pack()
    Button(root, text="Quit", command=RemoveLastUIItem).pack()
    root.mainloop()