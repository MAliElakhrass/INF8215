from MiniMaxSearch import MiniMaxSearch
from Rushhour import Rushhour
from state import State


def testRocks():
    rh = Rushhour([True, False, True, False, False, True, False, True, False, True, False, True],
                  [2, 2, 3, 2, 3, 2, 2, 2, 2, 2, 2, 3],
                  [2, 2, 0, 0, 3, 1, 1, 3, 0, 4, 5, 5],
                  ["rouge", "vert clair", "jaune", "orange", "violet clair", "bleu ciel", "rose", "violet", "vert",
                   "noir", "beige", "bleu"])
    s0 = State([1, 0, 3, 1, 1, 4, 3, 4, 4, 2, 4, 1])

    s1 = s0.put_rock((4, 4))
    s2 = s1.put_rock((3, 2))

    print("État initial")
    rh.print_pretty_grid(s0)
    print(rh.free_pos)
    print('\n')

    print("Roche 4-4")
    rh.print_pretty_grid(s1)
    print(rh.free_pos)
    print('\n')

    print("Roche 3-2")
    rh.print_pretty_grid(s2)
    print(rh.free_pos)
    print('\n')


def testPossibleRockMoves():
    rh = Rushhour([True, False, True, False, False, True, False, True, False, True, False, True],
                  [2, 2, 3, 2, 3, 2, 2, 2, 2, 2, 2, 3],
                  [2, 2, 0, 0, 3, 1, 1, 3, 0, 4, 5, 5],
                  ["rouge", "vert clair", "jaune", "orange", "violet clair", "bleu ciel", "rose", "violet", "vert",
                   "noir", "beige", "bleu"])
    s = State([1, 0, 3, 1, 1, 4, 3, 4, 4, 2, 4, 1])
    sols = rh.possible_rock_moves(s)
    print(len(sols))
    s1 = s.put_rock((3, 4))
    sols = rh.possible_rock_moves(s1)
    print(len(sols))


def test_print_move():
    rh = Rushhour([False], [2], [2], ["rouge"])
    s = State([0])
    s = s.put_rock((3, 1))  # Roche dans la case 3-1
    s = s.move(0, 1)  # Voiture rouge vers la droite
    algo = MiniMaxSearch(rh, s, 1)
    algo.print_move(True, s)
    algo.print_move(False, s)


def test9moves():
    rh = Rushhour([True, False, False, False, True],
                  [2, 3, 2, 3, 3],
                  [2, 4, 5, 1, 5],
                  ["rouge", "vert", "bleu", "orange", "jaune"])
    s = State([1, 0, 1, 3, 2])

    algo = MiniMaxSearch(rh, s, 1)
    algo.rushhour.init_positions(s)
    print("Free pos")
    print(algo.rushhour.free_pos)
    algo.solve(s, True)


def test16moves():
    # solution optimale: 16 moves
    rh = Rushhour([True, True, False, False, True, True, False, False],
                  [2, 2, 3, 2, 3, 2, 3, 3],
                  [2, 0, 0, 0, 5, 4, 5, 3],
                  ["rouge", "vert", "mauve", "orange", "emeraude", "lime", "jaune", "bleu"])
    s = State([1, 0, 1, 4, 2, 4, 0, 1])
    algo = MiniMaxSearch(rh, s, 1)
    algo.rushhour.init_positions(s)
    print(algo.rushhour.free_pos)
    algo.solve(s, True)


def test14moves():
    rh = Rushhour([True, False, True, False, False, False, True, True, False, True, True],
                  [2, 2, 3, 2, 2, 3, 3, 2, 2, 2, 2],
                  [2, 0, 0, 3, 4, 5, 3, 5, 2, 5, 4],
                  ["rouge", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])
    s = State([0, 0, 3, 1, 2, 1, 0, 0, 4, 3, 4])
    algo = MiniMaxSearch(rh, s, 1)
    algo.rushhour.init_positions(s)
    print(algo.rushhour.free_pos)
    algo.solve(s, True)


def test9moves3depth():
    rh = Rushhour([True, False, False, False, True],
                  [2, 3, 2, 3, 3],
                  [2, 4, 5, 1, 5],
                  ["rouge", "vert", "bleu", "orange", "jaune"])
    s = State([1, 0, 1, 3, 2])
    algo = MiniMaxSearch(rh, s, 3)
    algo.rushhour.init_positions(s)
    print(algo.rushhour.free_pos)
    algo.solve(s, False)


def test16moves3depth():
    # solution optimale: 16 moves
    rh = Rushhour([True, True, False, False, True, True, False, False],
                  [2, 2, 3, 2, 3, 2, 3, 3],
                  [2, 0, 0, 0, 5, 4, 5, 3],
                  ["rouge", "vert", "mauve", "orange", "emeraude", "lime", "jaune", "bleu"])
    s = State([1, 0, 1, 4, 2, 4, 0, 1])
    algo = MiniMaxSearch(rh, s, 3)
    algo.rushhour.init_positions(s)
    # print(algo.rushhour.free_pos)
    algo.solve(s, False)


def test14moves3depth():
    rh = Rushhour([True, False, True, False, False, False, True, True, False, True, True],
                  [2, 2, 3, 2, 2, 3, 3, 2, 2, 2, 2],
                  [2, 0, 0, 3, 4, 5, 3, 5, 2, 5, 4],
                  ["rouge", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])
    s = State([0, 0, 3, 1, 2, 1, 0, 0, 4, 3, 4])
    algo = MiniMaxSearch(rh, s, 3)
    algo.rushhour.init_positions(s)
    print(algo.rushhour.free_pos)
    algo.solve(s, False)


def test9movesAlphaBeta():
    # solution optimale: 9 moves
    rh = Rushhour([True, False, False, False, True],
                  [2, 3, 2, 3, 3],
                  [2, 4, 5, 1, 5],
                  ["rouge", "vert", "bleu", "orange", "jaune"])
    s = State([1, 0, 1, 3, 2])
    algo = MiniMaxSearch(rh, s, 3)
    algo.rushhour.init_positions(s)
    # print(algo.rushhour.free_pos)
    algo.solve(s, False, algo_type="pruning")


def test16movesAlphaBeta():
    # solution optimale: 16 moves
    rh = Rushhour([True, True, False, False, True, True, False, False],
                  [2, 2, 3, 2, 3, 2, 3, 3],
                  [2, 0, 0, 0, 5, 4, 5, 3],
                  ["rouge", "vert", "mauve", "orange", "emeraude", "lime", "jaune", "bleu"])
    s = State([1, 0, 1, 4, 2, 4, 0, 1])
    algo = MiniMaxSearch(rh, s, 3)
    algo.rushhour.init_positions(s)
    print(algo.rushhour.free_pos)
    algo.solve(s, False, algo_type="pruning")


def test14movesAlphaBeta():
    # solution optimale: 14 moves
    rh = Rushhour([True, False, True, False, False, False, True, True, False, True, True],
                  [2, 2, 3, 2, 2, 3, 3, 2, 2, 2, 2],
                  [2, 0, 0, 3, 4, 5, 3, 5, 2, 5, 4],
                  ["rouge", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])
    s = State([0, 0, 3, 1, 2, 1, 0, 0, 4, 3, 4])
    algo = MiniMaxSearch(rh, s, 3)
    algo.rushhour.init_positions(s)
    print(algo.rushhour.free_pos)
    algo.solve(s, False, algo_type="pruning")


def test9movesExpectimax():
    # solution optimale: 9 moves
    rh = Rushhour([True, False, False, False, True],
                  [2, 3, 2, 3, 3],
                  [2, 4, 5, 1, 5],
                  ["rouge", "vert", "bleu", "orange", "jaune"])
    s = State([1, 0, 1, 3, 2])
    algo = MiniMaxSearch(rh, s, 3)
    algo.rushhour.init_positions(s)
    # print(algo.rushhour.free_pos)
    algo.solve(s, False, algo_type="expectimax", ai_vision="pessimiste")


def test16movesExpectimax():
    # solution optimale: 16 moves
    rh = Rushhour([True, True, False, False, True, True, False, False],
                  [2, 2, 3, 2, 3, 2, 3, 3],
                  [2, 0, 0, 0, 5, 4, 5, 3],
                  ["rouge", "vert", "mauve", "orange", "emeraude", "lime", "jaune", "bleu"])
    s = State([1, 0, 1, 4, 2, 4, 0, 1])
    algo = MiniMaxSearch(rh, s, 3)
    algo.rushhour.init_positions(s)
    print(algo.rushhour.free_pos)
    algo.solve(s, False, algo_type="expectimax", ai_vision="pessimiste")


def test14movesExpectimax():
    # solution optimale: 14 moves
    rh = Rushhour([True, False, True, False, False, False, True, True, False, True, True],
                  [2, 2, 3, 2, 2, 3, 3, 2, 2, 2, 2],
                  [2, 0, 0, 3, 4, 5, 3, 5, 2, 5, 4],
                  ["rouge", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"])
    s = State([0, 0, 3, 1, 2, 1, 0, 0, 4, 3, 4])
    algo = MiniMaxSearch(rh, s, 3)
    algo.rushhour.init_positions(s)
    print(algo.rushhour.free_pos)
    algo.solve(s, False, algo_type="expectimax", ai_vision="pessimiste")


if __name__ == '__main__':
    print("\n\nPartie 2 Implémentation d'une recherche minimax (35pts)\n")
    """
    print("2.1 Implémentation simple")
    print("Test 9 moves")
    test9moves()
    print("Test 16 moves")
    test16moves()
    print("Test 14 moves")
    test14moves()
    print("2.2 Implémentation adversarielle")
    print("Test 9 moves")
    test9moves3depth()
    print("Test 16 moves")
    test16moves3depth()
    print("Test 14 moves")
    test14moves3depth()

    print("\n\nPartie 3 Élagage Alpha-Beta (15pts)\n")
    print("Test 9 moves")
    test9movesAlphaBeta()
    print("Test 16 moves")
    test16movesAlphaBeta()
    print("Test 14 moves")
    test14movesAlphaBeta()
    """
    # """
    print("\n\nPartie 4 Expectimax (15 pts)\n")
    print("Test 9 moves")
    test9movesExpectimax()
    print("Test 16 moves")
    # test16movesExpectimax()
    print("Test 14 moves")
    # test14movesExpectimax()
    # """

