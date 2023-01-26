import tkinter as tk


def activate(RIS):
    RIS.window = tk.Tk()
    widgetTitle = tk.Label(RIS.window, text="This is the GUI associated to the RIS system.")
    RIS.widgetAbove = tk.Label(RIS.window, text="Empty space.")
    RIS.widgetBelow = tk.Label(RIS.window, text="Empty space.")
    widgetTitle.pack()
    RIS.widgetAbove.pack()
    RIS.widgetBelow.pack()


def deactivate(RIS):
    RIS.window.close()
    RIS.window = None
