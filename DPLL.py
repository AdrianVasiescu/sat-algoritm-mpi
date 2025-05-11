import time

def dpll(formula):
    start_time = time.time()  


    def dpll_recursive(formula):
        if len(formula) == 0:
            return True  
        if any(len(clauza) == 0 for clauza in formula):
            return False 

        var = formula[0][0]


        formula_copy = [clauza for clauza in formula if var not in clauza]
        if dpll_recursive(formula_copy):
            return True
        return dpll_recursive([clauza for clauza in formula if -var not in clauza])

    result = dpll_recursive(formula)

    end_time = time.time()  
    print(f"DPLL terminat în {end_time - start_time:.6f} secunde")
    return result
