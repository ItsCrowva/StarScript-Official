from Core import *
from windowExtension import *

import random
import os
import json

GoTicker = 0
def runLine(lineScript, tempObject, attachedVariables):
    global GoTicker # Super Useless. Just- Variables before Variables are good
    global GlobalVariables
    global Modules
    # print(tempObject)
    # lineScript = Line to run
    # tempObject = FormerOtherdata
    try:
        tempObject["LinesRan"] += 1
    except:
        pass
    # Construct Variable
    if lineScript.startswith("import "):
        modeLine = lineScript.split(" ")
        # First try to import with the modules folder
        try:
            runScript(open(f"{StarSettings['Install']}\\Modules\\{modeLine[1]}.str", "r").read(), tempObject, attachedVariables)
        # Try to import from a file local to the python file
        except:
            runScript(open(f"{os.getcwd()}\\{modeLine[1]}.str", "r").read(), tempObject, attachedVariables)
    if lineScript.startswith("var "):
        # var TestVariable string Input: TestVariable1, Second: TestVariable2
        aboutToAdd = {
            f"Configuartion_{random.randint(100,999)}": f"{random.randint(1000,9999)} - This Makes Sure everything is Working"
        }
        lineWork = lineScript.split(" ", 3)
        GlobalVariables.update({
            f"{lineWork[1]}": {
                "Type": f"{lineWork[2]}",
                "Flags": {}
            }
        })
        GlobalVariables[f"{lineWork[1]}"]["Flags"].update(GlobalClasses[lineWork[2]]["TagsToFill"]) # Default
        ReturnV = grabValues(lineWork[3])
        GlobalVariables[f"{lineWork[1]}"]["Flags"].update(ReturnV) # Extras
        betterPrint("Notice","Current Variables Mode:", GlobalVariables)
        # Append Current Variable Directory
        attachedVariables.update(GlobalVariables)
        # Run Main Function
        betterPrint("Notice", "About to run the (Main) script of a class that has just been defined using var")
        print("ABOUT TO RUN:", GlobalClasses[lineWork[2]]["Main"])
        runScript(GlobalClasses[lineWork[2]]["Main"], tempObject, attachedVariables)
        betterPrint("Success", "Running the script should've been successful :)")
    # Returns
    if lineScript.startswith("return "):
      try:
        MotorTemp = tempObject
        # input(MotorTemp)
        # input("whhhh")
        # return TestVariable1, Second: TestVariable2
        # ReturnV = grabValues(lineScript.split(" ", 1)[1])
        # print(ReturnV)
        ReturnV = getBubble(lineScript.split(" ", 1)[1], attachedVariables)
        # input(f"wait for it: {ReturnV}")
        betterPrint("Notice", "Returning:", ReturnV)
        tempObject.update({"return": ReturnV})
        # tempObject = {"return": "blank"}
        # input(tempObject)
        # input(tempObject)
        try:
            if tempObject["SpecialFlag"] == "SentFromCore":
                # input("-----")
                return tempObject["return"]
        except:
            return tempObject, attachedVariables
      except:
          input("Error: Fatal error with the return statement")
    # Direct System Calls
    if lineScript.startswith("say "):
        SplitDrive = lineScript.split(" ", 1)[1]

        Response = getBubble(SplitDrive, attachedVariables)
        print(f"{AnnounceOutputs}{Response}")
        # # print(f"{AnnounceOutputs}Direct Paste of Variable:{attachedVariables[SplitDrive]}")
        # if lineScript.split(" ", 1)[1].startswith("@"):
        #     SplitDrive = SplitDrive.replace("@", "", 1)
        #     print(f"{AnnounceOutputs}say (Variable):{attachedVariables[SplitDrive]}")
        # else:
        #     print(f"{AnnounceOutputs}say      (Raw): {SplitDrive}")
    # Running Programs
    if lineScript.startswith("run"):
        # run C:\Users\Andi\Documents\desktop\starScript-0.2.3\Scripts\FeatureTest
        # run Scripts/PerformanceTest
        runScript(open(f"{lineScript.split(' ')[1]}.str", "r").readlines(), tempObject, GlobalVariables)
    # Raising Issues
    if lineScript.startswith("raise"):
        if lineScript == "raise classes":
            print("honestly this being a command is a sign of a stupid coding language")
            print("but whatever- our developer is an idiot. \nClasses:")
            print(json.dumps(GlobalClasses, indent=4))
        if lineScript.startswith("raise error"):
            if lineScript == "raise error":
                # No reason given
                bprint("Error", f"There has been an unspecified error!")
            else:
                raiseTemp = lineScript.split(": ", 1)[1]
                bprint("Error", f"{raiseTemp}")
        if lineScript.startswith("raise warning"):
            if lineScript == "raise warning":
                # No reason given
                print(f"{Warning}There has been an unspecified warning!")
            else:
                raiseTemp = lineScript.split(": ", 1)[1]
                print(f"{Warning}{raiseTemp}")
        if lineScript.startswith("raise notice"):
            if lineScript == "raise notice":
                # No reason given
                print(f"{Notice}There has been an unspecified notice!")
            else:
                raiseTemp = lineScript.split(": ", 1)[1]
                print(f"{Notice}{raiseTemp}")
        if lineScript.startswith("raise success"):
            if lineScript == "raise success":
                # No reason given
                print(f"{Success}There has been an unspecified success!")
            else:
                raiseTemp = lineScript.split(": ", 1)[1]
                print(f"{Success}{raiseTemp}")
        if lineScript.startswith("raise comment"):
            if lineScript == "raise comment":
                # No reason given
                print(f"{Comment}There has been an undefined comment!")
            else:
                raiseTemp = lineScript.split(": ", 1)[1]
                print(f"{Comment}{raiseTemp}")
        if lineScript.startswith("raise debug"):
            if lineScript == "raise debug":
                # No reason given
                print(f"{Debug}There has been an unspecified debug!")
            else:
                raiseTemp = lineScript.split(": ", 1)[1]
                print(f"{Debug}{raiseTemp}")
    if lineScript.startswith("print "):
        # Print requires 2 flags
        # 'value' & 'repeat'
        # if StarSettings["alerts"]["Error"] == True:
        bprint("Error", "The print function failed to execute~")
        bprint("Debug", f"Heya! strlng5(2ndEdition) no longer uses the print function. print <Variable Mention>/<Bubble> is a very old command and doesn't work especially since bubbles aren't a thing in this language anymore. Please use `say`. To print raw text: say <Text>. To print a flag/DirectFlagVariable: say @<Variable>")

    # Try Running Line from another File
    if Modules["WindowExtension"]["Enabled"] == True: windowExtensionRunLine(lineScript, tempObject, attachedVariables)

    return tempObject, attachedVariables


def runScript(script, tempObject, attachedVariables):
    global GlobalClasses
    # script = script.replace("^*^", "\n")
    tempPointer = 0
    # print(script)
    scriptLength = len(script)

    # Comment Stuff
    previousMode = ""
    # Class Stuff
    holdingCell = []
    lineMode = "Execute"
    otherMode = "None"
    nameMode = "??"
    className = "What"
    classTicker = 0
    holdingClass = {}

    # RUN
    while tempPointer < scriptLength:
        aboutToRun = script[tempPointer].split("^*^")
        tick = 0
        while tick < len(aboutToRun):
            aboutToRun[tick] = aboutToRun[tick].strip()
            if lineMode == "Comment":
                if StarSettings["alerts"]["Comment"] == True:
                    print(f"{Comment}{aboutToRun[tick]}")
                if "-/" in aboutToRun[tick]:
                    line = aboutToRun[tick].split("-/")[1]
                    aboutToRun[tick] = line
                    lineMode = previousMode
            if lineMode == "Execute":
                if aboutToRun[tick].startswith("--"):
                    if StarSettings["alerts"]["Comment"] == True:
                        print(f"{Comment}{aboutToRun[tick]}")
                elif aboutToRun[tick].startswith("/-"):
                    previousMode = str(lineMode)
                    lineMode = "Comment"
                elif aboutToRun[tick].startswith("class"):
                    holdingCell = []
                    otherMode = "None" # Current Class-Working Mode
                    className = aboutToRun[tick].split(" ")[1]
                    holdingClass = {
                        "TagsToFill": {
                            "ExampleVariablePleaseNeverFillMe": "None"
                        },
                        "Main": [
                            "// Main Class",
                            "raise notice: This Class has been Initialised Correctly!"
                        ]
                    }
                    lineMode = "Class"
                    classTicker = 0 # Should be a value of 1 however it gets set to one in the linemode = class
                else:
                    # See if line is a variable {Class}?
                    if aboutToRun[tick].split(".")[0] in attachedVariables:
                        TempLine = aboutToRun[tick].split(".")
                        TempLine[1] = TempLine[1].split(" ", 1)
                        # Get Class Type
                        ClassType = attachedVariables[TempLine[0]]["Type"]
                        # Run Script
                        attachment = attachedVariables[TempLine[0]]["Flags"]
                        runScript(GlobalClasses[ClassType][TempLine[1][0]], tempObject, attachment)
                    # See if the line is a class (Undefined Class)
                    if aboutToRun[tick].split(".")[0] in GlobalClasses:
                        # This means it's possible to run as a class!
                        TempLine = aboutToRun[tick].split(".")
                        TempLine[1] = TempLine[1].split(" ", 1)
                        print(TempLine[0], TempLine[1][0])
                        # Set up all the variables:
                        addedVariables = grabValues(TempLine[1][1])
                        # Run it as a script
                        handOffVariable = attachedVariables
                        handOffVariable.update(addedVariables)
                        print(handOffVariable)
                        runScript(GlobalClasses[TempLine[0]][TempLine[1][0]], tempObject, handOffVariable)
                    # run the line as a standard line
                    tempObject, attachedVariables = runLine((aboutToRun[tick].replace("\n", "")).replace("\\n", "\n"), tempObject, attachedVariables)
            if lineMode == "Class":
                # Construct a class object to send directly to the makeClass function
                if "{" in aboutToRun[tick]:
                    classTicker += 1
                if "}" in aboutToRun[tick]:
                    classTicker -= 1
                if classTicker == 1:
                    otherMode = "*AboutToGoNone*"
                
                # Function Initialisation
                if aboutToRun[tick].startswith("func"):
                    nameMode = aboutToRun[tick].split(" ")[1]
                    otherMode = "AboutToFunction"
                    holdingClass.update({str(nameMode): [
                        f"// {nameMode} function."
                    ]})
                if otherMode == "None":
                    holdingClass["Main"].append(aboutToRun[tick])
                    betterPrint("Notice", "Current Holding Class", holdingClass)
                if otherMode == "Function":
                    holdingClass[nameMode].append(aboutToRun[tick])
                
                if aboutToRun[tick].startswith("@flag "):
                    temp = aboutToRun[tick].split(" ")[1].replace(":", "")
                    Ven = "None" # Default Value
                    if "=" in temp:
                        # A default value has been detected;
                        Ven = temp.split(" = ", 1)[1] # The Default Value

                    holdingClass["TagsToFill"].update({
                        str(temp): Ven
                    })
                

                # This Means the Class has been closed.
                if classTicker == 0:
                    lineMode = "Execute"
                    betterPrint("Warning", "Final Holding Class", holdingClass)
                    GlobalClasses.update({str(className): holdingClass})
                    betterPrint("Warning", "Current Global Class", GlobalClasses)
                    # print(str(json.loads(GlobalClasses)))
                    print(GlobalClasses)
                
                # This is so "}" isn't put anywhere
                if otherMode == "AboutToFunction":
                    otherMode = "Function"
                if otherMode == "*AboutToGoNone*":
                    otherMode = "None"
                # holdingClass.append(aboutToRun[tick]) # formerly holding cell
            tick += 1
        tempPointer += 1
    return tempObject