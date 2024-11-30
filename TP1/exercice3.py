def intersection(ensemble1, ensemble2):
    resultat = set()
    for element in ensemble1:
        if element in ensemble2:
            resultat.add(element)
    return resultat

print(intersection({1, 2, 3}, {2, 3, 4})) 