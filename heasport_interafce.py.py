import random
import time


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


def construire_max_heap(tab):
    n = len(tab)
    for i in range(n // 2 - 1, -1, -1):
        heapify(tab, n, i)


def heap_sort(tab):
    n = len(tab)

    construire_max_heap(tab)

    for fin in range(n - 1, 0, -1):
        tab[0], tab[fin] = tab[fin], tab[0]
        heapify(tab, fin, 0)


def afficher_tableau(tab, titre=""):
    if titre:
        print(f"{titre} : ", end="")
    if len(tab) == 0:
        print("(tableau vide)")
    else:
        print(" ".join(str(x) for x in tab))


def ligne(titre=""):
    largeur = 55
    if titre:
        print(f"\n{' ' + titre + ' ':=^{largeur}}")
    else:
        print("=" * largeur)


def saisir_tableau():
    while True:
        saisie = input("Entrez les nombres séparés par des espaces "
                        "(ex: 12 5 8 20 3 15 7) : ").strip()
        if saisie == "":
            return []
        try:
            return [int(x) for x in saisie.split()]
        except ValueError:
            print("  -> Entrée invalide, merci de ne saisir que des entiers.\n")


def generer_tableau_aleatoire():
    try:
        n = int(input("Taille du tableau à générer (défaut 10) : ") or 10)
        borne_min = int(input("Valeur minimale (défaut 0) : ") or 0)
        borne_max = int(input("Valeur maximale (défaut 100) : ") or 100)
    except ValueError:
        print("  -> Valeurs invalides, utilisation des valeurs par défaut (10, 0, 100).")
        n, borne_min, borne_max = 10, 0, 100

    return [random.randint(borne_min, borne_max) for _ in range(n)]


def trier_et_afficher(tab):
    afficher_tableau(tab, "Tableau initial")

    copie = tab.copy()
    debut = time.perf_counter()
    heap_sort(copie)
    fin = time.perf_counter()

    afficher_tableau(copie, "Tableau trié")
    print(f"Temps d'exécution : {(fin - debut) * 1000:.4f} ms "
          f"(n = {len(tab)}, complexité théorique O(n log n))")


def demo_construction_max_heap(tab):
    tab = tab.copy()
    n = len(tab)

    if n == 0:
        print("Tableau vide, rien à construire.")
        return

    afficher_tableau(tab, "Tableau de départ")
    print("\nConstruction du Max-Heap (on part du dernier nœud interne "
          f"= indice {n // 2 - 1}, jusqu'à la racine) :\n")

    for i in range(n // 2 - 1, -1, -1):
        heapify(tab, n, i)
        afficher_tableau(tab, f"  Après heapify(tab, n, i={i})")

    print("\nMax-Heap final :")
    afficher_tableau(tab)


def lancer_tests():
    tests = [
        ("Normal",       [12, 5, 8, 20, 3, 15, 7], [3, 5, 7, 8, 12, 15, 20]),
        ("Déjà trié",    [1, 2, 3, 4, 5],           [1, 2, 3, 4, 5]),
        ("Inversé",      [5, 4, 3, 2, 1],           [1, 2, 3, 4, 5]),
        ("Doublons",     [4, 2, 4, 1, 2],           [1, 2, 2, 4, 4]),
        ("Un élément",   [9],                       [9]),
        ("Vide",         [],                        []),
    ]

    ligne("RÉSULTATS DES TESTS")
    tous_ok = True
    for nom, entree, attendu in tests:
        tab = entree.copy()
        heap_sort(tab)
        ok = (tab == attendu)
        tous_ok &= ok
        statut = "OK" if ok else "ÉCHEC"
        print(f"[{statut:5}] {nom:12} entrée={entree} -> obtenu={tab} (attendu={attendu})")

    print()
    if tous_ok:
        print("Tous les tests sont réussis.")
    else:
        print("Au moins un test a échoué, vérifier l'implémentation.")


def afficher_menu():
    ligne("TRI PAR TAS (HEAPSORT) - MENU PRINCIPAL")
    print("1. Saisir un tableau et le trier")
    print("2. Générer un tableau aléatoire et le trier")
    print("3. Visualiser étape par étape la construction du Max-Heap")
    print("4. Lancer les tests automatiques (section 9 du cahier des charges)")
    print("5. Afficher la complexité de l'algorithme")
    print("0. Quitter")


def afficher_complexite():
    ligne("COMPLEXITÉ")
    print("Construction du Max-Heap : O(n)")
    print("Tri complet (Heapsort)   : O(n log n)")
    print("Espace supplémentaire   : O(1) (tri en place, hors variables locales)")


def menu():
    print("===== TRI PAR TAS (HEAPSORT) =====")
    print("Sujet 5 - Projet Algo Avancé - Démonstration")

    while True:
        afficher_menu()
        choix = input("\nVotre choix : ").strip()

        if choix == "1":
            tab = saisir_tableau()
            ligne("TRI D'UN TABLEAU SAISI")
            trier_et_afficher(tab)

        elif choix == "2":
            tab = generer_tableau_aleatoire()
            ligne("TRI D'UN TABLEAU ALÉATOIRE")
            trier_et_afficher(tab)

        elif choix == "3":
            tab = saisir_tableau()
            if not tab:
                tab = [12, 5, 8, 20, 3, 15, 7]
                print(f"(Aucune saisie, utilisation de l'exemple {tab})")
            ligne("CONSTRUCTION DU MAX-HEAP - ÉTAPE PAR ÉTAPE")
            demo_construction_max_heap(tab)

        elif choix == "4":
            lancer_tests()

        elif choix == "5":
            afficher_complexite()

        elif choix == "0":
            print("\nFin du programme. Merci !")
            break

        else:
            print("\nChoix invalide, veuillez réessayer.")

        input("\nAppuyez sur Entrée pour continuer...")


if __name__ == "__main__":
    menu()
