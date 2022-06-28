from gurobipy import *


class Mcf:

    def __init__(self, topo, paths, routing_scheme, tm):
        self.model = None
        self.topoObj = topo
        self.pathObj = paths
        self.routingScheme = routing_scheme
        self.paths_variables = {}
        self.tm = tm

        self.build_model()

    def build_model(self):
        try:
            self.model = Model(name="model")
        except RuntimeError:
            print("Check Gurobi installation!")

        # one more variable for the objective function:
        z = self.model.addVar(lb=0.0, vtype=GRB.CONTINUOUS, name="z")
        self.model.setObjective(z, GRB.MINIMIZE)

        self.formulate_paths_flow_variables()
        self.addDemandConstr()

    def given_tm_update_model(self, tm):
        # todo change method name?? because we are adding constraints
        routing_scheme = self.routingScheme.get_routing_scheme()
        # using routing scheme only:
        for (src, dst) in routing_scheme:
            tmp_list = []
            for path_list_no, _ in enumerate(routing_scheme[(src, dst)]['Paths']):
                path_name_str = str(
                    src + '_' + dst + '_path_' + str(path_list_no))  # path sample: PaloAlto_LosAngeles_path_1
                path_name_str = path_name_str.replace(" ", "")
                tmp_list.append(self.paths_variables[path_name_str])

            self.model.addConstr(sum(tmp_list) == self.tm[src][dst])

    def formulate_paths_flow_variables(self):
        routing_scheme = self.routingScheme.get_routing_scheme()
        # using routing scheme only:
        for (src, dst) in routing_scheme:
            for path_list_no, _ in enumerate(routing_scheme[(src, dst)]['Paths']):
                path_name_str = str(
                    src + '_' + dst + '_path_' + str(path_list_no))  # path sample: PaloAlto_LosAngeles_path_1
                path_name_str = path_name_str.replace(" ", "")
                self.paths_variables[path_name_str] = self.model.addVar(lb=0.0, vtype=GRB.CONTINUOUS,
                                                                        name=path_name_str)
                self.model.addConstr(self.paths_variables[path_name_str] >= 0.0)

    def addDemandConstr(self):
        yield

    def optimize(self):
        self.model.update()
        pass
