import logging
import pandas as pd
import networkx as nx

from cobra.manipulation import remove_genes
from cobra.flux_analysis import find_blocked_reactions

from csmemo.reachability import find_gene_knockout_reactions



class UmFinder:
    def __init__(self, cobra_model, cc_method='fva', level=logging.INFO):
        
        self._model = cobra_model
        logging.basicConfig(level=level)

        logging.info(" ===========================================================")
        logging.info(" Initializing UmFinder Builder using")
        logging.info(" Model: %s" % cobra_model.id)

        logging.info(" - Nº of reactions: %i" % len(self._model.reactions))
        logging.info(" - Nº of metabolites: %i" % len(self._model.metabolites))
        logging.info(" Checking network consistency (may take some minutes)")
        logging.info(" Finding blocked reaction using method: %s\n" % cc_method)

        self._blocked_reactions = find_blocked_reactions(self.model)
        self._gap_metabolites = UmFinder.find_gap_metabolites(self.model, self.blocked_reactions)
        self._gap_graph = UmFinder.create_gap_graph(self.model, self._gap_metabolites, self._blocked_reactions)

        unconnected_modules = nx.connected_components(self._gap_graph.to_undirected())
        self._unconnected_modules = sorted(unconnected_modules, key=lambda x: len(x), reverse=True)

        
        logging.info(" - Nº of blocked reactions: %i" % len(self._blocked_reactions))
        logging.info(" - Nº of gap metabolites: %i" % len(self._gap_metabolites))
        logging.info(" - Nº of unconnected modules: %i" % len(self.unconnected_modules))

        if len(self.unconnected_modules):
            df_ums = self.unconnected_modules_frame()
            df_biggest_um = df_ums.node_type[df_ums.um_id == 1]
            rxns = df_biggest_um.index[df_biggest_um =='rxn']
            mets = df_biggest_um.index[df_biggest_um == 'met']
            logging.info(" - Nº of reactions in the biggest unconnected module: %i" % len(rxns))
            logging.info(" - Nº of metabolites in the biggest unconnected module: %i" % len(mets))


    @property
    def model(self):
        return self._model

    @property
    def gap_metabolites(self):
        return frozenset(self._gap_metabolites)

    @property
    def gap_graph(self):
        return self._gap_graph

    @property
    def blocked_reactions(self):
        return frozenset(self._blocked_reactions)

    @property
    def unconnected_modules(self):
        return self._unconnected_modules

    def update(self):
        self._blocked_reactions = find_blocked_reactions(self.model)
        self._gap_metabolites = UmFinder.find_gap_metabolites(self.model, self.blocked_reactions)
        self._gap_graph = UmFinder.create_gap_graph(self.model, self._gap_metabolites, self._blocked_reactions)
        self._unconnected_modules = nx.connected_component_subgraphs(self._gap_graph.to_undirected())
        self._unconnected_modules = sorted(self._unconnected_modules, key=lambda x: len(x), reverse=True)

    def unconnected_module_subgraphs(self):
        for um in self.unconnected_modules:
            yield self.gap_graph.subgraph(um)

    def unconnected_modules_frame(self, unconnected_modules=[]):
        columns = ['node_id', 'node_type', 'um_id']
        data = {}
        counter = 0
        if len(unconnected_modules) == 0:
            unconnected_modules = self.unconnected_modules
        for i, um in enumerate(unconnected_modules):
            for e in um:
                if e in self.gap_metabolites:
                    e_type = 'met'
                elif e in self.blocked_reactions:
                    e_type = 'rxn'
                else:
                    e_type = None
                data[counter] = (e, e_type, i+1)
                counter += 1

        return pd.DataFrame.from_dict(data, orient='index', columns=columns)

    def find_new_ums(self, reactions_to_inactivate):
        if len(reactions_to_inactivate) == 0:
            return []

        if hasattr(reactions_to_inactivate[0], 'id'):
            reactions_to_inactivate = [r.id for r in reactions_to_inactivate]

        bounds = {}

        for r in reactions_to_inactivate:
            r = self.model.reactions.get_by_id(r)
            bounds[r.id] = r.bounds
            r.bounds = (0, 0)
            print(r)

        new_blocked_reactions = find_blocked_reactions(self.model)

        for r in reactions_to_inactivate:
            r = self.model.reactions.get_by_id(r)
            r.bounds = bounds[r.id]

        new_blocked_reactions = set(new_blocked_reactions) - self.blocked_reactions
        new_blocked_reactions = list(new_blocked_reactions)
        print(new_blocked_reactions)
        new_gap_metabolites = UmFinder.find_gap_metabolites(self.model, new_blocked_reactions)
        new_gap_graph = UmFinder.create_gap_graph(self.model, new_gap_metabolites, new_blocked_reactions)
        new_unconnected_modules = nx.connected_components(new_gap_graph.to_undirected())

        return new_unconnected_modules

    def get_trimmed_model(self, trim_genes=True):
        logging.info(" Creating Trimmed Model")
        trimmed_model = self.model.copy()
        blocked_reactions = [trimmed_model.reactions.get_by_id(r) for r in self.blocked_reactions]
        if len(blocked_reactions) > 0:
            logging.info(f" - trimming {len(blocked_reactions)} blocked reactions")
            trimmed_model.remove_reactions(blocked_reactions)

        gap_metabolites = [trimmed_model.metabolites.get_by_id(i) for i in self.gap_metabolites]
        if len(gap_metabolites) > 0:
            logging.info(f" - trimming {len(gap_metabolites)} gap metabolites")
            trimmed_model.remove_metabolites(gap_metabolites)

        orphan_genes = [g for g in trimmed_model.genes if len(g.reactions) == 0]
        if len(orphan_genes) > 0 and trim_genes:
            logging.info(f" - trimming {len(orphan_genes)} orphan genes")
            remove_genes(trimmed_model, orphan_genes)
            
        return trimmed_model

    @staticmethod
    def find_gap_metabolites(model, blocked_reactions=[]):
        if len(blocked_reactions) == 0:
            blocked_reactions = find_blocked_reactions(model)
        gap_metabolites = []
        for m in model.metabolites:
            reactions = set([r.id for r in m.reactions])
            if reactions.issubset(blocked_reactions):
                gap_metabolites.append(m.id)

        return gap_metabolites

    @staticmethod
    def create_metabolic_graph(cobra_model, directed=True, reactions=None, rev_rxn_label='reversible'):

        graph = nx.DiGraph()
        if not directed:
            graph = nx.Graph()

        if not reactions:
            reactions = cobra_model.reactions

        if not hasattr(reactions[0], 'id'):
            reactions = [cobra_model.reactions.get_by_id(r) for r in reactions]

        for r in reactions:
            graph.add_node(r.id, label=r.id, text=r.id, node_class="rxn", node_id=r.id)
            for m in r.metabolites:
                if m.id not in graph.nodes():
                    graph.add_node(m.id, label=m.id, text=m.id, node_class="met", node_id=m.id)

                (tail, head) = (r.id, m.id)
                if r.get_coefficient(m) < 0:
                    (tail, head) = (m.id, r.id)

                graph.add_edge(tail, head)
                graph[tail][head][rev_rxn_label] = r.lower_bound < 0

        return graph

    @staticmethod
    def create_gap_graph(model, gap_metabolites, blocked_reactions):

        if len(gap_metabolites):
            if hasattr(gap_metabolites[0], 'id'):
                gap_metabolites = [m.id for m in gap_metabolites]

        if len(blocked_reactions) > 0:
            if hasattr(blocked_reactions[0], 'id'):
                blocked_reactions = [r.id for r in blocked_reactions]

        graph = UmFinder.create_metabolic_graph(model)
        gap_graph = graph.subgraph(gap_metabolites + blocked_reactions)

        return gap_graph


def get_unconnected_modules_frame(model, element_list, element_type='gene'):
    df = None
    um_finder = UmFinder(model)
    result_dict = {}
    if element_type == 'gene':
        for g in element_list:
            gene = model.genes.get_by_id(g)
            reactions_to_disable = find_gene_knockout_reactions(model, [gene])
            if len(reactions_to_disable) == 0:
                continue
            result_dict[g] = um_finder.find_new_ums(reactions_to_disable)

        data = []
        for g in result_dict:
            for i, um in enumerate(result_dict[g]):
                gene_id = "%s.%i" % (g, i+1)
                for e in um:
                    if e in model.reactions:
                        etype = 'rxn'
                    elif e in model.metabolites:
                        etype = 'met'
                    row = (gene_id, e, etype)
                    data.append(row)

        index = range(len(data))
        columns = ('gene_id', 'element_id', 'element_type')
        df = pd.DataFrame(data, columns=columns, index=index)

        return df

    if element_type == 'reactions':
        um_finder.find_new_ums(element_list)

    return df




