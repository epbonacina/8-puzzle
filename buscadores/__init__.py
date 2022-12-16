def make_manhattan_dict():
    '''
    Creates a dictionary M[c][n] with the Manhattan
    distance for the cell "c" when it contains the number "n".

    Cells are 0-indexed, blank space is represented by the
    number 0.
    '''
    manhattan = dict()
    for cell in range(9):
        manhattan[str(cell)] = dict()
        for number in range(1, 10):
            y1 = (cell)//3
            y2 = (number-1)//3
            x1 = (cell) % 3
            x2 = (number-1) % 3
            if number == 9:
                number = '_'
            manhattan[str(cell)][str(number)] = abs(x2-x1) + abs(y2-y1)
    return manhattan


MANHATTAN_DICT = make_manhattan_dict()
