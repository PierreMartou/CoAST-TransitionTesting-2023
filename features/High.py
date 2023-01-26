def activate(RIS):
    RIS.emergencyLevel = 2


def deactivate(RIS):
    if RIS.featuresFutureStatus['Low']:
        RIS.emergencyLevel = 1
    else:
        RIS.emergencyLevel = 0