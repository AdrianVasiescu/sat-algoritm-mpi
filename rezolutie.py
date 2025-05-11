import time

def rezolutie(formula):
    start_time = time.time() 


    while True:
        for i in range(len(formula)):
            for j in range(i + 1, len(formula)):
                for literal in formula[i]:
                    if -literal in formula[j]:
                        new_clause = list(set(formula[i]) | set(formula[j]))
                        new_clause.remove(literal)
                        new_clause.remove(-literal)

                        if not new_clause:
                            end_time = time.time()  
                            print(f"Rezoluție terminată în {end_time - start_time:.6f} secunde")
                            return False
                        
                        formula.append(new_clause)
                        formula[i] = []  
                        formula[j] = []  
                        break
        if all(len(clauza) == 0 for clauza in formula):  
            end_time = time.time()  
            print(f"Rezoluție terminată în {end_time - start_time:.6f} secunde")
            return True
