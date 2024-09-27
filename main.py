from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import re
# setting
root = Tk()
icon = PhotoImage(file="icon.png")
root.iconphoto(True, icon)
root.title("Boletos")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

window_width = 500
window_height = 200

x_coord = int((screen_width - window_width) / 2)
y_coord = int((screen_height - window_height) / 2)

root.geometry(f"{window_width}x{window_height}+{x_coord}+{y_coord}")

# frame 1
frm = ttk.Frame(root, padding=10)
frm.grid()
root.grid_columnconfigure(0, weight=1)

# dropdown list 1
combo1 = ttk.Combobox(root, values=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "exec"], state="readonly")
combo1.grid(column=0,row=0, sticky="ew", padx=10, pady=10)
combo1.set("selecione o beneficiário")

# dropdown list 2
combo2 = ttk.Combobox(root, values=["tipo 1", "tipo 2", "tipo 3"], state="readonly")
combo2.grid(column=1, row=1)
combo2.set("selecione o tipo de compra")

# validation

def validadeDateFormat(char, entry):
    if entry == "":
        return True
    
    pattern = r"^(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/([0-9]{4})$"
    if re.match(pattern, entry):
        return True
    else:
        False

def validadeValueFormat(char, entry):
    if entry == "":
        return True
    
    pattern = r"^\d+,(\d{2})$"
    
    if re.match(pattern, entry):
        return True
    else:
        False

def onSubmit():
    value = entry3.get()
    if validadeValueFormat(None, value):
        messagebox.showinfo("O valor está no formato correto")
    else:
        messagebox.showerror("O valor não está no formato correto")

vcmd = (root.register(validadeDateFormat), "%S", "%P")
vcmd2 = (root.register(validadeDateFormat), "%S", "%P")
# entry 1

entry1 = ttk.Entry(root, validate="key", validatecommand=vcmd)
entry1.grid(column=0, row=2)

entry2 = ttk.Entry(root, validate="key", validatecommand=vcmd)
entry2.grid(column=1, row=2)

entry3 = ttk.Entry(root, validate="key", validatecommand=vcmd2)
entry3.grid(column=2, row=2)

submit_btn = ttk.Button(root, text="Validar Número", command=onSubmit)
submit_btn.grid (column=0, row=2)
root.mainloop()