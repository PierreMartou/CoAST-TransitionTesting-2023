def activate(RIS):
    widget = RIS.widgetBelow if "Instructions" in RIS.widgetBelow.cget("text") else RIS.widgetAbove
    # widget.configure(text=widget.cget("text")+" Instructions on Cold weather displayed.")
    widget.configure(text="This is the Instructions widget. Instructions on Flood are displayed.")


def deactivate(RIS):
    widget = RIS.widgetBelow if "Flood" in RIS.widgetBelow.cget("text") else RIS.widgetAbove
    if RIS.featuresStatus['InstrColdWeather'] and RIS.featuresFutureStatus['InstrColdWeather']:
        widget.configure(text="This is the Instructions widget. Instructions on Cold weather displayed.")
    else:
        widget.configure(text="This is the Instructions widget.")
