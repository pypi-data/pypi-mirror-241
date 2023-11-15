from tketool.ml.modelbase import Model_Base


class graph(Model_Base):
    @property
    def model_name(self):
        return graph

    def __init__(self):
        super().__init__()
        self.save_variables['nodes'] = {}  # id: data
        self.save_variables['node_lines_index'] = {}  # node_id: [line_id]
        self.save_variables['lines'] = {}  # id:data
        self.save_variables['lines_endpoint'] = {}  # id:(start_end)

    def __getitem__(self, item):
        return self.save_variables['nodes'][item]

    def __setitem__(self, key, value):
        self.save_variables['nodes'][key] = value

    def __contains__(self, item):
        return item in self.save_variables['nodes']

    def __iter__(self):
        for item_key, item_value in self.save_variables['nodes'].items():
            yield item_key, item_value

    def add_node(self, id, data=None):
        if id in self.save_variables['nodes']:
            raise Exception("duplicate node id.")
        self.save_variables['nodes'][id] = data

    def add_line(self, node_id1, node_id2, data=None):
        line_name = f"line_{len(self.save_variables['lines'])}"
        self.save_variables['lines'][line_name] = data

        if node_id1 not in self.save_variables['node_lines_index']:
            self.save_variables['node_lines_index'][node_id1] = []
        self.save_variables['node_lines_index'][node_id1].append(line_name)

        if node_id2 not in self.save_variables['node_lines_index']:
            self.save_variables['node_lines_index'][node_id2] = []
        self.save_variables['node_lines_index'][node_id2].append(line_name)

        self.save_variables['lines_endpoint'][line_name] = (node_id1, node_id2)

    def get_node(self, key):
        return self.save_variables['nodes'][key]

    def get_relations(self, key, start_to=True):
        result = []

        if key not in self.save_variables['node_lines_index']:
            return result

        for lineid in self.save_variables['node_lines_index'][key]:
            line_data = self.save_variables['lines'][lineid]
            if start_to:
                if self.save_variables['lines_endpoint'][lineid][0] == key:
                    result.append((self.save_variables['lines_endpoint'][lineid][1], line_data))
                else:
                    continue
            else:
                if self.save_variables['lines_endpoint'][lineid][1] == key:
                    result.append((self.save_variables['lines_endpoint'][lineid][0], line_data))
                else:
                    continue

        return result


# aa = graph()
# aa.add_node("a", 1)
# aa.add_node("b", 2)
# aa.add_line("a", "b", 33)
# aa.add_line("b", "a", 44)
# r1 = aa.get_relations("a")
# r2 = aa.get_relations("a", False)
# pass
