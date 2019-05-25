class Graph:
  def __init__(self, key, value):
    self.key = key
    self.value = value

def DFS(s, g, graph):
    open = [s]
    close = []
    result = []
    while open:
        p = open[0]
        open.remove(p)
        result.append(p)
        close.append(p)
        if p is g:
            return result
        index = 0
        for item in graph:
            if (item.key == p) and (item.value not in close):
                open.insert(index, item.value)
                index += 1
    return "Not found"
    

s = 'S'
g = 'T'
graph = []
graph.append(Graph('S','A'))
graph.append(Graph('S','H'))
graph.append(Graph('A','B'))
graph.append(Graph('A','C'))
graph.append(Graph('B','D'))
graph.append(Graph('B','E'))
graph.append(Graph('C','G'))
graph.append(Graph('H','I'))
graph.append(Graph('H','J'))
graph.append(Graph('I','K'))
rs = DFS(s, g, graph)
print(rs)