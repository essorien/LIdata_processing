import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import os


def choose_folder():
    folder_path = filedialog.askdirectory()  # Open folder selection dialog
    folder_path_var.set(folder_path)


def process_files():
    folder_path = folder_path_var.get()
    if not folder_path:
        tk.messagebox.showerror("Error", "Select folder with files!")
        return

    df = pd.DataFrame()

    files = sorted([f for f in os.listdir(folder_path) if f.endswith(".txt")])

    for i, filename in enumerate(files):
        file_path = os.path.join(folder_path, filename)
        temp_df = pd.read_csv(file_path, sep="\t", header=None)

        if i > 0:
            temp_df = temp_df.iloc[2:]

        df = pd.concat([df, temp_df])

    df = df.dropna(axis=1, thresh=df.shape[0] - 100)

    current_directory = os.getcwd()
    excel_file = os.path.join(current_directory, "output.xlsx")
    df.to_excel(excel_file, index=False)
    tk.messagebox.showinfo("Ready", f"Table has been saved to {excel_file}!")


root = tk.Tk()
root.title("Cleaning txt-files")

choose_folder_button = tk.Button(root, text="Select folder", command=choose_folder)
choose_folder_button.pack(pady=10)
folder_path_var = tk.StringVar()
folder_path_entry = tk.Entry(root, textvariable=folder_path_var)
folder_path_entry.pack()
process_files_button = tk.Button(root, text="Process data", command=process_files)
process_files_button.pack(pady=10)
status_label = tk.Label(root, text="")
status_label.pack()

root.mainloop()
