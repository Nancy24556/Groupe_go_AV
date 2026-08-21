from heapify import heapify
from construire_max_heap import construire_max_heap
from heap_sort import heap_sort


def test_heapify_basic():
    tab = [5, 15, 10, 8, 3]
    heapify(tab, 5, 0)
    assert tab[0] >= tab[1] and tab[0] >= tab[2]
    print("✓ test_heapify_basic")


def test_heapify_enfant_gauche():
    tab = [3, 15, 8]
    heapify(tab, 3, 0)
    assert tab[0] == 15
    print("✓ test_heapify_enfant_gauche")


def test_heapify_enfant_droit():
    tab = [3, 8, 15]
    heapify(tab, 3, 0)
    assert tab[0] == 15
    print("✓ test_heapify_enfant_droit")


def test_heapify_feuille():
    tab = [10, 5, 8, 2, 1]
    heapify(tab, 5, 4)
    assert tab == [10, 5, 8, 2, 1]
    print("✓ test_heapify_feuille")


def test_heapify_deja_heap():
    tab = [20, 15, 10, 5, 3]
    heapify(tab, 5, 0)
    assert tab[0] == 20
    print("✓ test_heapify_deja_heap")


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


def test_heapify_avec_construire_max_heap():
    tab = [12, 5, 8, 20, 3, 15, 7]
    construire_max_heap(tab)
    assert tab[0] == 20
    assert tab[1] >= tab[3] and tab[1] >= tab[4]
    assert tab[2] >= tab[5] and tab[2] >= tab[6]
    print("✓ test_heapify_avec_construire_max_heap")


def test_heapify_avec_heap_sort():
    tab = [12, 5, 8, 20, 3, 15, 7]
    heap_sort(tab)
    assert tab == [3, 5, 7, 8, 12, 15, 20]
    print("✓ test_heapify_avec_heap_sort")


if __name__ == "__main__":
    print("=== TESTS HEAPIFY ===\n")
    test_heapify_basic()
    test_heapify_enfant_gauche()
    test_heapify_enfant_droit()
    test_heapify_feuille()
    test_heapify_deja_heap()
    test_heapify_doublons()
    test_heapify_arbre_complet()
    test_heapify_un_element()
    test_heapify_negatifs()
    test_heapify_avec_construire_max_heap()
    test_heapify_avec_heap_sort()
    print("\nTous les tests passés ✓")
