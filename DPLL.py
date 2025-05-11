def dpll(formula):
    if len(formula) == 0:
        return True  
    if any(len(clauza) == 0 for clauza in formula):
        return False  

    unit_clause = [clauza for clauza in formula if len(clauza) == 1]
    if unit_clause:
        return dpll(propagare_unitara(formula, unit_clause[0]))

    var = formula[0][0]
    return dpll(propagare_unitara(formula, var)) or dpll(propagare_unitara(formula, -var))

def propagare_unitara(formula, unit):
    return [clauza for clauza in formula if unit not in clauza]
