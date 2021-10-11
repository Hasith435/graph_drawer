from tkinter import *
import tkinter as tk
import tkinter.font as tkFont
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np


#essential colors
root_bg = "#1C1C1C"
enter_button_bg = "#1aeb8d"
back_button_color = "#e84d1a"
enter_button_hover_color = "#63ed28"
back_button_hover_color = "#eb6709"
light_color_frame = "#404036"

root = Tk()
root.title('Graph Drawer')
root.configure(bg=root_bg)

#essential fonts
style1 = tkFont.Font(family= "Comic Sans MS", size=15) #general text
style2 = tkFont.Font(family= "corbel light", size = 15, weight= "bold")#for enter or submit buttons
style3 = tkFont.Font(family= "corbel light", size= 13) #for entry fields
style4 = tkFont.Font(family="corbel bold", size= 13) #bold corbel
style5 = tkFont.Font(family="corbel bold", size=12) #button text

class HoverButton(tk.Button):
    def __init__(self, master, **kw):
        tk.Button.__init__(self, master=master, **kw)
        self.default_bg = self["bg"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['bg'] = self['activebackground']

    def on_leave(self, e):
        self['bg'] = self.default_bg

def create_frame(popup, colour, row=0, column=0, padx=20, pady=20, sticky=NSEW, columnspan=1, rowspan=1):
    frame = LabelFrame(popup, padx=padx, pady=pady, borderwidth=0)
    frame.configure(bg=colour)
    frame.grid(row=row, column=column, sticky=sticky, columnspan=columnspan, rowspan=rowspan)
    return frame

#frame contaning the equation enter fields and the enter button
eq_enter_frame = create_frame(root, light_color_frame, pady=30, padx=50)

eq_lbl = Label(eq_enter_frame, text="Equation:", font=style1, bg=light_color_frame, fg='white')
eq_input_box = Entry(eq_enter_frame,bg="#2e2e2d", foreground="#FFFFFF", borderwidth=0, width=40,font=style3)
enter_button = HoverButton(eq_enter_frame, text="Enter",font=style5, bg=enter_button_bg, activebackground=enter_button_hover_color, borderwidth=0, width=40)

eq_lbl.grid(row=0, column=0, sticky=W, pady=10)
eq_input_box.grid(row=1, column=0)
enter_button.grid(row=2, column=0, pady=10)

#frame containing the graph
graph_frame = create_frame(root, root_bg, column=1, rowspan=2)

# fig = Figure(figsize=(5,5), dpi=100)
#
# x = np.linspace(-5,5,100)
#
# plot = fig.add_subplot(111)
# plot.plot(x, 5*x+3, '-r', label="graph")
#
# canvas = FigureCanvasTkAgg(fig, graph_frame)
# canvas.draw()
# canvas.get_tk_widget().pack()

fig = Figure(figsize=(5,5), dpi=100)
plot = fig.add_subplot(111)
x = np.linspace(-5,5, 100)

plot.plot(x, x*x, '-r',label="graph")
plot.grid()
plot.axhline()
plot.axvline()
plot.set_xlim([-6,6])
plot.set_ylim([-6,6])

canvas = FigureCanvasTkAgg(fig, graph_frame)
canvas.draw()
canvas.get_tk_widget().pack()






root.mainloop()


