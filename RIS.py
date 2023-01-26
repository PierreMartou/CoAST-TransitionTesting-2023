import PySimpleGUI as sg
from features import EmergencyLevel, High, Low, Widget, Map, Instr, InstrColdWeather, InstrFlood
from time import sleep

class RIS:
    # Initializes main components of the RIS system to None.
    # Lists all possible features, and initializes them all to False.
    # featuresFutureStatus will be used during transitions.
    def __init__(self):
        self.emergencyLevel = None
        self.window = None
        self.widgetAbove = None
        self.widgetBelow = None
        # sg.Window(title="Widgets", layout=[[]], margins=(100, 50)).read()

        self.features = ["EmergencyLevel", "Low", "High", "Widget", "Map", "Instr",
                         "InstrColdWeather", "InstrFlood"]

        self.featuresStatus = {f: False for f in self.features}
        self.featuresFutureStatus = self.featuresStatus.copy()

    # Reads transition as described in the paper and apply them to the RIS system.
    def transition(self, transitionsText):
        transitionsText = transitionsText.lower().replace(" ", "").replace("instructions", "instr").strip()
        transitions = transitionsText.split(",")

        toActivate = {f: None for f in self.features}
        toDeactivate = {f: None for f in self.features}
        featuresLower = [f.lower() for f in self.features]
        for t in transitions:
            if t[1:].lower() not in featuresLower:
                print("This transition was not recognized: " + str(t) + ". The transition was aborted.")
                return False
            feature = self.features[featuresLower.index(t[1:].lower())]

            if t[0:1] == "+":
                self.featuresFutureStatus[feature] = True
                if self.featuresStatus[feature]:
                    print("This transition cannot be executed, as the feature is already activated: " + str(t))
                    return False
                toActivate[feature] = getattr(globals()[feature], 'activate')
            else:
                self.featuresFutureStatus[feature] = False
                if not self.featuresStatus[feature]:
                    print("This transition cannot be executed, as the feature is already deactivated: " + str(t))
                    return False
                toDeactivate[feature] = getattr(globals()[feature], 'deactivate')

        for i in range(len(self.features)-1, -1, -1):
            func = toDeactivate[self.features[i]]
            if func is not None:
                func(self)
        for i in range(len(self.features)):
            func = toActivate[self.features[i]]
            if func is not None:
                func(self)

        self.featuresStatus = self.featuresFutureStatus.copy()

        if self.featuresStatus['Widget']:
            self.window.update()
            sleep(0.05)

        print("Transition completed : " + str(transitions))
        if not self.emergencyLevelValidity():
            print("!!! Error detected in the current configuration, unexpected emergency level !!!")
        if not self.windowValidity():
            print("!!! Error detected in the current configuration, unexpected window layout !!!")

    # This verifies the correctness of the current emergency level.
    # Returns True if everything is valid.
    def emergencyLevelValidity(self):
        if self.featuresStatus['High'] and self.emergencyLevel == 2:
            return True
        if self.featuresStatus['Low'] and self.emergencyLevel == 1:
            return True
        if not self.featuresStatus['High'] and not self.featuresStatus['Low'] and self.emergencyLevel == 0:
            return True
        if not self.featuresStatus['EmergencyLevel'] and self.emergencyLevel is None:
            return True
        return False

    # This verifies the correctness of the current window displayed.
    # Returns True if everything is valid.
    def windowValidity(self):
        if self.featuresStatus['InstrColdWeather'] and 'Cold weather' not in self.widgetBelow.cget("text") and 'Cold weather' not in self.widgetAbove.cget("text"):
            return False
        if self.featuresStatus['InstrFlood'] and 'Flood' not in self.widgetBelow.cget("text") and 'Flood' not in self.widgetAbove.cget("text"):
            return False
        if "empty space" in self.widgetAbove.cget("text") and "empty space" not in self.widgetBelow.cget("text"):
            return False
        return True

