import heapq


class QNode:
    def __init__(self, v):
        self.v = v
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None

    def insert(self, item):
        item = QNode(item)
        if self.first is None:
            self.first = item
        if self.last is not None:
            self.last.next = item
        self.last = item

    def empty(self):
        return self.first is None

    def pop(self):
        v = self.first.v if self.first.v else None
        self.first = self.first.next
        return v


class GenericQueue:
    def __init__(self, queue_type):
        self.queue = queue_type

    def insert(self, item):
        self.queue.put(item)

    def empty(self):
        return self.queue.empty()

    def pop(self):
        return self.queue.get()


class Stack:
    def __init__(self):
        self.stack = []

    def insert(self, item):
        self.stack.append(item)

    def empty(self):
        return len(self.stack) == 0

    def pop(self):
        return self.stack.pop()


class AStar:
    def __init__(self, heuristic):
        self.heuristic = heuristic
        self.heap = []

    def insert(self, item):
        hitem = (item.custo + self.heuristic(item), item)
        heapq.heappush(self.heap, hitem)

    def empty(self):
        return len(self.heap) == 0

    def pop(self):
        item = heapq.heappop(self.heap)
        return item[1]


def make_manhattan_dict():
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


def hamming_heuristic(item):
    goal = "12345678_"
    state = item.estado
    sum = 0
    for i, v in enumerate(goal):
        if v != state[i]:
            sum += 1
    return sum


def manhattan_heuristic(item):
    state = item.estado
    total = 0
    for i, v in enumerate(state):
        total += MANHATTAN_DICT[str(i)][v]
    return total


def swap(string, i, j):
    ls = list(string)
    ls[i], ls[j] = ls[j], ls[i]
    return ''.join(ls)


MANHATTAN_DICT = make_manhattan_dict()