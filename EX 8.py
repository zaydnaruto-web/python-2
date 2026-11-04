max_val = int(input("Entrez un entier : "))
for _ in range(3):
    val = int(input("Entrez un entier : "))
    if val > max_val:
        max_val = val
print("Le plus grand entier est :", max_val)