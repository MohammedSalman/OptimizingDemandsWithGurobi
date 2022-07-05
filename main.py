import multiprocessing
from multiprocessing import Process

from Mcf import Mcf
from Topology import Topology
from Paths import Paths
from RoutingScheme import RoutingScheme
from Demands import Demands


def formulate_and_optimize(shared_dict, topo, path, routing_scheme, current_tm):
    mcf = Mcf(shared_dict, topo, path, routing_scheme, current_tm)
    mcf.optimize()
    mcf.printQuality()
    mcf.write_model()


def chunks(ll, nn):
    for index in range(0, len(ll), nn):
        yield ll[index:index + nn]


def initialize_shared_dictionary():
    manager = multiprocessing.Manager()
    return manager.dict()


if __name__ == '__main__':
    number_traffic_matrix = 100
    network_load = 1.0

    topoObj = Topology()
    topoObj.readFromFile("Epoch.gml")  # Geant2001
    pathObj = Paths(topoObj, "shortest_path")
    routingSchemeObj = RoutingScheme(pathObj)
    demands = Demands(topoObj, "uniform", number_traffic_matrix, network_load)

    shared_dictionary = initialize_shared_dictionary()
    procs = []
    for traffic_matrix in demands.matrices_sequence:
        proc = Process(target=formulate_and_optimize, args=(shared_dictionary, topoObj, pathObj, routingSchemeObj, traffic_matrix))
        procs.append(proc)

    # run all processes in chunks, so we don't overload CPU & Memory
    for i in chunks(procs, multiprocessing.cpu_count()):
        for j in i:
            j.start()
        for j in i:
            j.join()

    # print(demands.matrices_sequence)
