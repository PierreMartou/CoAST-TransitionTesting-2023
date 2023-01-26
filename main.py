from features import *
from RIS import RIS
from time import sleep

def runTable1():
    RISsystem = RIS()
    testSuite = ["+Widget, +Instructions, +InstrColdweather,  +EmergencyLevel, +Low",
                 "-InstructionsColdweather, -Low, +InstructionsFlood, +High",
                 "-Instructions, -InstructionsFlood, +Map",
                 "+Instructions, +InstructionsFlood, +InstructionsColdweather, +Low",
                 "-InstructionsFlood, -High",
                 "-Instructions, -InstructionsColdweather, -Low",
                 "+Low",
                 "+High"]
    iter = 1
    for transitions in testSuite:
        print("================= Test number " + str(iter) + "================================")
        RISsystem.transition(transitions)
        print("Current emergency level : " + str(RISsystem.emergencyLevel))
        sleep(0.05)
        answer = input("Please enter anything to transition to the next test configuration, or \"exit\" to stop the simulation.")
        if answer.lower() == "exit":
            break
        iter += 1


def runTransitionError():
    pass


def runFreeMode():
    print("Entered free mode. Please type \"exit\" to stop the program.")
    print("The expected transitions between configurations is a list of features that are activated ('+') or deactivated ('-'), ")
    print("separated by commas. Example : \"-Low, +High, -InstructionsFloods, +InstructionsColdWeather\"")
    print("Note that the transition is automatically ordered. However, this prototype does not check whether your transition leads to a valid system state.")
    RISsystem = RIS()
    iter = 1
    answer = input("Please enter the first transition : ")
    while answer.lower() != "exit":
        RISsystem.transition(answer)
        print("Currently in test number " + str(iter) + ". Current emergency level : " + str(RISsystem.emergencyLevel))
        iter += 1
        answer = input("Please enter the next transition : ")

print("Welcome to this little demonstration on transition behavioural errors.")
print("Please read the README to understand the three modes proposed, then type the mode you wish to run between \"CIT\", \"transition\" and \"free\".")
choice = input()
while choice not in ["CIT", "transition", "free"]:
    print("The mode was not recognized. Please choose among \"CIT\", \"transition\" and \"free\".")
    choice = input()
if "CIT" in choice:
    runTable1()
elif "transition" in choice:
    runTransitionError()
elif "free" in choice:
    runFreeMode()
