from operator import attrgetter

class Graph:
    def __init__(self, key, value, cost):
        self.key = key
        self.value = value
        self.cost = cost

class Current:
    def __init__(self, key, cost):
        self.key = key
        self.cost = cost

def UCS(Graph, root, goal):
    open = [Current(root, 0)]
    close = []
    while open:
        p = min(open,key=attrgetter('cost'))
        cost = p.cost
        open.remove(p)
        close.append(p)
        if p.key == goal:
            return close
        for item in Graph:
            if p.key == item.key and item.value not in close:
                
               open.append(Current(item.value, item.cost + cost))
    return "Not found"      
        
root = 'S'
goal = 'G'
graph = []
graph.append(Graph('S','A', 1))
graph.append(Graph('S','B', 4))
graph.append(Graph('A','D', 2))
graph.append(Graph('A','C', 3))
graph.append(Graph('B','G', 5))
graph.append(Graph('C','E', 5))
graph.append(Graph('D','F', 10))
graph.append(Graph('D','G', 3))
graph.append(Graph('E','G', 5))
rs = UCS(graph, root, goal)

for item in rs:
    print(item.key + ": " + item.cost)

