# https://www.coolmathgames.com/0-bloxorz This code solves bloxory game in the minumum number of movement

def blox_solver(ar):
    data = set()
    new_element = set()
    x_limit = len(ar)
    y_limit = len(ar[0])
    coor_start = ()
    fnish_coor = ()
    all_moves = set()
    for x, part in enumerate(ar):
        for y, el in enumerate(part):
            if el == "X":
                fnish_coor = (x, y)
            if el == "B":
                coor_start = (x,y)

    class Blox:
        def __init__(self, coor, answer):
            self.coor = coor
            all_moves.add(coor)
            self.position = True if not type(self.coor[0]) == tuple else False
            self.answer = answer

        def moves_for_up(self):
            x, y = self.coor
            return [((x - 1, y), (x - 2, y)),  # Up
                    ((x, y + 1), (x, y + 2)),  # Right
                    ((x + 1, y), (x + 2, y)),  # Down
                    ((x, y - 1), (x, y - 2))]  # Left

        def moves_for_down(self):
            x1, y1 = self.coor[0]
            x2, y2 = self.coor[1]
            x1,x2 = min(x1,x2),max(x1,x2)
            y1,y2 = min(y1,y2), max(y1,y2)
            if x1 == x2: #Yatay
                return (((x1 -1, y1), (x2 -1, y2)),  # UP
                        (x2, y2 + 1),  # Right
                        ((x1 +1, y1), (x2 + 1, y2)),  # Down
                        (x2, y1 -1),  # Left
                        )
            else:
                return ((x1 -1, y1),  # UP
                        ((x1, y1 + 1), (x2, y2 + 1)),  # Right
                        (x2 + 1, y1),  # Down
                        ((x1, y1 - 1), (x2, y2 - 1)),  # Left
                )

        def check_moves(self, moves):
            if type(moves[0]) == tuple:
                for part in moves:
                    x, y = part
                    if 0 <= x < x_limit and 0 <= y < y_limit and ar[x][y] != "0":
                        continue
                    else:
                        return False
                return True

            else:
                x, y = moves
                if 0 <= x < x_limit and 0 <= y < y_limit and ar[x][y] != "0":
                    return True
                else:
                    return False

        def check_win(self):
            if self.position and self.coor == fnish_coor:
                return True
            else:
                return False

        def move(self):
            pos = "URDL"
            if self.position:
                for current,move in enumerate(self.moves_for_up()):
                    if self.check_moves(move):
                        if not move in all_moves:
                            new_element.add(Blox(move, self.answer + pos[current]))
            else:
                for current,move in enumerate(self.moves_for_down()):
                    if self.check_moves(move):
                        if not move in all_moves:
                            new_element.add(Blox(move, self.answer + pos[current]))

    data.add(Blox(coor_start,""))
    while True:
        for element in data:
            if element.check_win():
                return element.answer
            element.move()
        data = new_element
        new_element = set()

# Write map: 0 = air, 1 = block, B = start point, X = Fnish point
print(blox_solver([
    "B111000111111111111",
    "1111000111111111111",
    "1110111111100100111",
    "111111000111111111X",
]))
