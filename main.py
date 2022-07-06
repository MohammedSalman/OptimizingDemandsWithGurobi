import multiprocessing
from multiprocessing import Process

from Demands import Demands
from Mcf import Mcf
from Paths import Paths
from RoutingScheme import RoutingScheme
from Topology import Topology


def formulate_and_optimize(shared_dict, pid, topo, path, routing_scheme, current_tm):
    mcf = Mcf(shared_dict, pid, topo, path, routing_scheme, current_tm)
    mcf.optimize()
    # mcf.printQuality()
    # mcf.write_model()


def chunks(ll, nn):
    for index in range(0, len(ll), nn):
        yield ll[index:index + nn]


def initialize_shared_dictionary():
    manager = multiprocessing.Manager()
    return manager.dict()


if __name__ == '__main__':
    number_traffic_matrix = 3
    network_load = 1.0

    topoObj = Topology()
    topoObj.readFromFile("Epoch.gml")  # Geant2001
    pathObj = Paths(topoObj, "shortest_path")
    routingSchemeObj = RoutingScheme(pathObj)
    demands = Demands(topoObj, "uniform", number_traffic_matrix, network_load)

    manager = multiprocessing.Manager()
    shared_dictionary =  manager.dict()
    procs = []
    for pid, traffic_matrix in enumerate(demands.matrices_sequence):
        # pid is not a process id but it is a unique id.
        shared_dictionary[pid] = manager.dict()

        proc = Process(target=formulate_and_optimize,
                       args=(shared_dictionary, pid, topoObj, pathObj, routingSchemeObj, traffic_matrix))
        procs.append(proc)

    # run all processes in chunks, so we don't overload CPU & Memory
    for i in chunks(procs, multiprocessing.cpu_count()):
        for j in i:
            j.start()
        for j in i:
            j.join()

    for p_id in shared_dictionary:

        print(p_id, shared_dictionary[p_id])
    # print(demands.matrices_sequence)
