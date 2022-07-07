import os
import csv
import multiprocessing
from multiprocessing import Process

from Demands import Demands
from Mcf import Mcf
from Paths import Paths
from RoutingScheme import RoutingScheme
from Topology import Topology


def formulate_and_optimize(shared_dict, p_id, topo, path, routing_scheme, current_tm):
    mcf = Mcf(shared_dict, p_id, topo, path, routing_scheme, current_tm)
    mcf.optimize()
    mcf.save_data_to_shared_dict()

    # mcf.printQuality()
    # mcf.write_model()


def chunks(ll, nn):
    for index in range(0, len(ll), nn):
        yield ll[index:index + nn]


# def initialize_shared_dictionary():
#     manager = multiprocessing.Manager()
#     return manager.dict()


def saved_shared_dict_to_csv():
    global pid
    output_dir_name = 'output/'
    try:
        os.makedirs(output_dir_name)
    except OSError:
        pass
    filename = "output" + '.csv'
    try:
        with open(output_dir_name + filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile, delimiter=',')
            # if not header_written:
            writer.writerow(shared_dictionary[1].keys())
            #     header_written = True
            alist = []
            for pid in shared_dictionary.keys():
                if not shared_dictionary[pid]:  # if dict is empty, continue. Only when the current model is infesable.
                    continue
                for field_name in shared_dictionary[pid].keys():
                    alist.append(shared_dictionary[pid][field_name])
                writer.writerow(alist)
                # print(alist)
                alist = []
    except PermissionError:
        print("PermissionError: Check if the file is open.")


if __name__ == '__main__':
    number_traffic_matrix = 10
    network_load = 1.1

    topoObj = Topology()
    topoObj.readFromFile("Epoch.gml")  # Geant2001
    pathObj = Paths(topoObj, "shortest_path")
    routingSchemeObj = RoutingScheme(pathObj)
    demands = Demands(topoObj, "uniform", number_traffic_matrix, network_load)

    manager = multiprocessing.Manager()
    shared_dictionary = manager.dict()
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

    saved_shared_dict_to_csv()
    # print(demands.matrices_sequence)
