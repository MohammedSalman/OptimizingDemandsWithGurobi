# allocation is 1/k-paths
# from Topology import Topology
# from Paths import Paths

class RoutingScheme:
    def __init__(self, pathsObj):
        self.routing_scheme = None
        self.pathsObj = pathsObj
        self.build_routing_scheme()

    def build_routing_scheme(self):
        self.routing_scheme = {}
        for source in self.pathsObj.paths:
            for destination in self.pathsObj.paths[source]:
                path_tuple = (source, destination)
                self.routing_scheme[path_tuple] = dict()
                path_list = self.pathsObj.paths[source][destination]
                self.routing_scheme[path_tuple]["Paths"] = path_list
                self.routing_scheme[path_tuple]["Allocation"] = [1/len(path_list)] * len(path_list)
        # print(self.routing_scheme)

    def get_routing_scheme(self):
        return self.routing_scheme



