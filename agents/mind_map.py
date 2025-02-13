import networkx as nx

class MindMapAgent:
    def __init__(self):
        self.graph = nx.DiGraph()

    def process(self, question, context):
        self.graph.add_node(question)
        for fact in context:
            self.graph.add_edge(question, fact)
        return list(self.graph.successors(question))
