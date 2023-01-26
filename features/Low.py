def activate(RIS):
    # if RIS.emergencyLevel == 0:
    if RIS.emergencyLevel < 2:
        RIS.emergencyLevel += 1


def deactivate(RIS):
    if not RIS.featuresFutureStatus['High']:
        RIS.emergencyLevel = 0
