import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
import subprocess

def open_folder_dialog():
    file_path = r"\\alpha\tools\Itsalive\It's Maya 2022.lnk"
    subprocess.Popen(f'explorer /select,"{file_path}"')

root = tk.Tk()
root.title("Не пугайся, всё будет как и прежде")
root.geometry("500x200")

label = tk.Label(root, text="Эта версия Maya не изменилась, но у неё поменялось место. \n"
                            "Что бы дальше использовать её, \n"
                            "удали пожалуйста этот ярлык на рабочем столе, \n"
                            "и скопируй себе новый ярлык It's Maya 2022")
label.pack(pady=10)
open_folder_button = tk.Button(root, text="Открыть папку с новыми ярлыками", command=open_folder_dialog)
open_folder_button.pack(pady=10)

root.mainloop()
