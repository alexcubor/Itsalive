import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog

def open_folder_dialog():
    file_path = r"\\alpha\tools\Itsalive\It's Maya 2022.ink"
    subprocess.Popen(f'explorer /select,"{file_path}"')

root = tk.Tk()
root.title("Не пугайся, всё будет как и прежде")
root.geometry("500x200")

title = tk.Label(root, text="Эта версия Maya не изменилась, но у неё поменялось место. "
                            "Что бы дальше использовать её, удали пожалуйста этот ярлык на рабочем столе, "
                            "и скопируй себе новый ярлык It's Maya 2022")
open_folder_button = tk.Button(root, text="Открыть папку с новыми ярлыками", command=open_folder_dialog)
open_folder_button.pack(pady=50)

root.mainloop()
