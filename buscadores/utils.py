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


def busca_grafo(start_node, F):
    objective = "12345678_"
    X = set()
    F.insert(start_node)
    while True:
        if F.empty():
            return len(X), None
        v = F.pop()
        if v.estado == objective:
            return len(X), v.trace_history()
        if v.estado not in X:
            X.add(v.estado)
            for node in v.expand():
                F.insert(node)
