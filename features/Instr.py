def activate(RIS):
    # if RIS.featuresFutureStatus['Map']:
    if RIS.featuresFutureStatus['Map'] or RIS.featuresStatus['Map']:
        RIS.widgetBelow.configure(text="This is the Instructions Widget.")
    else:
        RIS.widgetAbove.configure(text="This is the Instructions widget.")


def deactivate(RIS):
    RIS.widgetBelow.configure(text="This is empty space.")
    if not RIS.featuresStatus['Map']:
        RIS.widgetAbove.configure(text="This is the Instructions Widget.")
        RIS.widgetBelow.configure(text="This is empty space.")