import numpy as np
import copy


class State:
    """
    Contructeur d'un état initial
    """

    def __init__(self, pos):
        """
        pos donne la position de la voiture i dans sa ligne ou colonne (première case occupée par la voiture);
        """
        self.pos = np.array(pos)

        """
        c,d et prev premettent de retracer l'état précédent et le dernier mouvement effectué
        """
        self.c = self.d = self.prev = None

        self.nb_moves = 0
        self.score = 0

        # TODO
        self.rock = None

    """
    Constructeur d'un état à partir du mouvement (c,d)
    """

    def move(self, c, d):
        s = State(self.pos)
        s.prev = self
        s.pos[c] += d
        s.c = c
        s.d = d
        s.nb_moves = self.nb_moves + 1
        s.rock = s.prev.rock
        # TODO
        return s

    def put_rock(self, rock_pos):
        # TODO
        s = copy.deepcopy(self)
        s.rock = rock_pos

        return s

    def score_state(self, rh):
        self.score = self.estimee(rh)

        return self.score

    def success(self):
        return self.pos[0] == 4

    def car_blocked(self, rh):
        penalite = 0

        possible_moves = rh.possible_moves(self)
        car_moved = [move.c for move in possible_moves]
        for i in range(1, rh.nbcars):
            if i not in car_moved:
                penalite += (rh.move_on[i] + 1)

        return penalite

    def estimee(self, rh):
        cost = 100 * self.pos[0]

        for i in range(1, rh.nbcars):
            if not rh.horiz[i] and rh.move_on[i] >= self.pos[0] + rh.length[0]:
                if rh.length[i] == 3:
                    cost += (self.pos[i] + 1) * 15

                    for j in range(self.pos[i] + rh.length[i], 6):
                        if rh.free_pos[j][rh.move_on[i]]:
                            cost += (rh.move_on[i] * 2)
                else:
                    if self.pos[i] == 1:
                        if rh.free_pos[0][rh.move_on[i]]:
                            cost += rh.move_on[i]
                    elif self.pos[i] == 2:
                        if rh.free_pos[4][rh.move_on[i]]:
                            cost += rh.move_on[i]
            elif rh.horiz[i] and (self.pos[i] + rh.length[i] - 1) < (self.pos[0]):
                cost += 100
            elif rh.horiz[i] and (self.pos[i] + rh.length[i]) <= (
                    self.pos[0] + rh.length[0]):  # Si t a gauche de l'auto rouge
                cost += 20

        for i in range(self.pos[0] + rh.length[0], 6):
            if rh.free_pos[2][i]:
                cost += 20

        # Penalite si une auto est bloque
        cost -= self.car_blocked(rh)

        return cost

    def __eq__(self, other):
        if not isinstance(other, State):
            return NotImplemented
        if len(self.pos) != len(other.pos):
            print("les états n'ont pas le même nombre de voitures")

        return np.array_equal(self.pos, other.pos)

    def __hash__(self):
        h = 0
        for i in range(len(self.pos)):
            h = 37 * h + self.pos[i]
        return int(h)

    def __lt__(self, other):
        return self.score < other.score
