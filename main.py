"""
fichier 
"""

from math import sqrt

#### Fonction secondaire


def isprime(p):

    """
    retourne true si le nombre passé en argument est premier faux sinon

    args :
        p un entier
    returns :
        un booléen valant true si p est premier false sinon

    >>> fact(1)
    True

    """

    print(print.__doc__)
    if p in (0,1):
        return False
    if p == 2 :
        return True
    premier = True
    for d in range (2, int(sqrt(p) + 1)) :
        if p % d == 0 :
            premier = False
            break
    return premier


#### Fonction principale


def main():

    """
    main fonction
    """

    for n in range(100):
        if isprime(n):
            print(n, end=", ")

    print()


if __name__ == "__main__":
    main()
    help(isprime)
    help(main)
    print(print.__doc__)
