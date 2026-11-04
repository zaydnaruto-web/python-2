nom1 = input("Nom de la personne 1 : ")
age1 = int(input("Âge de la personne 1 : "))

nom2 = input("Nom de la personne 2 : ")
age2 = int(input("Âge de la personne 2 : "))

nom3 = input("Nom de la personne 3 : ")
age3 = int(input("Âge de la personne 3 : "))

plus_age = nom1
max_age = age1

if age2 > max_age:
    max_age = age2
    plus_age = nom2

if age3 > max_age:
    max_age = age3
    plus_age = nom3

print("La personne la plus âgée est :", plus_age)