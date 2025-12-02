import csv
import tkinter as tk

def open_csv():
    csv_test = tk.Label(int_frame, bg="#ACAEC2", fg="#93123D", text="C'est tout bon", font=("Courrier", 15))
    csv_test.pack(pady=20, padx=20, expand=True)


#créer un fenêtre
root = tk.Tk()

#personalisation - color 1 : #93123D - color 2 : #ACAEC2
root.title("MyApp")
root.geometry("750x500")
root.minsize(300,250)
root.iconbitmap("./src/pos.ico")
root.configure(bg="#93123D")

#composant
header_frame = tk.Frame(root, bg="#ACAEC2")
label_title = tk.Label(header_frame, text="POS APPLICATION", bg="#ACAEC2", fg="#93123D", font=("Courrier", 30))
label_title.pack(expand=True, fill="both", pady=20)
header_frame.pack(fill=tk.X, side=tk.TOP)

doc_frame = tk.Frame(root, bg="#93123D")
text_frame = tk.Frame(doc_frame, bg="#93123D", bd=1, relief=tk.SUNKEN)
label_text1 = tk.Label(text_frame, text="Cette application permet de génerer des feuille de route pour les stagiaires à partir des résultats du test de positionnement.\nFaites un export des résultats de la classe souhaitée sur That Quiz - sur l'appli, cliquez sur le bouton \"Choisir un fichier\" - choisissez le fichier d'export qui se trouve dans votre dossier  Téléchargement.\nAccédez aux feuilles de route en cliquant sur le bouton \"Accéder aux résultats\" quand il apparait", bg="#93123D", fg="#ACAEC2", font=("Courrier", 13),wraplength=300, justify=tk.LEFT)
label_text1.pack(pady=15, padx=15)

text_frame.pack(expand=True, pady=20, padx=20)
doc_frame.pack(side=tk.LEFT, fill=tk.Y)


int_frame = tk.Frame(root, bg="#93123D")
csv_button = tk.Button(int_frame,text="Choisir un fichier", font=("Courrier", 15), bg="#ACAEC2", fg="#93123D", command=open_csv)
csv_button.pack(pady=20, padx=20, expand=True)
int_frame.pack(side=tk.RIGHT, fill=tk.Y )


#Afficher la fenêtre
root.mainloop()
