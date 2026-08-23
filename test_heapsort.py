# =========================================================
# PROJET ALGO AVANCÉ - Sujet 5 : Tri par Tas (Heapsort)
# MEMBRE 4 : Andy Hifaliana
# RÔLE : Validation globale et tests unitaires (unittest)
# =========================================================

"""
Tests unitaires pour le projet Heapsort.
Couvre les cas décrits dans le rapport : normal, déjà trié,
inversé, doublons, un élément, tableau vide.
"""

import unittest
from heapsort import heap_sort, construire_max_heap


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
        # La racine doit être le plus grand élément
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


if __name__ == "__main__":
    unittest.main(verbosity=2)