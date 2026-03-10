import tkinter as tk
from tkinter import ttk

# Wechselkurse
rates = {
    "Euro": 1.0,
    "Yen": 160,
    "Schwedische Kronen": 11.2,
    "Bosnische Mark": 1.95583,
    "Türkische Lira": 35,
    "USD": 1.1  # NEU: US-Dollar als zusätzliche Währung
   
}
print("Hallo")
# Funktion zum Umrechnen
def convert():
    try:
        amount = float(entry.get())
        from_currency = from_box.get()
        to_currency = to_box.get()

        euro = amount / rates[from_currency]
        result = euro * rates[to_currency]

        result_label.config(text=str(round(result, 2)) + " " + to_currency)
    except ValueError:
        result_label.config(text="Bitte Zahl eingeben!")

# GUI erstellen
root = tk.Tk()
root.title("Currency Converter - My Feature")

# Betrag
tk.Label(root, text="Betrag").pack()
entry = tk.Entry(root)
entry.pack()

# Von Währung
tk.Label(root, text="Von").pack()
from_box = ttk.Combobox(root, values=list(rates.keys()))
from_box.pack()
from_box.current(0)

# Nach Währung
tk.Label(root, text="Nach").pack()
to_box = ttk.Combobox(root, values=list(rates.keys()))
to_box.pack()
to_box.current(1)

# Button Umrechnen
tk.Button(root, text="Umrechnen", command=convert).pack()

# Ergebnis
result_label = tk.Label(root, text="Ergebnis")
result_label.pack()

root.mainloop()