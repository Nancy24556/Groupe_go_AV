"""
PROJET ALGO AVANCÉ — Sujet 5 : Tri par Tas (Heapsort)
Langage : Python

Fichier unique regroupant le travail des 5 membres du groupe :
    - Membre 1 (Randrezamihamina Tinou Fitia) : Théorie et conception            (voir rapport / PDF du sujet)
    - Membre 2 (Nancy romus): Construction du Max-Heap          (heapify, construire_max_heap)
    - Membre 3 (Andry): Tests unitaires de heapify        (test_heapify_*)
    - Membre 4 (Andy Hifaliana): Heapsort                          (heap_sort) + tests (unittest + démo simple)
    - Membre 5 (Frederico Princy): Interface utilisateur, menu, démonstration, tests de bout en bout

Règle respectée : aucune bibliothèque de tas/tri prête à l'emploi
(pas de heapq, pas de sorted()) n'est utilisée. Tout est implémenté à la main.
"""

import random
import time
import unittest

def heapify(tab, n, i):
    """
    Rétablit la propriété de Max-Heap
    pour le sous-arbre dont la racine est i.
    n = taille actuelle du tas.
    """
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
    """
    Construit un Max-Heap à partir d'un tableau quelconque.
    On part du dernier nœud interne (qui a au moins un enfant)
    et on remonte jusqu'à la racine.
    """
    n = len(tab)
    dernier_noeud_interne = n // 2 - 1

    for i in range(dernier_noeud_interne, -1, -1):
        heapify(tab, n, i)



def heap_sort(tab):
    """Trie le tableau dans l'ordre croissant avec Heapsort."""
    n = len(tab)


    construire_max_heap(tab)

    for fin in range(n - 1, 0, -1):
        tab[0], tab[fin] = tab[fin], tab[0]
        heapify(tab, fin, 0)


def test_heapify_basic():
    tab = [5, 15, 10, 8, 3]
    heapify(tab, 5, 0)
    assert tab[0] >= tab[1] and tab[0] >= tab[2]
    print("✓ test_heapify_basic")


def test_heapify_avec_enfant_gauche():
    tab = [3, 15, 8]
    heapify(tab, 3, 0)
    assert tab[0] == 15
    print("✓ test_heapify_avec_enfant_gauche")


def test_heapify_avec_enfant_droit():
    tab = [3, 8, 15]
    heapify(tab, 3, 0)
    assert tab[0] == 15
    print("✓ test_heapify_avec_enfant_droit")


def test_heapify_feuille():
    tab = [10, 5, 8, 2, 1]
    heapify(tab, 5, 4)
    assert tab == [10, 5, 8, 2, 1]
    print("✓ test_heapify_feuille")


def test_heapify_already_heap():
    tab = [20, 15, 10, 5, 3]
    heapify(tab, 5, 0)
    assert tab[0] == 20
    print("✓ test_heapify_already_heap")


def test_heapify_doublons():
    tab = [5, 20, 20, 10, 3]
    heapify(tab, 5, 0)
    assert tab[0] == 20
    print("✓ test_heapify_doublons")


def test_heapify_arbre_complet():
    tab = [1, 10, 8, 5, 6, 3, 2]
    heapify(tab, 7, 0)
    assert tab[0] == 10
    print("✓ test_heapify_arbre_complet")


def test_heapify_un_element():
    tab = [5]
    heapify(tab, 1, 0)
    assert tab == [5]
    print("✓ test_heapify_un_element")


def test_heapify_negatifs():
    tab = [-5, 10, -10, 8, 3]
    heapify(tab, 5, 0)
    assert tab[0] == 10
    print("✓ test_heapify_negatifs")


def test_heapify_recursive():
    tab = [3, 20, 15, 10, 5, 8, 7]
    heapify(tab, 7, 0)
    assert tab[0] >= tab[1] and tab[0] >= tab[2]
    print("✓ test_heapify_recursive")


def lancer_tests_heapify():
    """Regroupe et exécute tous les tests unitaires de heapify (Membre 3)."""
    test_heapify_basic()
    test_heapify_avec_enfant_gauche()
    test_heapify_avec_enfant_droit()
    test_heapify_feuille()
    test_heapify_already_heap()
    test_heapify_doublons()
    test_heapify_arbre_complet()
    test_heapify_un_element()
    test_heapify_negatifs()
    test_heapify_recursive()
    print("\nTous les tests de heapify sont passés ✓")



def demo_tests_heapsort_simple():
    """
    Tests globaux simples (version originale du fichier headsort.py) :
    affiche le tableau avant/après tri pour les 6 cas du sujet.
    """
    tests = [
        [12, 5, 8, 20, 3, 15, 7],
        [1, 2, 3, 4, 5],          
        [5, 4, 3, 2, 1],        
        [4, 2, 4, 1, 2],         
        [9],                       
        []                   
    ]

    for t in tests:
        original = t.copy()
        heap_sort(t)
        print(f"Avant : {original}")
        print(f"Après : {t}")
        print()


def est_max_heap(tab):
    """Vérifie que tab respecte bien la propriété de Max-Heap."""
    n = len(tab)
    for i in range(n):
        gauche = 2 * i + 1
        droite = 2 * i + 2
        if gauche < n and tab[i] < tab[gauche]:
            return False
        if droite < n and tab[i] < tab[droite]:
            return False
    return True


class TestHeapify(unittest.TestCase):

    def test_construire_max_heap(self):
        tab = [12, 5, 8, 20, 3, 15, 7]
        construire_max_heap(tab)
        self.assertTrue(est_max_heap(tab))
        self.assertEqual(tab[0], max([12, 5, 8, 20, 3, 15, 7]))


class TestHeapSort(unittest.TestCase):

    def test_normal(self):
        tab = [12, 5, 8, 20, 3, 15, 7]
        heap_sort(tab)
        self.assertEqual(tab, [3, 5, 7, 8, 12, 15, 20])

    def test_deja_trie(self):
        tab = [1, 2, 3, 4, 5]
        heap_sort(tab)
        self.assertEqual(tab, [1, 2, 3, 4, 5])

    def test_inverse(self):
        tab = [5, 4, 3, 2, 1]
        heap_sort(tab)
        self.assertEqual(tab, [1, 2, 3, 4, 5])

    def test_doublons(self):
        tab = [4, 2, 4, 1, 2]
        heap_sort(tab)
        self.assertEqual(tab, [1, 2, 2, 4, 4])

    def test_un_element(self):
        tab = [9]
        heap_sort(tab)
        self.assertEqual(tab, [9])

    def test_vide(self):
        tab = []
        heap_sort(tab)
        self.assertEqual(tab, [])

    def test_nombres_negatifs(self):
        tab = [-5, 3, -1, 0, 8, -3]
        heap_sort(tab)
        self.assertEqual(tab, sorted(tab))


def lancer_tests_unittest():
    """Lance les tests unittest (Membre 4) sans quitter le programme."""
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    suite.addTests(loader.loadTestsFromTestCase(TestHeapify))
    suite.addTests(loader.loadTestsFromTestCase(TestHeapSort))
    unittest.TextTestRunner(verbosity=2).run(suite)


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
    """Tests automatiques de bout en bout (section 9 du cahier des charges)."""
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
    ligne("TRI PAR TAS")
    print("1. Saisir un tableau et le trier")
    print("2. Générer un tableau aléatoire et le trier")
    print("3. Visualiser étape par étape la construction du Max-Heap")
    print("4. Lancer les tests automatiques (comparaison résultats attendus)")
    print("5. Lancer les tests unitaires de heapify ")
    print("6. Lancer les tests unittest de heap_sort / Max-Heap ")
    print("7. Lancer la démonstration simple de heap_sort ")
    print("8. Afficher la complexité de l'algorithme")
    print("0. Quitter")


def afficher_complexite():
    ligne("COMPLEXITÉ")
    print("Construction du Max-Heap : O(n)")
    print("Tri complet (Heapsort)   : O(n log n)")
    print("Espace supplémentaire   : O(1) (tri en place, hors variables locales)")


def menu():
    print("TRI PAR TAS")
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
            ligne("TESTS UNITAIRES DE HEAPIFY (MEMBRE 3)")
            lancer_tests_heapify()

        elif choix == "6":
            ligne("TESTS UNITTEST (MEMBRE 4)")
            lancer_tests_unittest()

        elif choix == "7":
            ligne("DÉMONSTRATION SIMPLE DE HEAP_SORT (MEMBRE 4)")
            demo_tests_heapsort_simple()

        elif choix == "8":
            afficher_complexite()

        elif choix == "0":
            print("\nFin du programme. Merci !")
            break

        else:
            print("\nChoix invalide, veuillez réessayer.")

        input("\nAppuyez sur Entrée pour continuer...")


if __name__ == "__main__":
    menu()
