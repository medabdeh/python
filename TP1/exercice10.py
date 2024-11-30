def fusionner_dicts(dict1, dict2):
    resultat = {}
    for cle in dict1:
        resultat[cle] = dict1[cle]
    for cle in dict2:
        if cle in resultat:
            resultat[cle] += dict2[cle]
        else:
            resultat[cle] = dict2[cle]
    return resultat

dict1 = {"a": 1, "b": 2}
dict2 = {"b": 3, "c": 4}
print(fusionner_dicts(dict1, dict2))  