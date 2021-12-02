def syracuse(n):
    liste_syracuse = [n]

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else:
            n = n * 3 + 1
        liste_syracuse.append(n)
    
    return liste_syracuse

variable = syracuse(3)
print(variable) 

# ce n'est pas la correction
def testeConjecture(n_max):
    for i in range(2, n_max):
        def syracuse(n):
            liste_syracuse = [n]

            while n != 1:
                if n % 2 == 0:
                    n = n // 2
                else:
                    n = n * 3 + 1
                liste_syracuse.append(n)
    
            return liste_syracuse

print(testeConjecture(100))










