import math

import numpy as np

from state import State

class MiniMaxSearch:
    def __init__(self, rushHour, initial_state, search_depth):
        self.rushhour = rushHour
        self.state = initial_state
        self.search_depth = search_depth

    def minimax_1(self, current_depth, current_state, visited):
        # TODO
        children = self.rushhour.possible_moves(current_state)
        new_moves = []
        for child in children:
            if child.d != visited[child.c]:
                new_moves.append(child)

        if current_depth == self.search_depth or len(children) == 0 or current_state.success():
            current_state.score_state(self.rushhour)
            return current_state

        values = []
        for child_state in new_moves:
            values.append(self.minimax_1(current_depth + 1, child_state, visited))

        best_max = max(values)

        return best_max


    def minimax_2(self, current_depth, current_state, is_max):
        # TODO
        best_move = None
        best_value_min = math.inf
        best_value_max = -math.inf
        for child_move in self.rushhour.possible_moves(current_state):
            temp_value = self.value(current_state, current_depth)
            if is_max:
                if temp_value > best_value_max:
                    best_value_max = temp_value
                    best_move = child_move
            else:
                if temp_value < best_value_min:
                    best_value_min = temp_value
                    best_move = child_move

        return best_move

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

    def decide_best_move_2(self, state, is_max):
        # TODO
        return self.minimax_2(0, state, is_max)

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
            while not state.success(): # and compteur < 15000:
                compteur += 1
                state = self.decide_best_move_1(state, visited)
                visited[state.c] = state.d * -1
                print("Mouvement: " + str(compteur))
                self.print_move(is_singleplayer, state)

        return state

    def print_move(self, is_max, state):
        # TODO
        index_car = state.c

        if is_max:
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