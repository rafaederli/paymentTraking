from tkinter import *
from tkinter import ttk

# setting
root = Tk()
icon = PhotoImage(file="icon.png")
root.iconphoto(True, icon)
root.title("Contas a Pagar")

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

# dropdown list 1
combo1 = ttk.Combobox(frm, values=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "exec"], state="readonly")
combo1.grid(column=0,row=0)
combo1.set("selecione o beneficiário")

# dropdown list 2
combo2 = ttk.Combobox(frm, values=["tipo 1", "tipo 2", "tipo 3"], state="readonly")
combo2.grid(column=1, row=0)
combo2.set("selecione o tipo de compra")


root.mainloop()