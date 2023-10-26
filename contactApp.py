
import tkinter as tk
from tkinter import *
import json
import tkinter.messagebox

window = tk.Tk()

#PAGES
pageAcceuil = Frame(window)
pageAjoutContact = Frame(window)
pageDetailContact = Frame(window)

pageAcceuil.grid(row=0, column=0, sticky="nsew")
pageAjoutContact.grid(row=0, column=0, sticky="nsew")
pageDetailContact.grid(row=0, column=0, sticky="nsew")

#Design
font_B = ("Helvetica", 12)
paddings = {'padx': 5, 'pady': 5}

contacts = []

#functions

def modifyJsonFile():
    with open("allContact.json", "w") as file:
        json.dump(contacts,file, indent=4)
    updateContactList()

#---------------------------- ACCUEIL / ALL CONTACT -------------------------

pageAccueilTitle = tk.Label(pageAcceuil, text="Tous les contacts")
pageAccueilTitle.grid(row=0, column=0)
pageAddContactBTN = tk.Button(pageAcceuil, text="Ajouter un contact", command=lambda: pageAjoutContact.tkraise())
pageAddContactBTN.grid(row=0, column=1)

def updateContactList():
    global contacts
    with open("allContact.json", "r") as json_file:
        contacts = json.load(json_file)

    for contact in contacts :
        conctButton = tk.Button(pageAcceuil, text=f"{contact['nom']}", command=lambda contactDetails=contact: showContactDetails(contactDetails), font=font_B)
        conctButton.grid(row=f"{contact['id']}", column=0, **paddings)

updateContactList()


#----------------------------- ADD CONTACT PAGE --------------------

def ajouterContact():
    if(len(pageAjoutContactNameE.get()) > 0 and len(pageAjoutContactPrenomE.get()) > 0 and len(pageAjoutContactAdressE.get()) > 0 and len(pageAjoutContactTelE.get()) > 0):
        if(pageAjoutContactTelE.get().isdigit()):
            contact = {
                "id": len(contacts) + 1,
                "nom": pageAjoutContactNameE.get(),
                "prenom": pageAjoutContactPrenomE.get(),
                "adresse": pageAjoutContactAdressE.get(),
                "numero_de_telephone": pageAjoutContactTelE.get()
            }
            contacts.append(contact)
            modifyJsonFile()
            tkinter.messagebox.showinfo("Contact ajouté", f"Le Contact :[{pageAjoutContactPrenomE.get()}] est ajouté")
        else:
            tkinter.messagebox.showwarning("Warning Contact", f"Le champ tel ne doit contenir que des chiffre et pas de lettres")
    else:
            tkinter.messagebox.showwarning("Warning Contact", f"Tous les champs doivent être remplis")
        
    

#HEADER
pageAjoutContactTitle = tk.Label(pageAjoutContact, text="Ajouter un contact")
pageAjoutContactTitle.grid(row=0, column=0, **paddings)
pageAcceuilBTN = tk.Button(pageAjoutContact, text="Tous les contacts", command=lambda: pageAcceuil.tkraise())
pageAcceuilBTN.grid(row=0, column=1,**paddings)

#NOM
pageAjoutContactNameE = tk.Entry(pageAjoutContact)
pageAjoutContactNameL = tk.Label(pageAjoutContact, text="Nom : ")
pageAjoutContactNameL.grid(row=1,column=0, **paddings)
pageAjoutContactNameE.grid(row=1,column=1, **paddings)

#PRENOM
pageAjoutContactPrenomE = tk.Entry(pageAjoutContact)
pageAjoutContactPrenomL = tk.Label(pageAjoutContact, text="Prenom : ")
pageAjoutContactPrenomL.grid(row=2,column=0, **paddings)
pageAjoutContactPrenomE.grid(row=2,column=1, **paddings)

#ADRESS
pageAjoutContactAdressE = tk.Entry(pageAjoutContact)
pageAjoutContactAdressL = tk.Label(pageAjoutContact, text="Adress : ")
pageAjoutContactAdressL.grid(row=3,column=0, **paddings)
pageAjoutContactAdressE.grid(row=3,column=1, **paddings)

#TEL
pageAjoutContactTelE = tk.Entry(pageAjoutContact)
pageAjoutContactTelL = tk.Label(pageAjoutContact, text="Tel : ")
pageAjoutContactTelL.grid(row=4,column=0, **paddings)
pageAjoutContactTelE.grid(row=4,column=1, **paddings)

#AJOUT
pageAjoutContactAjouter = tk.Button(pageAjoutContact, text="Ajouter", command=ajouterContact)
pageAjoutContactAjouter.grid(row=5,column=0, **paddings)


#------------------------ CONTACT DETAILS -------------

    

def showContactDetails(contactDetails):

    def suppContact():
        for contact in contacts:
            if contact["id"] == contactDetails["id"]:
                contacts.pop(contactDetails["id"] - 1)
                modifyJsonFile()
                updateContactList()
                tkinter.messagebox.showinfo("Contact Supprimé", "Le Contact est Supprimé")
                pageAcceuil.tkraise()
                 


    def modifierContact(): 
        for contact in contacts:
            if contact["id"] == contactDetails["id"]:
                contact["nom"] = pageDetailContactNameE.get() if len(pageDetailContactNameE.get()) > 0 else contactDetails["nom"]
                contact["prenom"] = pageDetailContactPrenomE.get() if len(pageDetailContactPrenomE.get()) > 0 else contactDetails["prenom"]
                contact["adresse"] = pageDetailContactAdressE.get() if len(pageDetailContactAdressE.get()) > 0 else contactDetails["adresse"]
                contact["numero_de_telephone"] = pageDetailContactTelE.get() if len(pageDetailContactTelE.get()) > 0 else contactDetails["numero_de_telephone"] 
                break
        modifyJsonFile()
        updateContactList()
        tkinter.messagebox.showinfo("Contact Modifié", "Le Contact est modifié")
        pageAcceuil.tkraise()
         
    



    #header
    pageDetailContact.tkraise()
    pageDetailContactTitle = tk.Label(pageDetailContact, text="Details du contact")
    pageDetailContactTitle.grid(row=0, column=0, **paddings)
    pageAcceuilBTN = tk.Button(pageDetailContact, text="Tous les contacts", command=lambda: pageAcceuil.tkraise())
    pageAcceuilBTN.grid(row=0, column=1,**paddings)

    # NOM
    pageDetailContactNameL = tk.Label(pageDetailContact, text=f"Nom : {contactDetails['nom']} ")
    pageDetailContactNameL.grid(row=1,column=0, **paddings)
    pageDetailContactNameE = tk.Entry(pageDetailContact)
    pageDetailContactNameE.grid(row=1, column=1)

    # PRENOM
    pageDetailContactPrenomL = tk.Label(pageDetailContact, text=f"Prenom : {contactDetails['prenom']} ")
    pageDetailContactPrenomL.grid(row=2,column=0, **paddings)
    pageDetailContactPrenomE = tk.Entry(pageDetailContact)
    pageDetailContactPrenomE.grid(row=2, column=1)
    
    # ADRESS
    pageDetailContactAdressL = tk.Label(pageDetailContact, text=f"Adress : {contactDetails['adresse']} ")
    pageDetailContactAdressL.grid(row=3,column=0, **paddings)
    pageDetailContactAdressE = tk.Entry(pageDetailContact)
    pageDetailContactAdressE.grid(row=3, column=1)
    
    # TEL
    pageDetailContactTelL = tk.Label(pageDetailContact, text=f"Tel : {contactDetails['numero_de_telephone']} ")
    pageDetailContactTelL.grid(row=4,column=0, **paddings)
    pageDetailContactTelE = tk.Entry(pageDetailContact)
    pageDetailContactTelE.grid(row=4, column=1)

    # MODIFIER
    pageDetailContactModifier = tk.Button(pageDetailContact, text="Modifier", command=modifierContact)
    pageDetailContactModifier.grid(row=5,column=1, **paddings)

    #SUPP
    pageDetailContactSupp = tk.Button(pageDetailContact, text="Supprimer", command=suppContact,fg="red")
    pageDetailContactSupp.grid(row=5,column=0, **paddings)


# First Page 
pageAcceuil.tkraise()
# WINDOW
window.title("Contact App")
window.geometry("500x500")
window.mainloop()

