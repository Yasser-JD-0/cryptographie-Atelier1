from sympy import mod_inverse

# Saisie utilisateur
a = int(input("Entrez la valeur de a : "))
m = int(input("Entrez la valeur de m : "))

try:
    # Avec SymPy
    inv_sympy = mod_inverse(a, m)
    print(f"[SymPy] L'inverse modulaire de {a} modulo {m} est : {inv_sympy}")

    # Avec pow (Python natif)
    inv_builtin = pow(a, -1, m)
    print(f"[Python pow()] L'inverse modulaire de {a} modulo {m} est : {inv_builtin}")

except ValueError:
    print(f"Aucun inverse modulaire n'existe pour a = {a} et m = {m}.")
1