def rezolva(formula):
    while True:
        for clauza1 in formula:
            for clauza2 in formula:
                rezultat = rezolva_clauze(clauza1, clauza2)
                if rezultat:
                    formula.add(rezultat)
                    if [] in formula:
                        return False  
        break
    return True  

def rezolva_clauze(clauza1, clauza2):
    for litera in clauza1:
        if -litera in clauza2:
            return list(set(clauza1 + clauza2) - {litera, -litera})
    return None
