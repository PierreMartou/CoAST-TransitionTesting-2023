def activate(RIS):
    widget = RIS.widgetBelow if "Instructions" in RIS.widgetBelow.cget("text") else RIS.widgetAbove
    # widget.configure(text=widget.cget("text")+" Instructions on Cold weather displayed.")
    widget.configure(text="This is the Instructions widget. Instructions on Cold weather are displayed.")


def deactivate(RIS):
    widget = RIS.widgetBelow if "Cold weather" in RIS.widgetBelow.cget("text") else RIS.widgetAbove
    if RIS.featuresStatus['InstrFlood'] and RIS.featuresFutureStatus['InstrFlood']:
        widget.configure(text="This is the Instructions widget. Instructions on Flood displayed.")
    else:
        widget.configure(text="This is the Instructions widget.")
