# generate 10 (nu_of_TM) distribution using a topology
# we might also require less data if we can create different distribution
# % of data will be a specific distribution
# adding 0 into the model can help the model learn faster because it can identify which neurons are the more effective

import copy
import numpy as np

import RoutingScheme


class Demands:
    matrices_sequence = []

    def __init__(self, topo, dist_type, nu_of_tms, network_load):
        self.topo = topo.topo
        self.nu_of_TM = nu_of_tms
        self.dist_type = dist_type
        self.network_load = network_load

        if dist_type == "uniform":
            self.generate_uniform()

    def generate_uniform(self):
        num_nodes = len(self.topo.nodes())

        # making the percentage of 0s in matrix dynamic according to num_nodes
        if num_nodes >= 10:
            percentage = 0.05
        else:
            percentage = -0.05 * num_nodes + 0.75

        # print(loc)

        # randomly assign the percentage in the tm
        tm = {}
        for s in self.topo.nodes():
            tm[s] = {}
            for d in self.topo.nodes():
                tm[s][d] = 0.0

        for _ in range(self.nu_of_TM):
            # find the position where we will randomly assign 0s in the matrix
            # for i in range(100):
            loc = []
            num_of_zeros = np.random.randint(int(percentage * ((num_nodes * num_nodes) - num_nodes)))
            for _ in range(num_of_zeros):
                loc.append(np.random.randint((num_nodes * num_nodes) - num_nodes))
            print(loc)
            rnd_mat = np.random.uniform(0, 1, size=(num_nodes, num_nodes))
            # print(rnd_mat)

            # this skips the ones in the matrix where src == dst
            for src_i, src in enumerate(tm.keys()):
                for dst_i, dst in enumerate(tm.keys()):
                    if dst != src:
                        if np.random.uniform() < 0.15:
                            #TODO the hardcoded number above should be passed as a parameter.
                            # The user should adjust this parameter is needed.
                            tm[src][dst] = "zeroes"
                        else:
                            tm[src][dst] = rnd_mat[src_i][dst_i] * self.network_load  # std = tm[src][dst]/5

            temp_tm = copy.deepcopy(tm)
            self.matrices_sequence.append(temp_tm)

        for traffic_matrix in self.matrices_sequence:
            print(traffic_matrix)



