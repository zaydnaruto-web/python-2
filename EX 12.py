import math

print("--- Résolution de axssssbx + c = 0 ---")

# Utilisation de float pour accepter aussi les nombres décimaux
a = float(input("Entrer la valeur de a : "))
b = float(input("Entrer la valeur de b : "))
c = float(input("Entrer la valeur de c : "))

# Calcul du discriminant (Delta)
D = b**2 - 4 * a * c

# Cas 1 : Delta égal à 0 (une solution double)
if D == 0:
    x = -b / (2 * a)
    print(f"La valeur unique de x est : {x:.2f}")

# Cas 2 : Delta négatif (pas de solution réelle)
elif D < 0:
    print("Le discriminant est négatif (D < 0) : il n'y a pas de solutions réelles.")

# Cas 3 : Delta positif (deux solutions distinctes)
else:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)
    print("Les solutions sont :")
    print(f"x1 = {x1:.2f}")
    print(f"x2 = {x2:.2f}")