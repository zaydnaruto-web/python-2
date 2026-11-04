note = float(input("Entrez une note : "))

if 0 <= note <= 20:
    print("La note est valide et appartient à l'intervalle [0, 20].")
else:
    print("Erreur : la note n'appartient pas à l'intervalle [0, 20].")