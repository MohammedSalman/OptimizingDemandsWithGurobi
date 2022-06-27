import networkx
import networkx as nx
import matplotlib.pyplot as plt


# from networkx import read_gml
from Paths import Paths
from RoutingScheme import RoutingScheme


class Topology:
    """
    Stores network topology graph, configures capacities, visualize graph.
    """

    # def __init__(self):
    #     # self.q = q
    #     # self.num_nodes = num_nodes
    #     # self.num_links = num_links
    #     # self.topo_id = random.random()
    #     pass

    def readFromFile(self, filePath):
        self.topo = nx.read_gml(filePath)

        print(self.topo.edges(data=True))


if __name__ == '__main__':
    topoObj = Topology()
    topoObj.readFromFile("Epoch.gml")
    pathObj = Paths(topoObj, "shortest_path")
    routingObj = RoutingScheme(pathObj)

    # networkx.draw_networkx(topo)


