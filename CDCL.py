import time

def cdcl(formula):
    start_time = time.time()  


    def cdcl_recursive(formula):
        if len(formula) == 0:
            return True  
        if any(len(clauza) == 0 for clauza in formula):
            return False  
        
       
        var = formula[0][0]
        
       
        formula_copy = [clauza for clauza in formula if var not in clauza]
        if cdcl_recursive(formula_copy):
            return True

        
        return cdcl_recursive([clauza for clauza in formula if -var not in clauza])

    result = cdcl_recursive(formula)

    end_time = time.time()  
    print(f"CDCL terminat în {end_time - start_time:.6f} secunde")
    return result
