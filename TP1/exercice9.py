def analyse_texte(texte):
    mots = texte.split()
    nb_mots = 0
    for mot in mots:
        nb_mots += 1
    
    nb_caracteres = 0
    for caractere in texte:
        nb_caracteres += 1
    
    return {"mots": nb_mots, "caracteres": nb_caracteres}

print(analyse_texte("Bonjour tout le monde."))