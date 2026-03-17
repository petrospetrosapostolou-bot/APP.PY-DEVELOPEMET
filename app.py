
import os
import tkinter as tk
from tkinter import ttk, simpledialog, messagebox

APP_PATH = os.path.dirname(os.path.abspath(__file__))
DATA_FOLDER = os.path.join(APP_PATH, "data")
LANG_FOLDER = os.path.join(APP_PATH, "languigee")

root = tk.Tk()
root.title("App")
root.geometry("500x400")

# Ask user language at startup
available_langs = [f.replace(".txt","") for f in os.listdir(LANG_FOLDER)]
chosen_lang = simpledialog.askstring("Language", f"Hello! Choose your type for reading text:\nOptions: {', '.join(available_langs)}")

if chosen_lang not in available_langs:
    chosen_lang = "english"  # default fallback

tabs = ttk.Notebook(root)
tabs.pack(fill="both", expand=True)

# ----------------------
# TAB 1: Make File
# ----------------------
tab1 = tk.Frame(tabs)
tabs.add(tab1, text="Make File")

canvas = tk.Canvas(tab1, bg="black")
canvas.pack(fill="both", expand=True, pady=(10,0))

file_listbox = tk.Listbox(tab1, width=50)
file_listbox.pack(pady=10)

def refresh_file_list():
    file_listbox.delete(0, tk.END)
    for f in os.listdir(DATA_FOLDER):
        file_listbox.insert(tk.END, f)

def create_new_file():
    filename = simpledialog.askstring("New File", "Enter file name:")
    if filename:
        path = os.path.join(DATA_FOLDER, filename)
        if not os.path.exists(path):
            with open(path, "w") as f:
                f.write("")  # create empty file
            refresh_file_list()
        else:
            messagebox.showerror("Error", "File already exists.")

btn_create = tk.Button(tab1, text="Create File", command=create_new_file)
btn_create.pack(pady=5)

refresh_file_list()

# ----------------------
# TAB 2: Other
# ----------------------
tab2 = tk.Frame(tabs)
tabs.add(tab2, text="Other")

label = tk.Label(tab2, text="Coming soon...")
label.pack(pady=20)

root.mainloop()
