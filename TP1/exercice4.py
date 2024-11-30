def compte_occurences(liste):
    dictionnaire = {}
    for mot in liste:
        if mot in dictionnaire:
            dictionnaire[mot] += 1
        else:
            dictionnaire[mot] = 1
    return dictionnaire


print(compte_occurences(["pomme", "orange", "pomme", "banane"])) 
