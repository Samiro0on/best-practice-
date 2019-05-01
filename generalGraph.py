# general graph implementation

class Graph:

    def __init__(self, graph_dict=None):

        if graph_dict == None:
            graph_dict = {}
        self.__graph_dict = graph_dict

    # @property
    def nodes(self):

        return list(self.__graph_dict.keys())


    # @property
    def get_edges(self):
        edges = []
        for node in self.__graph_dict:
            for edge in self.__graph_dict[node]:
                if (edge, node) not in edges:
                    edges.append((node, edge))

        return edges


    def edges(self):

        return self.get_edges()


    def add_node(self, node):
        if node not in self.__graph_dict.keys():
            self.__graph_dict[node] = []


    def add_weighted_node(self, node):
        if node not in self.__graph_dict.keys():
            self.__graph_dict[node] = {}


    def add_edge(self, node1, node2):
        if node1 in self.__graph_dict.keys():
            self.__graph_dict[node1].append(node2)
        else:
            self.__graph_dict[node1] = [node2]


    def add_weighted_edge(self, node1, node2, weight=1):
        if node1 in self.__graph_dict.keys():
            self.__graph_dict[node1][node2] = weight
        else:
            self.__graph_dict[node1] = {node2: weight}
        if node2 in self.__graph_dict.keys():
            self.__graph_dict[node2][node1] = weight
        else:
            self.__graph_dict[node2] = {node1: weight}


    def get_weighted_edges(self):
        edges = []
        for node in self.__graph_dict:
            for edge, weight in self.__graph_dict[node].iteritems():
                if (edge, node, weight) not in edges:
                    edges.append((node, edge, weight))

        return edges


    def __str__(self):

        output = "Nodes: "
        for key in self.__graph_dict:
            output += str(key) + " "
        output += "\nEdges: "
        for edge in self.get_edges():
            output += str(edge) + " "

        return output


    def find_Apath(self, start, end, path = None):
        if path == None:
            path = []

        graph = self.__graph_dict
        path = path + [start]

        if start == end:
            return path
        if start not in graph.keys():
            return None

        for node in graph[start]:
            if node not in path:
                new_path = self.find_Apath(node, end, path)
                if new_path:
                    return new_path
        return None


    def find_All_paths(self, start, end, path = []):

        graph = self.__graph_dict
        path = path + [start]

        if start == end:
            return [path]

        if start not in graph.keys():
            return None

        paths = []

        for node in graph[start]:
            if node not in path:
                new_path = self.find_All_paths(node, end, path)
                for npath in new_path:
                    paths.append(npath)

        return paths


    def display_graph(self):
        return self.__graph_dict

    def BFS(self, start, goal):

        graph = self.__graph_dict
        # visited = [False] * (len(graph))
        if start == goal:
            return "That was easy! Start = goal"
        queue, path = [], []
        queue.append(start)
        # visited = []
        while queue:
            node = queue.pop(0)
            # visited.append(node)
            if node not in path:
                path.append(node)
                if path[-1] == goal:
                    return path
                queue.extend(n for n in graph[node] if n not in path)
        return path


    def weighted_BFS(self, start, goal):

        graph = self.__graph_dict
        distance = 0
        BFS = []
        queue = [start]
        lvl = {}
        sol = [goal]
        while queue:
            node = queue.pop(0)
            if node not in BFS:
                BFS.append(node)
                if BFS[-1] == goal:
                    for xtimes in range(len(sol)-1):
                        distance += graph[sol[xtimes]][sol[xtimes+1]]
                    return BFS, sol, distance
                li = []
                # queue.extend(n for n in graph[node] if n not in path)
                for xNodes in graph[node]:
                    if xNodes not in BFS:
                        queue.append(xNodes)
                        li.append(xNodes)
                if node not in lvl.keys():
                    lvl[node] = li
                    for n in li:
                        if n == goal:
                            yy = lvl.copy()
                            while sol[0] != start:
                                for k, v in yy.items():
                                    if sol[0] in v:
                                        sol.insert(0, k)
        return False


    def DFS(self, start, goal):
        graph = self.__graph_dict
        if start == goal:
            return "That was easy! Start = goal"
        path = []
        stack = [start]

        while stack:
            node = stack.pop(0)
            if node not in path:
                path.append(node)
                if path[-1] == goal:
                    return path
                val = list(graph[node])
                for n in reversed(val):
                    if n not in path:
                        stack.insert(0, n)
        return path

    def DFS_distance(self, path):
        distance = 0
        for xtimes in range(len(path)-1):
            distance += self.__graph_dict[path[xtimes]][path[xtimes+1]]
            # error hna if parent mesh bt3haa hegeeb l distance ezay
            # print("d = ", distance)
        return distance


    def dijkstra_SPT(self, start):
        graph = self.__graph_dict
        unvisited_nodes = list(graph.keys())
        visited_nodes = []
        path = [start]
        possibility = {}
        distance = 0
        cost =[0]
        while unvisited_nodes:
            node = unvisited_nodes.pop(0)
            if node not in visited_nodes:
                visited_nodes.append(node)

            for k, v in graph[path[-1]].items():
                if k not in visited_nodes:
                    possibility[k] = v + distance
            # print("poss", possibility)
            for k, v in possibility.items():
                if v == min(possibility.values()):
                    distance = v
                    cost.append(distance)
                    path.append(k)
                    # possibility.pop(k)
                    # print("path", path)

            del possibility[path[-1]]
            # print("new poss", possibility)

            if len(path) == len(list(graph.keys())):
                return path, cost


if __name__ == "__main__":

    gra = {"a": ["c", 'd', 'f'], "b": ["c", "e"], "c": ["a", "b", "d", "e"], "d": ["c", 'a']
           ,"e": ["c", "b"], "f": ['d', 'j'], 'j': []}

    myGraph = Graph(gra)

    print("Nodes:", myGraph.nodes())
    print("Edges:", myGraph.edges())
    myGraph.add_node('k')
    myGraph.add_edge('f', 'k')
    # print(myGraph.edges())
    print(myGraph.__str__())


    print(myGraph.find_Apath('a', 'e'))
    print(myGraph.find_All_paths('a', 'd'))

    print(myGraph.BFS('a', 'j'))


    g = {'Frankfurt': {'Mannheim':85, 'Wurzburg':217, 'Kassel':173}, 'Mannheim': {'Frankfurt':85, 'Karlsruhe':80},
     'Karlsruhe': {'Augsburg':250, 'Mannheim':80}, 'Augsburg': {'Karlsruhe':250, 'Munchen':84},
     'Wurzburg': {'Erfurt':186, 'Numberg':103,'Frankfurt':217}, 'Erfurt': {'Wurzburg':186},
     'Numberg': {'Wurzburg':103, 'Stuttgart':183,'Munchen':167}, 'Munchen': {'Numberg':167, 'Augsburg':84,'Kassel':502},
     'Kassel': {'Frankfurt':173, 'Munchen':502}, 'Stuttgart': {'Numberg':183}}

    yourGraph = Graph(g)
    print(yourGraph.nodes())
    print(yourGraph.get_edges())
    print(yourGraph.__str__())
    print(yourGraph.BFS('Frankfurt', 'Munchen'))

    bfs, p , d = yourGraph.weighted_BFS("Frankfurt", "Augsburg")
    print("the BFS path is", bfs)
    print("the steps are", p)
    print("distance =", d, "KM")

    print(myGraph.DFS('a', 'e'))
    print(yourGraph.DFS("Frankfurt", 'Stuttgart'))
    # p = yourGraph.DFS("Frankfurt", 'Stuttgart')
    # print(yourGraph.DFS_distance(path= p))

    print(yourGraph.nodes())


    print(yourGraph.find_Apath("Frankfurt", "Augsburg"))
    print(yourGraph.find_All_paths("Frankfurt", "Augsburg"))
    print("%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%")
    print(yourGraph.dijkstra_SPT('Frankfurt'))

# def get_edges(graph):
#     edges = []
#     for node in graph:
#         for edge in graph[node]:
#             edges.append((node, edge))
#
#     return edges

# print(get_edges(graph))

