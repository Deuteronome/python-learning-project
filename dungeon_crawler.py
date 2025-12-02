import tkinter as tk

# couleurs - main : #413642 - sec : #c5d3d5

#fenêtre de l'application
root = tk.Tk()
root.title("Crawler")
root.geometry("720x480")
root.iconbitmap("./src/crawler.ico")
root.configure(bg="#413642")

#frame principale
frame = tk.Frame(root, bg="white", bd=1, relief=tk.SUNKEN)

#titre
header=tk.Frame(frame, bg="#c5d3d5")
title = tk.Label(header, text="Dungeon Crawler", font=("Courrier", 25), fg="#413642", bg="#c5d3d5")
title.pack(expand=tk.YES, fill=tk.BOTH)

#canva
width = 300
height = 300
image = tk.PhotoImage(file="./src/donjon.png").zoom(18).subsample(32)
canvas = tk.Canvas(frame, width=width, height=height, background="#413642", bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)

right_frame = tk.Frame(frame, bg="white")
test = tk.Label(right_frame, text="coucou")
test.pack()

canvas.grid(row=1, column=0, columnspan=1)
right_frame.grid(row=1, column=1, columnspan=1)
header.grid(row=0, column=0,columnspan=2, sticky=tk.EW, ipady=20, ipadx=20)


frame.pack(expand=tk.YES, fill=tk.BOTH)

root.mainloop()


