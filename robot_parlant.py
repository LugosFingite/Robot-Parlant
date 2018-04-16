from table import *

def suivant(table_lettres):
    """prends table_lettres en paramètres, une liste de chaines
renvoie True si la lettre à analyser est suivi par une des lettre de chaque chaine de la liste
ex : suivi(["abc","def"]) renvoie True si la lettre actuelement analysée
est suivie de a,b ou c puis de d,e ou f"""
    for increment,lettres in enumerate(table_lettres):
        position = indice+increment+1
        if position < 0 or position >= len(phrase):
            continue
        if (not phrase[position] in lettres):
            return False
    return True

def precedent(table_lettres):
    """comme suivant mais pour les lettres avant"""
    for increment,lettres in enumerate(table_lettres):
        position = indice-increment-1
        if position < 0 or position >= len(phrase):
            continue
        if (not phrase[position] in lettres):
            return False
    return True

def transcrire(indice):
    """Converti un son en lettre"""
    if phrase[indice]==phrase[indice-1]:
        return ("",1)
    try:
        convert = table_conversion[phrase[indice]]
    except KeyError:
        convert = phrase[indice],1
    if not isinstance(convert,tuple): #si il existe plusieurs cas spéciaux, on les teste
        for condition,resultat in convert[:len(convert)-1:1]:
            if eval(condition):
                if debug:
                    print(condition,end=": ")
                return resultat
        return convert[-1]
    return convert

def convertir(phrase):
    """Converti une phrase de texte en son"""
    global indice
    phrase_convertie = []
    while indice < len(phrase):
        if debug:
            print("[{}] '{}' ->  ".format(indice,phrase[indice]),end="")
        son,increment = transcrire(indice)
        phrase_convertie.append(son)
        if debug:
            print("'{}' +{}".format(son,increment))
        indice += increment
    return "".join(phrase_convertie)

debug = input("Debug ?").lower()
if debug in ["yes","oui","vrai","true","activer","actif"]:
    debug = True
else:
    debug = False
while True:
    indice = 0
    entre = input("Entrez une phrase à prononcer : ")
    phrase = " " + entre.lower() + " "
    phrase_sonore = convertir(phrase)
    print(phrase_sonore)
