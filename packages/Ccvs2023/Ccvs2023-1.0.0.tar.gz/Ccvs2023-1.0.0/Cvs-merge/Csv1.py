import pandas as pd
import tkinter as tk
from tkinter import filedialog

def melanje_fichye_csv():
    # Fonksyon sa a pral melanje de fichye CSV
    fichye1 = filedialog.askopenfilename(title="Chwazi premye fichye CSV")
    fichye2 = filedialog.askopenfilename(title="Chwazi dezyèm fichye CSV")

    # Verifye ke fichye yo byen chwazi
    if not fichye1 or not fichye2:
        return

    try:
        Fich1 = pd.read_csv(fichye1)
        Fich2 = pd.read_csv(fichye2)
    except pd.errors.EmptyDataError:
        print("Erè: Youn oswa plizyè fichye yo vid.")
        return
    except pd.errors.ParserError:
        print("Erè: Kontni a nan yon oswa plizyè fichye yo pa bon format CSV.")
        return

    # Melanje done yo
    try:
        df_melanje = pd.concat([Fich1, Fich2], ignore_index=True)
    except ValueError:
        print("Erè: Nom kòlon ki idantik, se jis kondisyonere premye kolòn nan.")
        return

    # Chwazi kote ou vle sovegade nouvo fichye a
    fichye_sove = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("Fichye CSV", "*.csv")])

    # Verifye ke fichye sovegade a byen chwazi
    if not fichye_sove:
        return

    df_melanje.to_csv(fichye_sove, index=False)

    print(f"Melanj la kreye kòrèkteman. W'ap jwenn li nan '{fichye_sove}'")

    # Femen fenèt la apre li fin melanje
    fenet.destroy()

# Kreye yon fenèt tkinter
fenet = tk.Tk()
fenet.title("Melanj Fichye CSV")

# Kreye bouton pou lansman fonksyon melanje_fichye_csv
bouton_melanje = tk.Button(fenet, text="Melanj Fichye CSV", command=melanje_fichye_csv)
bouton_melanje.pack(pady=30)

# Lanse bouk la
fenet.mainloop()
