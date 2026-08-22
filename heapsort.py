"""
PROJET ALGO AVANCÉ - Sujet 5 : Tri par Tas (Heapsort)
Implémentation complète en Python (sans heapq ni sorted())
"""


def heapify(tab, n, i):
    """
    Rétablit la propriété de Max-Heap
    pour le sous-arbre dont la racine est i.
    n = taille actuelle du tas.
    """
    plus_grand = i
    gauche = 2 * i + 1
    droite = 2 * i + 2

    # Comparer avec le fils gauche
    if gauche < n and tab[gauche] > tab[plus_grand]:
        plus_grand = gauche

    # Comparer avec le fils droit
    if droite < n and tab[droite] > tab[plus_grand]:
        plus_grand = droite

    # Si le plus grand n'est pas la racine
    if plus_grand != i:
        tab[i], tab[plus_grand] = tab[plus_grand], tab[i]
        # Continuer la réorganisation
        heapify(tab, n, plus_grand)


def construire_max_heap(tab):
    """Construit un Max-Heap dans le tableau."""
    n = len(tab)
    # Les feuilles sont déjà des tas.
    # On commence au dernier nœud qui possède un enfant.
    for i in range(n // 2 - 1, -1, -1):
        heapify(tab, n, i)


def heap_sort(tab):
    """Trie le tableau dans l'ordre croissant avec Heapsort."""
    n = len(tab)

    # Étape 1 : construire le Max-Heap
    construire_max_heap(tab)

    # Étape 2 : déplacer le maximum à la fin
    for fin in range(n - 1, 0, -1):
        tab[0], tab[fin] = tab[fin], tab[0]
        # Réparer le tas restant
        heapify(tab, fin, 0)


def afficher_tableau(tab):
    print(" ".join(str(x) for x in tab))


def main():
    print("===== TRI PAR TAS (HEAPSORT) =====")

    # Exemple de tableau
    tab = [12, 5, 8, 20, 3, 15, 7]
    print("\nTableau initial :")
    afficher_tableau(tab)

    construire_max_heap(tab)
    print("\nAprès construction du Max-Heap :")
    afficher_tableau(tab)

    # Pour montrer le tri, on repart du tableau initial.
    tab = [12, 5, 8, 20, 3, 15, 7]
    heap_sort(tab)
    print("\nTableau trié :")
    afficher_tableau(tab)


if __name__ == "__main__":
    main()
