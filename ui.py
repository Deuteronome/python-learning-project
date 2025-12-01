import tkinter as tk

#créer un fenêtre
root = tk.Tk()
print("ok")

#personalisation - color 1 : #93123D - color 2 : #ACAEC2
root.title("MyApp")
root.geometry("500x500")
root.minsize(300,250)
root.iconbitmap("./src/pos.ico")
root.configure(bg="#93123D")

#Afficher la fenêtre
root.mainloop()
