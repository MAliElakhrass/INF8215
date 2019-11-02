import math

import numpy as np

from state import State


class MiniMaxSearch:
    def __init__(self, rushHour, initial_state, search_depth):
        self.rushhour = rushHour
        self.state = initial_state
        self.search_depth = search_depth

    def remove_reverse_move(self, state, visited):
        children = self.rushhour.possible_moves(state)
        new_moves = []
        for child in children:
            if child.d != visited[child.c]:
                new_moves.append(child)

        return new_moves

    def minimax_1(self, current_depth, current_state, visited):
        # TODO
        children = self.remove_reverse_move(current_state, visited)

        if current_depth == self.search_depth or current_state.success():
            current_state.score_state(self.rushhour)
            return current_state

        values = []
        for child_state in children:
            values.append(self.minimax_1(current_depth + 1, child_state, visited))

        best_max = max(values)

        return best_max

    # Retourner le score au lieu d'un state, quand t au depth de niveau 1, tu choisis le meilleur score
    # AI, Roche, AI, Roche, ...
    def minimax_2(self, current_depth, current_state, is_max, visited):
        if current_depth == self.search_depth or current_state.success():
            current_state.score_state(self.rushhour)
            return current_state

        if is_max:
            max_values = []
            children = self.remove_reverse_move(current_state, visited)
            for child_state in children:
                max_values.append(self.minimax_2(current_depth + 1, child_state, False, visited))
            return max(max_values)
        else:
            min_values = []
            children = self.rushhour.possible_rock_moves(current_state)
            for child_state in children:
                min_values.append(self.minimax_2(current_depth + 1, child_state, True, visited))
            return min(min_values)

    def minimax_pruning(self, current_depth, current_state, is_max, alpha, beta):
        # TODO
        return best_move

    def expectimax(self, current_depth, current_state, is_max):
        # TODO
        return best_move

    def decide_best_move_1(self, state, visited):
        # TODO
        return self.minimax_1(0, state, visited)
        # return state.move(best_child.c, best_child.d)

    def decide_best_move_2(self, state, is_max, visited):
        # TODO
        return self.minimax_2(0, state, is_max, visited)

    def decide_best_move_pruning(self, is_max):
        # TODO
        return None

    def decide_best_move_expectimax(self, is_max):
        # TODO
        return None

    def solve(self, state, is_singleplayer):
        # TODO
        visited = [0] * self.rushhour.nbcars
        compteur = 0

        if is_singleplayer:
            while not state.success():
                compteur += 1
                state = self.decide_best_move_1(state, visited)
                visited[state.c] = state.d * -1
                print("Mouvement: " + str(compteur))
                self.print_move(True, state)
        else:
            isMax = True
            i = 1
            while not state.success():
                compteur += 1
                state = self.decide_best_move_2(state, isMax, visited)
                if isMax:
                    visited[state.c] = state.d * -1
                i = self.print_previous_depth(state, compteur, i)

                isMax = not isMax

        return state

    def print_previous_depth(self, state, compteur, i):
        if compteur % 2 == 1:
            first_state = state.prev
            print("Mouvement: " + str(i))
            if first_state.success():
                return
            self.print_move(True, first_state)
            print("Mouvement: " + str(i + 1))
            self.print_move(False, state)
            print("Mouvement: " + str(i + 2))
            self.print_move(True, state)
        else:
            first_state = state.prev
            print("Mouvement: " + str(i))
            self.print_move(False, first_state)
            print("Mouvement: " + str(i + 1))
            self.print_move(True, state)
            if state.success():
                return
            print("Mouvement: " + str(i + 2))
            self.print_move(False, state)

        return i + 3

    def print_move(self, is_max, state):
        # TODO
        if is_max:
            index_car = state.c
            if self.rushhour.horiz[index_car]:
                if state.d == +1:
                    print("Voiture " + self.rushhour.color[index_car] + " vers la droite")
                else:
                    print("Voiture " + self.rushhour.color[index_car] + " vers la gauche")
            else:
                if state.d == +1:
                    print("Voiture " + self.rushhour.color[index_car] + " vers le bas")
                else:
                    print("Voiture " + self.rushhour.color[index_car] + " vers le haut")
        else:
            print("Roche dans la case " + str(state.rock[0]) + "-" + str(state.rock[1]))

        return None
