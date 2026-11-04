
jour = int(input("Entrez un entier entre 0 et 6 : "))
jours = ["Dimanche", "Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi"]

if 0 <= jour <= 6:
    print("Le jour correspondant est :", jours[jour])
else:
    print("Erreur : la valeur est en dehors de l'intervalle [0, 6].")