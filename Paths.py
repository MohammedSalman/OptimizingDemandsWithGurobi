# import networkx
import networkx as nx
import matplotlib.pyplot as plt
from itertools import islice


class Paths:

    # self.paths
    # a dictoinary

    def __init__(self, topoObj, paths_algo):
        self.topoObj = topoObj
        if paths_algo == "shortest_path":
            self.build_shortest_paths()

    def k_shortest_paths(self, source, target, k, weight=None):
        return list(islice(nx.shortest_simple_paths(self.topoObj.topo, source, target, weight=weight), k))

    def build_shortest_paths(self):
        self.paths = dict()
        for source in self.topoObj.topo.nodes:
            for destination in self.topoObj.topo.nodes:
                if source == destination:
                    continue
                if source not in self.paths:
                    self.paths[source] = dict()
                if destination not in self.paths[source]:
                    # build list of 2 lists (2 paths)
                    self.paths[source][destination] = list(self.k_shortest_paths(source, destination, 30))


        #print(self.paths)

        # for path in self.k_shortest_paths('London', 'Paris', 100):
        #     print(path)
