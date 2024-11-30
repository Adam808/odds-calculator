from tkinter import *
from tkinter import ttk
from decimal import Decimal


def convert(self):

    odds_type = odds_combobox.get()
    odds_flt = float(odds.get())
    real_odds_flt = float(real_odds.get())

    if odds_type == 'American':
        if odds_flt < 0:
            res = round(Decimal((abs(odds_flt) / (abs(odds_flt) + 100)) * 100), 2)
            prop_gain = 100 / abs(odds_flt)
        elif odds_flt > 0:
            res = round(Decimal((100 / (odds_flt + 100)) * 100), 2)
            prop_gain = abs(odds_flt) / 100

        prob.set(str(res) + '%')

    elif odds_type == 'Percentage':
        res = round(Decimal(1 / odds_flt - 1), 2)
        prop_gain = 1 / odds_flt - 1
        prob.set(str(res))

    k_crit = round(Decimal((real_odds_flt - (1-real_odds_flt) / prop_gain) * 100), 2)
    
    kelly.set(str(k_crit) + '%')



# gui
root = Tk()
root.title('Odds Calculator')

frame = ttk.Frame(root, padding='2 2 2 2')
frame.grid(column=0, row=0, sticky=(N, W, E, S))

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

odds = StringVar(root)
prob = StringVar(root)
real_odds = StringVar(root)
kelly = StringVar(root)

ttk.Label(frame, text='Odds: ').grid(column=0, row=0, sticky=W)
odds_value = ttk.Entry(frame, textvariable=odds).grid(column=1, row=0, sticky=W)

odds_combobox = ttk.Combobox(frame, values=['American', 'Percentage'], state='readonly')
odds_combobox.grid(column=2, row=0, sticky=W)
odds_combobox.current(0)

ttk.Label(frame, text='Prob(1-?): ').grid(column=0, row=1, sticky=W)
ttk.Label(frame, textvariable=prob).grid(column=1, row=1, sticky=W)
ttk.Label(frame, text='Real Prob: ').grid(column=0, row=2, sticky=W)
real_odds_value = ttk.Entry(frame, textvariable=real_odds).grid(column=1, row=2, sticky=W)
ttk.Label(frame, text='Kelly: ').grid(column=0, row=4, sticky=W)
ttk.Label(frame, textvariable=kelly).grid(column=1, row=4, sticky=W)

root.bind('<Return>', convert)

root.attributes('-topmost', True)
root.minsize(300, 200)

for child in frame.winfo_children():
    child.grid_configure(padx=2, pady=2)

root.mainloop()