# create the variables
horaire = ""
salaire_annuel = ""

while salaire_annuel == "":
    salaire_annuel = input("Quel est votre salaire annuel ? ")
    try :
        int(salaire_annuel)
    except :
        salaire_annuel = ""

while horaire == "":
    horaire = input("Combien d'heures travaillez-vous par semaine ? ")
    try :
        int(horaire)
    except :
        horaire = ""

def salaire_mensuel(salaire_annuel) :
    """This function is so divides the 'salaire_annuel' variable by 12"""
    valeur1 = int(salaire_annuel)/12
    return(valeur1)


def salaire_hebdomadaire(salaire_mensuel) :
    """This function divides the 'salaire_mensuel' by 4"""
    valeur2 = int(salaire_mensuel)/4
    return(valeur2)

salaire_mensuel_val = salaire_mensuel(int(salaire_annuel))

salaire_hebdomadaire_val = salaire_hebdomadaire(int(salaire_mensuel_val))

def salaire_horaire(salaire_hebdomadaire, heures_travaillees):
    valeur3 = float(salaire_hebdomadaire)/float(heures_travaillees)
    return(valeur3)


reponse = salaire_horaire(salaire_hebdomadaire_val, int(horaire))

mode = "horaire"

print("Votre salaire " + mode + " est de "+str(reponse)+ " euros.")