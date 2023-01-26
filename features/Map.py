def activate(RIS):
    RIS.widgetAbove.configure(text="This is the Map widget.")
    if RIS.featuresStatus['Instr'] and RIS.featuresFutureStatus['Instr']:
        RIS.widgetBelow.configure(text="This is the Instructions Widget.")


def deactivate(RIS):
    RIS.widgetAbove.configure(text="This is empty space.")
    if RIS.featuresStatus['Instr'] and RIS.featuresFutureStatus['Instr']:
        RIS.widgetAbove.configure(text="This is the Instructions Widget.")
        RIS.widgetBelow.configure(text="This is empty space.")
