import tkinter as tk

def on_button_click():

    print('Kliknięto przycisk')

root = tk.Tk()


button = tk.Button(root, text='Kliknij mnie', command=on_button_click)
button.pack()

root.mainloop()
