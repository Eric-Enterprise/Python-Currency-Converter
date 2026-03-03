import customtkinter as ctk

rates = {
    "EUR": 1.0,
    "USD": 1.1,
    "JPY": 160.0,
    "SEK": 11.5
}

def convert():
    amount = float(entry.get())
    from_currency = from_box.get()
    to_currency = to_box.get()

    eur = amount / rates[from_currency]
    result = eur * rates[to_currency]

    result_label.configure(
        text=f"{amount:.2f} {from_currency} = {result:.2f} {to_currency}"
    )

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Währungsrechner")
root.geometry("350x300")

entry = ctk.CTkEntry(root, placeholder_text="Betrag eingeben")
entry.pack(pady=10)

from_box = ctk.CTkComboBox(root, values=list(rates.keys()))
from_box.pack(pady=5)
from_box.set("EUR")

to_box = ctk.CTkComboBox(root, values=list(rates.keys()))
to_box.pack(pady=5)
to_box.set("USD")

ctk.CTkButton(root, text="Umrechnen", command=convert).pack(pady=10)

result_label = ctk.CTkLabel(root, text="")
result_label.pack(pady=10)

root.mainloop()