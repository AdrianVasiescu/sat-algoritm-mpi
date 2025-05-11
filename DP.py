import time

def dp_solve(formula):
    start_time = time.time()  

    if len(formula) == 0:
        end_time = time.time()  
        print(f"Rezolvat în {end_time - start_time:.6f} secunde")
        return True

    if any(len(clauza) == 0 for clauza in formula):
        end_time = time.time() 
        print(f"Rezolvat în {end_time - start_time:.6f} secunde")
        return False

    var = formula[0][0]
    formula_copy = [clauza for clauza in formula if var not in clauza]
    if dp_solve(formula_copy):
        return True

    return dp_solve([clauza for clauza in formula if -var not in clauza])
