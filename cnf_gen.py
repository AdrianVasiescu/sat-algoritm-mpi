import random

def generate_cnf(num_vars, num_clauses, filename):
    with open(filename, 'w') as f:
        f.write(f"p cnf {num_vars} {num_clauses}\n")
        
        for _ in range(num_clauses):
            clause = []
            for _ in range(num_vars):
                var = random.randint(1, num_vars)
                if random.choice([True, False]):
                    clause.append(f"{var}")
                else:
                    clause.append(f"-{var}")
            clause.append("0")  
            f.write(" ".join(clause) + "\n")

generate_cnf(3, 5, "test.cnf")
