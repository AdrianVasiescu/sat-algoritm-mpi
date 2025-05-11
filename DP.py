def dp_solve(formula):
    if len(formula) == 0:
        return True  
    if any(len(clauza) == 0 for clauza in formula):
        return False  

    var = formula[0][0]
    formula_copy = [clauza for clauza in formula if var not in clauza]
    if dp_solve(formula_copy):
        return True
    return dp_solve([clauza for clauza in formula if -var not in clauza])

