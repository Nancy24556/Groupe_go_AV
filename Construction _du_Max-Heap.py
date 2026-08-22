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

    # Si le plus grand n'est pas la racine, on échange et on continue
    if plus_grand != i:
        tab[i], tab[plus_grand] = tab[plus_grand], tab[i]
        heapify(tab, n, plus_grand)


def construire_max_heap(tab):
    """
    Construit un Max-Heap à partir d'un tableau quelconque.
    On part du dernier nœud interne (qui a au moins un enfant)
    et on remonte jusqu'à la racine.
    """
    n = len(tab)
    dernier_noeud_interne = n // 2 - 1

    for i in range(dernier_noeud_interne, -1, -1):
        heapify(tab, n, i)