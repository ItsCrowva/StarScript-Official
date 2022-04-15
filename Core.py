import json
import Main
import RunLine

# System Configuration
StarSettings = json.load(open("Core/settings.json", "r"))
# System Messages
Notice =  "\033[96m[ Notic ]\033[0m - " # Letting the user know stuff
Timing =  "\033[35m[ Timing ]\033[0m - " # Letting the user know stuff
Extra =  "\033[96m[ Extra ]\033[0m - " # Spammy Stuff
Debug =  "\033[35m[ Debug ]\033[0m - " # Assist with debugging
Comment = "\033[32m[Comment]\033[0m - "
Warning = "\033[93m[ Warni ]\033[0m - " # Warning the user of possible future code breaks
Alert =   "\033[91m[ Alert ]\033[0m - " # Something is probably gonna go wrong
Error =   "\033[91m\033[1m[ Error ]\033[0m - " # Somethig is really wrong
Success = "\033[92m[ Succe ]\033[0m - " # Very Spammy Success Message
Console = "\033[90m[Console]\033[0m - " # Console Stuff
Clear = "\033[0m"
AnnounceOutputs = ""
if StarSettings["alerts"]["AnnounceOutputs"] == True:
    AnnounceOutputs = "\033[95m[ Outpu ]\033[0m - "

ErrorReturn = f"{Alert} - We were unable to complete this request." # The string that the system feeds back

# Storage


GlobalClasses = {}
GlobalVariables = {
    "ExampleTextVariable": "I hold an example value :P",
    "ExampleNumberVariable": 1,
    "ExampleClassDefVariable": "string.value Input: DefVariable",
    "ExampleClassVariable": {
        "Type": "string",
        "Flags": {
            "Input": "Defined Class"
        }
    }
}

def openStrRaw(File):
    for x in File:
        # print(File, x)
        Line = x

        # Remove New Lines
        Line = Line.replace("\n", "")

        # Add Color
        if "--" in Line:
            Line = Line.split("--")

            Line[1] = f"\033[32m--{Line[1]}"

            Line = "".join(Line) + "\033[0m"
        
        if Line.startswith("+"):
            Line = Line.replace("+", f"\033[92m+")
        if Line.startswith("-"):
            Line = Line.replace("-", f"\033[91m-")
        if Line.startswith("*"):
            Line = Line.replace("*", f"\033[93m*")

        Line = Line + "\033[0m"
        print(Line)

# Better Print Bridge
def bprint(Type, String1="", String2="", String3="", String4="", String5="", String6="", String7="", String8="", String9="", String10=""):
    betterPrint(Type, String1, String2, String3, String4, String5, String6, String7, String8, String9, String10)

# Better Print
def betterPrint(Type, *args, Thread="Unset"):
    try:
        String = "".join(args)
    except:
        String = str(args)
    if StarSettings["alerts"]["Notice"] == True:
      if Type == "Notice":
        print(f"{Notice}{String}")
    if StarSettings["alerts"]["Extra"] == True:
      if Type == "Extra":
        print(f"{Extra}{String}")
    if StarSettings["alerts"]["Debug"] == True:
        if Type == "Debug":
            print(f"{Debug}{String}")
    if StarSettings["alerts"]["Comment"] == True:
        if Type == "Comment":
            print(f"{Comment}{String}")
    if StarSettings["alerts"]["Warning"] == True:
        if Type == "Warning":
            print(f"{Warning}{String}")
    if StarSettings["alerts"]["Alert"] == True:
        if Type == "Alert":
            print(f"{Alert}{String}")
    if StarSettings["alerts"]["Error"] == True:
        if Type == "Error":
            print(f"{Error}{String}")
    if StarSettings["alerts"]["Success"] == True:
        if Type == "Success":
            print(f"{Success}{String}")
    if StarSettings["alerts"]["Timing"] == True:
        if Type == "Timing":
            print(f"{Timing}{String}")
    if StarSettings["alerts"]["Console"] == True:
        if Type == "Console":
            print(f"{Console}{String}")
    # if StarSettings["alerts"]["AnnounceOutputs"] == True:
    if Type == "AnnounceOutputs":
            print(f"{AnnounceOutputs}{String}")

# Grab Values from a command
def grabValues(Input):
    tick = 0
    maxLength = len(Input)
    currentSetup = {
        "Rotary": "Only to be kept during testing."
    }
    currentTag = []
    currentValue = []
    scanningMode = "Input" # Input = Find Tag Name, Value = Add To Tag
    while tick < maxLength:
        # If SkipSpace- And Space- start value
        if scanningMode == "ToInput":
            scanningMode = "Input"
        if scanningMode == "ToValue,SkipSpace":
            scanningMode = "Value"
        # If Value )NotBracket( and we find a comma- paste the output into the (Inputs) value
        if scanningMode == "Value":
            if Input[tick] == "," or Input[tick] == ";":
                bprint("Notice", "Preparing to paste to variables")
                scanningMode = "ToInput"
                currentSetup[str("".join(currentTag)).strip()] = "".join(currentValue).strip()
                currentTag = []
                currentValue = []
        # If Colon on Input- Switch to Value
        if scanningMode == "Input":
            if Input[tick] == ":":
                bprint("Extra", "COLON DETECTED")
                # No Longer Needing to find the given flag
                scanningMode = "ToValue,SkipSpace"
                # Add to CurSet
                currentSetup.update({
                    str("".join(currentTag)).strip(): ""
                })
                # currentTag = []
        # Detect Flag Name
        if scanningMode == "Input":
            currentTag.append(Input[tick])
        # Add Value if Flag is Up
        if scanningMode == "Value":
            bprint("Extra", "Is Value")
            currentValue.append(Input[tick])
        # Debug Info
        bprint("Extra", "Input:", Input, "\n    CurrentTag:", currentTag, "\n    Scanning Mode:", scanningMode, "\n    CurrentValue", currentValue)
        # Next Letter
        tick += 1
    if StarSettings["alerts"]["Notice"] == True:
        print(f"{Notice}---done---", currentSetup)
    return currentSetup

# Incredibly Stupid Idea
Vreturn = ""
def setVreturn(Input):
    global Vreturn
    Vreturn = Input


def getBubble(bubble, attachedVariables):
    # Get Bubble
    # Check if Flag

    # @ = Flag
    # # = Input
    # & = Run As Command then Use Return Value
    # Blank = Raw
    bubble = bubble.split("-- ")[0].strip()
    if bubble.startswith("&"):
        bubble = bubble.replace("&", "", 1)
        # print("bubble:", bubble)
        # TemporaryObject = {
        #     "return": "none?"
        # }
        TemporaryObject = Main.runLine(bubble, {
            "SpecialFlag": "SentFromCore"
        }, attachedVariables)
        # print(Vreturn)
        # print(TemporaryObject)
        return Vreturn
    if bubble.startswith("@"):
        bubble = bubble.replace("@", "", 1)
        try:
            # print("AttachedVariables:", attachedVariables, "bubble", bubble)
            return attachedVariables[bubble]
        except:
            print(f"{Error}Flag Bubble: ({bubble}) not found!!")
            if StarSettings["alerts"]["Debug"] == True:
                print(f"{Debug}Do some digging. Does the variable exist? Was the variable removed from memory? Did you make a spelling mistake?")
            return ErrorReturn
    elif bubble.startswith("#"):
        bubble = bubble.replace("#", "", 1)
        return input(f"{Console}Send Input {bubble}: ")
    return bubble
