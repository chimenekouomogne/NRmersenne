def mersenne_number(p):
    return 2**p - 1


def is_prime(nbr):
    if nbr <= 1 :
        return False
    for i in range(2 , nbr//2 + 1):
        if nbr % i == 0:
            return False
    return True



def mersennes(n_begin, n_end):
    liste_1 = [ nbre  for nbre in range(n_begin, n_end) if is_prime(nbre)]
    liste_2 = []
    for elt in liste_1:
        liste_2.append(mersenne_number(elt))
    return liste_2


print(mersennes(4, 15))

print(mersenne_number(17))

r=12
print('aire = ', r**2*3.14)
nom = "Sonia"
prenom = "soso"
