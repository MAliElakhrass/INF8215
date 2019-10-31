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


if __name__ == '__main__':
    test16moves()

