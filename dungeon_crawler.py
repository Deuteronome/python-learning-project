import tkinter as tk

# couleurs - main : #413642 - sec : #c5d3d5

#fenêtre de l'application
root = tk.Tk()
root.title("Crawler")
root.geometry("720x480")
root.iconbitmap("./src/crawler.ico")
root.configure(bg="#413642")

#frame principale
frame = tk.Frame(root, bg="#413642")

#titre
header=tk.Frame(root, bg="#c5d3d5")
title = tk.Label(header, text="Dungeon Crawler", font=("Courrier", 25), fg="#413642", bg="#c5d3d5")
title.pack(expand=tk.YES, fill=tk.BOTH)

header.pack(fill=tk.X, ipady=20, side=tk.TOP)

#canva
width = 300
height = 300
image = tk.PhotoImage(file="./src/donjon.png").zoom(18).subsample(32)
canvas = tk.Canvas(frame, width=width, height=height, background="white", bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)

right_frame = tk.Frame(frame, bg="white")
test = tk.Label(right_frame, text="coucou")
test.pack(expand=tk.YES, fill=tk.BOTH, side=tk.RIGHT)

canvas.grid(row=0, column=0)
right_frame.grid(row=0, column=1, sticky=tk.W)

frame.grid_rowconfigure(0, weight=1)
frame.grid_columnconfigure(0, weight=1)
frame.grid_columnconfigure(1, weight=1)



frame.pack(expand=tk.YES, fill=tk.BOTH)

root.mainloop()


