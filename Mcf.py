from gurobipy import *


class Mcf:

    def __init__(self, shared_dict, pid, topo, paths, routing_scheme, tm):

        self.model_is_feasible = False
        self.z = None
        self.model = None

        self.shared_dict = shared_dict
        self.pid = pid
        self.topoObj = topo
        self.pathObj = paths
        self.routingScheme = routing_scheme
        self.tm = tm

        self.paths_variables = {}
        self.bin_paths_variables = {}
        self.demand_constraint = {}  # tracking demands constraints

        self.build_model()

    def build_model(self):
        try:
            self.model = Model(name="model")
        except RuntimeError:
            print("Check Gurobi installation!")

        # one more variable for the objective function:
        self.z = self.model.addVar(lb=0.0, vtype=GRB.CONTINUOUS, name="z")
        self.model.setObjective(self.z, GRB.MAXIMIZE)

        self.formulate_paths_flow_variables()
        self.build_demand_constraints_template()
        self.build_capacity_constraints()

    # def given_tm_update_model(self, tm):
    #     # todo change method name?? because we are adding constraints
    #     routing_scheme = self.routingScheme.get_routing_scheme()
    #     # using routing scheme only:
    #     for (src, dst) in routing_scheme:
    #         tmp_list = []
    #         for path_list_no, _ in enumerate(routing_scheme[(src, dst)]['Paths']):
    #             path_name_str = str(
    #                 src + '_' + dst + '_path_' + str(path_list_no))  # path sample: PaloAlto_LosAngeles_path_1
    #             path_name_str = path_name_str.replace(" ", "")
    #             tmp_list.append(self.paths_variables[path_name_str])
    #         # print(tm[src][dst])
    #         # self.demand_constraint[(src, dst)].rhs = tm[src][dst]
    #         print("Here: ")
    #         print(self.demand_constraint[(src, dst)].__dict__)
    #         self.demand_constraint[(src, dst)].setAttr("rhs", tm[src][dst])

    def formulate_paths_flow_variables(self):
        routing_scheme = self.routingScheme.get_routing_scheme()
        # using routing scheme only:
        for (src, dst) in routing_scheme:
            bin_tmp_list = []
            for path_list_no, _ in enumerate(routing_scheme[(src, dst)]['Paths']):
                path_name_str = str(
                    src + '_' + dst + '_path_' + str(path_list_no))  # path sample: PaloAlto_LosAngeles_path_1
                path_name_str = path_name_str.replace(" ", "")
                self.paths_variables[path_name_str] = self.model.addVar(lb=0.0, vtype=GRB.CONTINUOUS,
                                                                        name=path_name_str)
                # add the corresponding binary variable:
                self.bin_paths_variables["bin_" + path_name_str] = self.model.addVar(vtype=GRB.BINARY,
                                                                                     name="bin_" + path_name_str)
                bin_tmp_list.append(self.bin_paths_variables["bin_" + path_name_str])
                self.model.addConstr(self.paths_variables[path_name_str] >= 0.0)  # no need if it is a bin?
            self.model.addConstr(sum(bin_tmp_list) == 1.0)

    def optimize(self):
        self.model.update()
        self.model.optimize()
        if self.model.Status != GRB.OPTIMAL:
            self.model_is_feasible = False
            return
        self.model_is_feasible = True

    def save_data_to_shared_dict(self):
        if not self.model_is_feasible:
            return
        # store the input first (traffic matrices).
        for src in self.tm:
            for dst in self.tm[src]:
                if src == dst:
                    continue
                src_dst_name = (str(src) + '_' + str(dst)).replace(" ", "")
                self.shared_dict[self.pid][src_dst_name] = self.tm[src][dst]

        for v in self.model.getVars():
            # if v.x == 0.0 or v.x == -0.0:
            #     continue
            # print(v.varName, v.x)
            if "path" in v.varName and "bin" not in v.varName:
                continue
            # don't include the variable of the objective function.
            if v.varName == 'z':
                continue
            self.shared_dict[self.pid][v.varName] = 0.0 if v.x == -0.0 else v.x


    def print_quality(self):
        if self.model.Status == GRB.OPTIMAL:
            print('The model is feasible')
            self.model_is_feasible = True
            return
        if self.model.Status == GRB.INF_OR_UNBD:
            print('Model is unbounded')
            self.model_is_feasible = False
            return
        if self.model.Status == GRB.INFEASIBLE:
            print('Model is infeasible')
            self.model_is_feasible = False
            return
        if self.model.Status == GRB.UNBOUNDED:
            print('Model is unbounded')
            self.model_is_feasible = False
            return

    def write_model(self):
        self.model.write("my model.lp")

    def build_demand_constraints_template(self):
        routing_scheme = self.routingScheme.get_routing_scheme()
        for (src, dst) in routing_scheme:
            tmp_list = []
            bin_tmp_list = []
            for path_list_no, _ in enumerate(routing_scheme[(src, dst)]['Paths']):
                path_name_str = str(
                    src + '_' + dst + '_path_' + str(path_list_no))  # path sample: PaloAlto_LosAngeles_path_1
                path_name_str = path_name_str.replace(" ", "")
                tmp_list.append(self.paths_variables[path_name_str])
                bin_tmp_list.append(self.bin_paths_variables["bin_" + path_name_str])
            # print(tm[src][dst])
            self.demand_constraint[(src, dst)] = self.model.addConstr(
                quicksum(tmp_list[i] * bin_tmp_list[i] for i in range(len(tmp_list))) == self.tm[src][
                    dst])  # 0.0 in the template only
            self.model.update()
            # print(self.demand_constraint[(src, dst)])
        self.model.update()

    def build_capacity_constraints(self):
        self.model.update()
        # first build the links_to_routes structure:
        links_to_routes = {}
        # print(self.topoObj.get_topo().edges)  # use (.adj) to print everything
        for link in self.topoObj.get_topo().edges:
            links_to_routes[(link[0], link[1])] = []
            links_to_routes[(link[1], link[0])] = []
        # print(links_to_routes)
        routing_scheme = self.routingScheme.get_routing_scheme()
        for (src, dst) in routing_scheme:
            for path_list_no, path in enumerate(routing_scheme[(src, dst)]['Paths']):
                path_name_str = str(
                    src + '_' + dst + '_path_' + str(path_list_no))  # path sample: PaloAlto_LosAngeles_path_1
                path_name_str = path_name_str.replace(" ", "")
                for index in range(len(path) - 1):
                    links_to_routes[(path[index], path[index + 1])].append(self.paths_variables[path_name_str])

        for link in links_to_routes:
            tmp_list = []
            # bin_tmp_list = []
            for variable in links_to_routes[link]:
                tmp_list.append(variable)
            self.model.addConstr(quicksum(tmp_list) + self.z <= 1)  # self.z
