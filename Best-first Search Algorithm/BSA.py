class StateGraph():
    def __init__(self, state_start, state_goal, value):
        self.state_start = state_start
        self.state_goal = state_goal
        self.value = value

class PointAndValue():
    def __init__(self, point, value):
        self.point = point
        self.value = value

def BSA(StateGraph, start, goal):
    # for item in StateGraph:
    #     if item.state_start is start:
    #         open = [PointAndValue(start, item.value)]
    open = [PointAndValue(start, 20)]
    close = []
    while open:
        open.sort(key=lambda x: x.value)
        p = open[0]
        open.remove(p)
        close.append(p)
        if p.point is goal:
            return close        
        for item in StateGraph:
            if item.state_start is p.point and PointAndValue(item.state_goal, item.value) not in close:
                open.append(PointAndValue(item.state_goal, item.value))
    return "Not found"

graph = []
graph.append(StateGraph('A','C', 15))
graph.append(StateGraph('A','D', 6))
graph.append(StateGraph('A','E', 7))
graph.append(StateGraph('C','F', 10))
graph.append(StateGraph('D','F', 10))
graph.append(StateGraph('D','I', 8))
graph.append(StateGraph('F','B', 0))
graph.append(StateGraph('I','B', 0))
graph.append(StateGraph('I','G', 5))
graph.append(StateGraph('G','B', 0))
graph.append(StateGraph('G','H', 3))
graph.append(StateGraph('E','G', 5))
graph.append(StateGraph('E','K', 12))
rs = BSA(graph, "A", "B")
for item in rs:
    print(item.point, item.value)
