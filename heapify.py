def heapify(tab, n, i):
    plus_grand = i
    gauche = 2 * i + 1
    droite = 2 * i + 2
    
    if gauche < n and tab[gauche] > tab[plus_grand]:
        plus_grand = gauche
    
    if droite < n and tab[droite] > tab[plus_grand]:
        plus_grand = droite
    
    if plus_grand != i:
        tab[i], tab[plus_grand] = tab[plus_grand], tab[i]
        heapify(tab, n, plus_grand)
