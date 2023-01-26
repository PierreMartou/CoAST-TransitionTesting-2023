from features import *
from RIS import RIS

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
        answer = input("Please enter anything to transition to the next test configuration, or \"exit\" to stop the simulation.")
        if answer.lower() == "exit":
            break
        iter += 1


def runTransitionError():
    print("In this mode, we perform the two transitions associated to transition behavioural errors in Section 2.")
    print("We first perform a transition that deactivates High and activates Low, which should trigger an error.")
    RISsystem = RIS()
    iter = 1
    print("================= Test number " + str(iter) + "================================")
    RISsystem.transition("+Widget, +emergencylevel, +high, +map")
    print("Current emergency level : " + str(RISsystem.emergencyLevel))
    answer = input("Please enter anything to perform the transition \"-high, +low\", or \"exit\" to stop the simulation.")
    if answer.lower() == "exit":
        return
    iter += 1
    print("================= Test number " + str(iter) + "================================")
    RISsystem.transition("-high, +low")
    print("Current emergency level : " + str(RISsystem.emergencyLevel))
    print("---------")
    print("We now demonstrate the other problematic transition : \"-Map, +Instructions\".")
    answer = input("Please enter anything to perform the transition \"-Map, +Instructions\", or \"exit\" to stop the simulation.")
    if answer.lower() == "exit":
        return
    iter += 1
    print("================= Test number " + str(iter) + "================================")
    RISsystem.transition("-Map, +Instructions")
    print("Current emergency level : " + str(RISsystem.emergencyLevel))

    print("This ends this short demonstration. Feel free to explore the possible configurations with the free mode.")
    input("Enter anything to terminate execution.")

def runFreeMode():
    print("Entered free mode. Please type \"exit\" to stop the program.")
    print("The expected transitions between configurations is a list of features that are activated ('+') or deactivated ('-'), separated by commas.")
    print("Example : \"-Low, +High, -InstructionsFloods, +InstructionsColdWeather\"")
    print("Note that the transition is automatically ordered and not case sensitive.\n However, this prototype does not check whether your transition leads to a valid system state.")
    RISsystem = RIS()
    iter = 1
    while True:
        print("================= Test number " + str(iter) + "================================")
        answer = input("Please enter transition to be executed, or \"exit\" to terminate execution :")
        if answer.lower() != "exit":
            return
        RISsystem.transition(answer)
        print("Current emergency level : " + str(RISsystem.emergencyLevel))
        iter += 1

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
