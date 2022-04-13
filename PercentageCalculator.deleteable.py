# Funny Little Percentage Calculator
from datetime import *
StartDate = datetime(2022, 4, 19, 7, 30, 0)
EndDate = datetime(2022, 4, 8, 12, 55, 0)
CurrentDate = datetime.now()

Percentage = 0

def CalculatePercentage():
    global Percentage
    Percentage = (CurrentDate - StartDate).total_seconds() / (EndDate - StartDate).total_seconds() * 100
    Percentage = round(Percentage, 2)
    return Percentage

print(CalculatePercentage())