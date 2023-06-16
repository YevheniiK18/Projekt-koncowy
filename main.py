import tkinter as tk

def on_button_click():
    # Obsługa kliknięcia przycisku
    print('Kliknięto przycisk')

root = tk.Tk()

# Dodanie elementów UI
button = tk.Button(root, text='Kliknij mnie', command=on_button_click)
button.pack()

# Uruchomienie głównej pętli UI
root.mainloop()
