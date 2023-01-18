from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3 as sq
import os
from connexion import connect_to_db
from PIL import Image, ImageTk
from tkcalendar import DateEntry
from datetime import datetime

def inscription():
    """Fonction d'inscription de l'utilisateur"""
    username = entre_nom.get()
    password = entre_pass.get()
    filename = os.listdir()

    if str(username) == "" or str(password) == "":
        messagebox.showerror("School System", "Champs non remplis!", parent=fen)
    else:
        if str(username) + ".txt" in filename:
            messagebox.showerror("School System", "Ce nom d'utilisateur est déjà reservé", parent=fen)
        else:
            with open(str(username) + ".txt", "w") as f:
                f.write(str(username) + ":" + str(password))
                fen.destroy()
                messagebox.showinfo("School System", "Compte créé avec succès")


def authentification():
    """Fonction de vérification de compte utilisateur"""
    username = user_entry.get()
    password = pass_entry.get()
    filename = os.listdir()

    if str(username) == "" or str(password) == "":
        messagebox.showerror("School System", "Mot de passe ou Nom d'utilisateur érroné")
    else:
        if str(username) + ".txt" in filename:
            with open(str(username) + ".txt", "r") as file:
                f = file.read().split(":")
                if username == f[0] and password == f[1]:
                    root.destroy()
                    inscription_eleve()
                else:
                    messagebox.showerror("School System", "Mot de passe ou Nom d'utilisateur érroné")


def inscription_eleve():
    global window, nom, postnom, prenom, sexe, classe, option, date_inscription, nom_tut, num_tut, ident
    window = Tk()
    window.title('Inscription des élèves')
    window.geometry("1100x700+125+15")
    # window.config(background="#fff")
    window.resizable(False, False)

    titre_fen = Label(window, text="INSCRIPTION DES ELEVES DE L'I.T.P", fg="#5053E2", bg="#333", font=("arial", 24, "bold"))
    titre_fen.place(x=0, y=0, width=1100, height=80)

    image = Image.open("logo/logo.png")
    photo = ImageTk.PhotoImage(image, master=window)
    can = Canvas(window, width=image.size[0], height=image.size[1], bg="grey")
    logo = can.create_image(50,50, image=photo)
    can.place(x=988, y=82)

    # création labels
    lab_nom = Label(window, text="NOM:", font=("ms reference sans serif", 14,), fg="#333")
    lab_nom.place(x=10, y=115)
    lab_postnom = Label(window, text="POST-NOM:", font=("ms reference sans serif", 14,), fg="#333")
    lab_postnom.place(x=10, y=170)
    lab_prenom = Label(window, text="PRENOM:", font=("ms reference sans serif", 14,), fg="#333")
    lab_prenom.place(x=10, y=210)
    lab_classe = Label(window, text="CLASSE:", font=("ms reference sans serif", 14,), fg="#333")
    lab_classe.place(x=10, y=245)
    lab_option = Label(window, text="OPTION:", font=("ms reference sans serif", 14,), fg="#333")
    lab_option.place(x=10, y=288)
    lab_sexe = Label(window, text="SEXE:", font=("ms reference sans serif", 14,), fg="#333")
    lab_sexe.place(x=10, y=335)
    lab_nom_tut = Label(window, text="NOM DU TUTEUR:", font=("ms reference sans serif", 14,), fg="#333")
    lab_nom_tut.place(x=10, y=385)
    lab_num_tut = Label(window, text="NUMERO DU TUTEUR:", font=("ms reference sans serif", 14,), fg="#333")
    lab_num_tut.place(x=10, y=430)
    lab_dat_inscript = Label(window, text="DATE D'INSCRIPTION:", font=("ms reference sans serif", 14,), fg="#333")
    lab_dat_inscript.place(x=10, y=465)
    lab_id = Label(window, text='ID:', font=("ms reference sans serif", 14,), fg="#333")
    lab_id.place(x=10, y=503)

    # création champs de saisie
    nom=StringVar() 
    postnom=StringVar() 
    prenom=StringVar() 
    sexe=StringVar() 
    classe=StringVar() 
    option=StringVar() 
    date_inscription=StringVar() 
    nom_tut=StringVar() 
    num_tut=StringVar() 
    ident = StringVar()

    nom_txt = Entry(window, bg="white", textvariable=nom, font=("ms reference sans serif", 12))
    nom_txt.place(x=90, y=115, width=240, height=28)
    postnom_txt = Entry(window, bg="white", textvariable=postnom, font=("ms reference sans serif", 12))
    postnom_txt.place(x=138, y=170, width=240, height=28)
    prenom_txt = Entry(window, bg="white", textvariable=prenom,font=("ms reference sans serif", 12))
    prenom_txt.place(x=115, y=210, width=240, height=28)
    classe_txt = ttk.Combobox(window, textvariable=classe, font=("ms reference sans serif", 12), state="readonly")
    classe_txt["values"] = ("7", "8", "1", "2", "3", "4")
    classe_txt.place(x=115, y=245, width=240, height=28)
    classe_txt.current(0)
    option_txt= ttk.Combobox(window, textvariable=option, font=("ms reference sans serif", 12), state="readonly")
    option_txt["values"] = ("Electronique Industriel", "Electricité Général", "Mécanique Auto", "Mécanique machine", "Commérciale", "Pédagogie Générale", "Secondaire Général")
    option_txt.place(x=115, y=288, width=240, height=28)
    option_txt.current(6)
    sexe_txt = ttk.Combobox(window, textvariable=sexe, font=("ms reference sans serif", 12), state="readonly")
    sexe_txt["values"] = ("H", "F")
    sexe_txt.place(x=108, y=335, width=240, height=28)
    sexe_txt.current(0)
    date_inscription_txt = DateEntry(window, textvariable=date_inscription, date_pattern="dd/mm/yyyy", bg="white", font=("ms reference sans serif", 12))
    date_inscription_txt.place(x=240, y=465, width=240, height=28)
    nom_tut_txt = Entry(window, bg="white", font=("ms reference sans serif", 12), textvariable=nom_tut)
    nom_tut_txt.place(x=240, y=385, width=240, height=28)
    num_tut_txt = Entry(window, bg="white", textvariable=num_tut, font=("ms reference sans serif", 12))
    num_tut_txt.place(x=240, y=430, width=240, height=28)
    id_txt = Entry(window, bg="white", textvariable=ident, font=("ms reference sans serif", 12))
    id_txt.place(x=240, y=503, width=240, height=28)

    # créations des boutons
    btn_inscrire = Button(window, text="Inscrire l'élève", bg="#37399D", fg="#fff", bd=0, command=insere, font=("ms reference sans serif", 11))
    btn_inscrire.place(x=110 , y=600, width=138, height=33)
    btn_modif = Button(window, text="Modifier l'élève", bg="#37399D", fg="#fff", bd=0, command=modify, font=("ms reference sans serif", 11))
    btn_modif.place(x=300 , y=600, width=138, height=33)
    btn_supp = Button(window, text="Supprimer l'élève", bg="red", fg="#fff", bd=0, command=suppression, font=("ms reference sans serif", 11))
    btn_supp.place(x=480 , y=600, width=138, height=33)
    btn_table = Button(window, text="Lister les élèves", bg="#37399D", fg="#fff", bd=0, command=tableau_eleve, font=("ms reference sans serif", 11))
    btn_table.place(x=660 , y=600, width=138, height=33)
    btn_paye = Button(window, text="Payement", bg="#37399D", fg="#fff", bd=0, command=payement_frais, font=("ms reference sans serif", 11))
    btn_paye.place(x=840 , y=600, width=138, height=33)

    window.mainloop()


def payement_frais():
    global montant, dat_paye, code_recu, name, postname, win
    win = Tk()
    win.title('Payement des frais scolaire')
    win.geometry("880x460+240+140")
    # win.config(background="#fff")
    win.resizable(0, 0)

    titre_fen = Label(win, text="PAYEMENT FRAIS SCOLAIRE", fg="#5053E2", bg="#333", font=("arial", 24, "bold"))
    titre_fen.place(x=0, y=0, width=900, height=80)
    
    lab_montant_txt = Label(win, text="MONTANT:", font=("ms reference sans serif", 14,), fg="#333")
    lab_montant_txt.place(x=10, y=90)
    lab_dat_txt = Label(win, text="DATE DE PAYEMENT:", font=("ms reference sans serif", 14,), fg="#333")
    lab_dat_txt.place(x=10, y=140)
    lab_code_txt = Label(win, text="N° Reçu:", font=("ms reference sans serif", 14,), fg="#333")
    lab_code_txt.place(x=10, y=190)
    lab_name_txt = Label(win, text="NOM DE L'ELEVE:", font=("ms reference sans serif", 14,), fg="#333")
    lab_name_txt.place(x=10, y=240)
    lab_postname_txt = Label(win, text="POST-NOM DE L'ELEVE:", font=("ms reference sans serif", 14,), fg="#333")
    lab_postname_txt.place(x=10, y=290)

    montant = Entry(win, bg="white", font=("ms reference sans serif", 12))
    montant.place(x=130, y=90, width=240, height=28)
    dat_paye = DateEntry(win, bg="white", font=("ms reference sans serif", 12), state='readonly', date_pattern='dd/mm/yyyy')
    dat_paye.place(x=230, y=140, width=240, height=28)
    code_recu = Entry(win, bg="white", font=("ms reference sans serif", 12))
    code_recu.place(x=110, y=190, width=240, height=28)
    name = Entry(win, bg="white", font=("ms reference sans serif", 12))
    name.place(x=210, y=240, width=240, height=28)
    postname = Entry(win, bg="white", font=("ms reference sans serif", 12))
    postname.place(x=260, y=290, width=240, height=28)

    btn_paye = Button(win, text="Payer les frais", bg="#37399D", fg="#fff", bd=0, command=paye, font=("ms reference sans serif", 11))
    btn_paye.place(x=340 , y=400, width=138, height=33)


def payement(mnt, dat, recu, nom, pstnom):
    try:
        con = connect_to_db()
        c = con.cursor()
        c.execute("""UPDATE eleves SET montant_paye='{0} FC', date_payement='{1}', code_recu={2} WHERE nom='{3}' AND postnom='{4}'
            """.format(float(mnt), str(dat), int(recu), str(nom).title(), str(pstnom).title()))
        con.commit()
        con.close()
    except Exception as e:
        print(e)


def paye():
    if name.get() == "" or postname.get() == "":
        messagebox.showerror("School System", "Spécifiez le nom complet de l'élève qui paye les frais", parent=win)
    else:
        if str(montant.get()) == "" or str(dat_paye.get()) == "" or str(code_recu.get()) == "":
            messagebox.showerror("School System", "Remplissez tout les champs", parent=win)
        else:
            payement(float(montant.get()), str(dat_paye.get()), int(code_recu.get()), str(name.get().title()), str(postname.get().title()))
            restor()
            messagebox.showinfo("School System", "OK", parent=win)


def restor():
    montant.delete(0, END)
    dat_paye.delete(0, END)
    code_recu.delete(0, END)
    name.delete(0, END)
    postname.delete(0, END)


def reini():
    nom.set('')
    postnom.set('')
    prenom.set('')
    sexe.set("H")
    classe.set("7")
    option.set("Secondaire Général")
    date_inscription.set('')
    nom_tut.set('')
    num_tut.set('')
    ident.set('')


def insere():
    if nom.get() == "" or postnom.get() == "" or prenom.get() == "" or nom_tut.get() == "": 
        messagebox.showerror("School System", "Vous n'avez pas rempli tous les champs requis")
    else:
        inserer_eleve(window, nom.get().title(), postnom.get().title(), prenom.get().title(), sexe.get().title(), classe.get().title(), option.get().title(), date_inscription.get(), nom_tut.get().title(), num_tut.get().title())
        reini()
        messagebox.showinfo("School System", "Elèves enrégistré", parent=window)


def inserer_eleve(root ,nom, pstnom, prenom, sexe, classe, option, dat, nom_tut, num_tut):
    try:
        db = connect_to_db()
        cur = db.cursor()
        datas = (str(nom).title(), str(pstnom).title(), str(prenom).title(), str(sexe), str(classe), str(option), str(dat), str(nom_tut).title(), str(num_tut))
        cur.execute("""INSERT INTO eleves(nom, postnom, prenom, sexe, classe, option, 
            date_inscription, nom_tuteur, num_tuteur) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?)""", datas)
        db.commit()
        db.close()
    except Exception as e:
        print(e)
        print("Impossible de se connecter dans la base de données")


def affiche_eleves():
    con = connect_to_db()
    cur = con.cursor()
    cur.execute("SELECT* FROM eleves")
    row = cur.fetchall()
    con.commit()

    return row


def modify():
    if ident.get() == "":
        messagebox.showerror("School System", "Entrez l'identifiant (Id) de l'élève", parent=window)
    else:
        if nom.get() == "" or postnom.get() == "" or prenom.get() == "" or nom_tut.get() == "":
            messagebox.showerror("School System", "Entrez les nouvelles informations de l'élève", parent=window)
        else:
            modifier_eleve(ident.get(), nom.get().title(), postnom.get().title(), prenom.get().title(), sexe.get().title(), classe.get().title(), option.get().title(), date_inscription.get(), nom_tut.get().title(), num_tut.get().title())
            reini()
            messagebox.showinfo("School System", "Les données de cet élève ont été modifées", parent=window)


def modifier_eleve(idd, nom, pstnom, prenom, sexe, classe, option, dat, nom_tut, num_tut):
    try:
        con = connect_to_db()
        c = con.cursor()
        c.execute("""UPDATE eleves SET nom='{0}', postnom='{1}', prenom='{2}' , sexe='{3}', classe='{4}', 
            option='{5}', date_inscription='{6}', nom_tuteur='{7}', num_tuteur='{8}' WHERE id={9}""".format(str(nom), str(pstnom), str(prenom), str(sexe), str(classe), str(option), str(dat), str(nom_tut), num_tut, idd))
        con.commit()
        con.close()
    except Exception as e:
        print(e)


def suppression():
    if ident.get() == "":
        messagebox.showerror("School System", "Spécifiez l'identifiant de l'élève que vous voullez supprimer")
    else:
        msg = messagebox.askyesno('Avertissement', "Cette action est irréversible\nVoullez-vous toujours supprimer cet élève ?")
        if msg:
            supprimer_eleve(ident.get())
            reini()
            messagebox.showinfo("School System", "Cet élève a été rétiré du Système scolaire")
        else:
            pass


def supprimer_eleve(idd):
    try:
        con = connect_to_db()
        c = con.cursor()
        c.execute("DELETE FROM eleves WHERE id=?", (idd,))
        con.commit()
        con.close()
    except Exception as e:
        print(e)


def rechercher_eleve(n):
    try:
        c = connect_to_db()
        cur = c.cursor()
        cur.execute("SELECT * FROM eleves WHERE nom LIKE'%" + str(n) + "%'")
        rows = cur.fetchall()
        
        if len(rows) != 0:
            for el in tree.get_children():
                tree.delete(el)
            for row in rows:
                tree.insert('', END, values=row)

        c.commit()
        c.close()

    except Exception as e:
        print(e)


def rechercher():
    if str(recherche) == "":
        messagebox.showerror("School System", "Entrez quelque chose avant de lancer la recherche")
    else:
        rechercher_eleve(recherche.get())
        recherche.set('')


def show_students():
    for stud in tree.get_children():
        tree.delete(stud)
    
    for student in affiche_eleves():
        tree.insert('', END, values=student)


def tableau_eleve():
    global tree, recherche
    fenetre = Toplevel()
    fenetre.title("Système scolaire")
    fenetre.geometry("1226x610")

    # Label
    lab_eleve = Label(fenetre, text="Elèves", font=("ms reference sans serif", 16))
    lab_eleve.place(x=550, y=0)

    # les scrollbar
    scrollX = Scrollbar(fenetre, orient=HORIZONTAL)
    scrollY = Scrollbar(fenetre, orient=VERTICAL)

    # champ de recherche
    recherche = StringVar()
    search_field = Entry(fenetre, textvariable=recherche, font=("ms reference sans serif", 11))
    search_field.place(x=680, y=5, width=170)

    # bouton recherche
    btn_search = Button(fenetre, text='Rechercher', width=10, command=rechercher)
    btn_search.place(x=870, y=5)

    # bouton pour afficher tous les informations
    btn_info = Button(fenetre, text='Afficher tous', width=10, command=show_students)
    btn_info.place(x=960, y=5)

    # tableau
    colonnes = ('id', 'nom', 'postnom', 'prenom', 'sexe', 'classe', 'option', 'date_inscription', 'nom_tut', 'num_tut', 'montant', 'dat_paye', 'code_recu')
    tree = ttk.Treeview(fenetre, columns=colonnes, show='headings', xscrollcommand=scrollX.set, yscrollcommand=scrollY.set)
    scrollX.pack(side=BOTTOM, fill=X)
    scrollY.pack(side=RIGHT, fill=Y)
    tree.column("#0", width=0, stretch=NO)
    tree.column('id', width=50)
    tree.column("nom", width=100)
    tree.column("postnom", width=100)
    tree.column("prenom", width=100)
    tree.column("sexe", width=35)
    tree.column("classe", width=43)
    tree.column("option", width=130)
    tree.column("date_inscription", width=105)
    tree.column("nom_tut", width=100)
    tree.column("num_tut", width=100)
    tree.column("montant", width=100)
    tree.column("dat_paye", width=100)
    tree.column("code_recu", width=100)

    tree.heading('id', text='Id')
    tree.heading('nom', text='Nom')
    tree.heading('postnom', text='Post-Nom')
    tree.heading('prenom', text='Prénom')
    tree.heading('sexe', text='Sexe')
    tree.heading('classe', text='Classe')
    tree.heading('option', text='Option')
    tree.heading('date_inscription', text="Date d'inscription")
    tree.heading('nom_tut', text='Nom Tuteur')
    tree.heading('num_tut', text='Numéro Tuteur')
    tree.heading('montant', text='Montant Payé')
    tree.heading('dat_paye', text='Date de Paye')
    tree.heading('code_recu', text='N° Reçu')
    tree.place(x=20, y=40, height=500)

    tree.bind("<ButtonRelease-1>", get_information)

    # bouton terminer
    terminer = Button(fenetre, text='Terminer', command=fenetre.destroy, width=20)
    terminer.place(x=500, y=550)

    for el in tree.get_children():
            tree.delete(el)
    
    for eleve in affiche_eleves():
        tree.insert('', END, values=(eleve))


def get_information(ev):
    ligne_focus = tree.focus()
    contenus = tree.item(ligne_focus)
    row = contenus["values"]
    nom.set(row[1]),
    postnom.set(row[2]),
    prenom.set(row[3]),
    sexe.set(row[4]),
    classe.set(row[5]),
    option.set(row[6]),
    date_inscription.set(row[7]),
    nom_tut.set(row[8]),
    num_tut.set(row[9]),
    ident.set(row[0])


def creer_compte():
    global entre_nom, entre_pass, sexe, fen 
    fen = Toplevel()
    fen.title("S'inscrire")
    fen.geometry("880x460+240+140")
    fen.config(background="#fff")
    fen.resizable(0, 0)
    canavas = Canvas(fen, width=412, height=460, bd=0, bg="#0077FC")
    canavas.place(x=-2, y=0)

    titre_can = Label(canavas, text="Institut Technique et Professionel", font=("ms reference sans serif", 14, "bold"), bg="#0077FC", fg="white")
    titre_can.place(x=28, y=10)

    titre1_can = Label(canavas, text="Bonjour,", font=("century shoolbook", 20), bg="#0077FC", fg="white")
    titre1_can.place(x=60, y=90)

    titre2_can = Label(canavas, text="Bienvenu!", font=("ms reference sans serif", 20, "bold"), bg="#0077FC", fg="white")
    titre2_can.place(x=60, y=128)    

    titre3_can = Label(canavas, text="""Ceci est la page pour la création d'un compte administrateur.\n
    La personne qui crééra ce compte sera chargée d'inscrire les élèves.""", font=("ms reference sans serif", 8), bg="#0077FC", fg="white")
    titre3_can.place(x=-5, y=240)

    titre4_can = Label(canavas, text="Créé par Josué Luis Panzu", font=("ms reference sans serif", 8, "bold"), bg="#0077FC", fg="white")
    titre4_can.place(x=5, y=328)

    annee = datetime.now()
    titre5_can = Label(canavas, text=f"{annee.year} Walborn. Tout droits reservés. Inc.", font=("ms reference sans serif", 8, "bold"), bg="#0077FC", fg="white")
    titre5_can.place(x=50, y=380)

    image = Image.open("logo/logo2.png")
    photo = ImageTk.PhotoImage(image, master=fen)
    canvas3 = Canvas(canavas, width=image.size[0], height=image.size[1], bg="#0077FC")
    logo = canvas3.create_image(62,62, image=photo)
    canvas3.place(x=220, y=70)

    canavas2 = Canvas(fen, width=800, height=460, bg="#fff", bd=0)
    canavas2.place(x=410, y=-2)

    titre = Label(canavas2, text="Création du compte", font=("ms reference sans serif", 20, "bold"), bg="#fff", fg="#333")
    titre.place(x=90, y=10)
    
    lab1 = Label(canavas2, text="Nom d'utilisateur:", font=("ms reference sans serif", 14,), bg="#fff", fg="#333")
    lab1.place(x=10, y=100)
    entre_nom = Entry(canavas2, bg="#DEDEDE", bd=1, font=("ms reference sans serif", 12))
    entre_nom.place(x=198, y=102, width=240, height=28)

    lab2 = Label(canavas2, text="Mot de passe:", font=("ms reference sans serif", 14,), bg="#fff", fg="#333")
    lab2.place(x=10, y=143)
    entre_pass = Entry(canavas2, bg="#DEDEDE", bd=1, font=("ms reference sans serif", 12), show="*")
    entre_pass.place(x=198, y=145, width=240, height=28)

    #bouton d'inscription
    btn_inscription = Button(canavas2, text="Créer le compte", bg="#0077FC", fg="#fff", bd=0, command=inscription, font=("ms reference sans serif", 11))
    btn_inscription.place(x=120 , y=370, width=228, height=33)

    fen.mainloop()


root = Tk()
root.title("Authentification")
root.geometry("540x410+380+160")
root.resizable(False, False)
root.config(background="#fff")

lable_principal = Label(root, text="S'identifier ici", fg="#5053E2", bg="#333", font=("arial", 18, "bold"))
lable_principal.place(x=0, y=0, width=540, height=90)

# LABEL POUR LE NOM D'UTILISATEUR
label1 = Label(root, text="Nom d'utilisateur", font=("ms reference sans serif", 14), bg='#fff')
label1.place(x=200, y=140)
user_entry = Entry(root, bg="#DEDEDE", bd=1, font=("ms reference sans serif", 12))
user_entry.place(x=165, y=180, width=240, height=28)

# LABEL POUR LE MOT DE PASSE
label2 = Label(root, text="Mot de passe", font=("ms reference sans serif", 14), bg='#fff')
label2.place(x=220, y=220)
pass_entry = Entry(root, bg="#DEDEDE", bd=1, font=("ms reference sans serif", 12), show="*")
pass_entry.place(x=165, y=250, width=240, height=28)

# Bouton se connecter
btn1 = Button(root, text="Se connecter", bg="#37399D", fg="#fff", bd=0, command=authentification, font=("ms reference sans serif", 11))
btn1.place(x=310 , y=315, width=138, height=33)

# Bouton créer un compte
btn2 = Button(root, text="Créer un compte", bg="#37399D", fg="#fff", bd=0, command=creer_compte, font=("ms reference sans serif", 11))
btn2.place(x=130 , y=315, width=138, height=33)

root.mainloop()
