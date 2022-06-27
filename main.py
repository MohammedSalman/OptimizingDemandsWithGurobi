from Mcf import Mcf
from Topology import Topology
from Paths import Paths
from RoutingScheme import RoutingScheme
from Demands import Demands

if __name__ == '__main__':
    topoObj = Topology()
    topoObj.readFromFile("Epoch.gml")
    pathObj = Paths(topoObj, "shortest_path")
    routingSchemeObj = RoutingScheme(pathObj)
    demands = Demands(topoObj, "uniform", 20, 0.5)

    mcf = Mcf(topoObj, pathObj, routingSchemeObj)

    for tm in demands.matrices_sequence:
        mcf.set_traffic_matrix(tm)
        mcf.optimize()







    #print(demands.matrices_sequence)

