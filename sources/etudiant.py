# Programme Python - Gestion des étudiants

# Définition d'une classe Etudiant
class Etudiant:
    def __init__(self, nom, age, matricule):
        self.nom = nom
        self.age = age
        self.matricule = matricule

# Étape 1 : Initialisation de la liste des étudiants
liste_etudiants = []

# Étape 2 : Fonction pour ajouter un étudiant
def ajouter_etudiant(nom, age, matricule):
    etudiant = Etudiant(nom, age, matricule)
    liste_etudiants.append(etudiant)
    print(f"{nom} a été ajouté à la liste des étudiants MP2L 2 / ahlem gammoudi.")

# Étape 3 : Fonction pour rechercher un étudiant par nom
def rechercher_etudiant_par_nom(nom):
    for etudiant in liste_etudiants:
        if etudiant.nom.lower() == nom.lower():
            return etudiant
    return None

# Étape 4 : Fonction pour afficher la liste complète des étudiants
def afficher_liste_etudiants():
    print("Liste des étudiants en MP2L /ahlem :")
    for etudiant in liste_etudiants:
        print(f"Nom: {etudiant.nom}, Age: {etudiant.age}, Matricule: {etudiant.matricule}")

# Étape 5 : Ajout de quelques étudiants à la liste
ajouter_etudiant("Ahlem", 28, "A123")
ajouter_etudiant("Asma", 27, "B456")
ajouter_etudiant("Abir", 26, "C789")

# Étape 6 : Recherche d'un étudiant par nom
etudiant_recherche = rechercher_etudiant_par_nom("Ahlem gammoudi")
if etudiant_recherche:
    print(f"Étudiant trouvé - Nom: {etudiant_recherche.nom}, Age: {etudiant_recherche.age}, Matricule: {etudiant_recherche.matricule}")
else:
    print("Aucun étudiant trouvé avec ce nom mp2l.")

# Étape 7 : Affichage de la liste complète des étudiants
afficher_liste_etudiants()
