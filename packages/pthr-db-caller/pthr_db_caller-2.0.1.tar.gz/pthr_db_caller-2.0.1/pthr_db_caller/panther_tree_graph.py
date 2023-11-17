import copy
import csv
import networkx
from networkx import MultiDiGraph
from typing import List, Dict
from Bio import Phylo
from Bio.Phylo import Newick
from io import StringIO
from pthr_db_caller.models.panther import NodeDatFile


# Unfortunately, this only uses AN# node IDs instead of PTNs due to parsing from tree files.
# If we parsed the enormous node.dat we could add a PTN option.

class PantherTreePhylo:

    def __init__(self, tree_file):
        # Load graph from tree file
        with open(tree_file) as tf:
            tree_line = tf.readline()
            tree_string = StringIO(tree_line)
            # tree_phylo = next(PantherNewickIOParser(tree_string).parse())
            tree_phylo = next(Phylo.parse(tree_string, "newick"))
            # Leaves parse clean due to not having species name in 'S:'

        self.tree: Newick.Tree = tree_phylo


def extract_clade_name(clade_comment):
    if clade_comment is None:
        clade_comment = ""
    # Ex: &&NHX:Ev=0>1:S=Dictyostelium:ID=AN13  # family internal
    # Ex: &&NHX:Ev=1>0:ID=AN32  # family leaf
    # Ex: &&NHX:S=Endopterygota  # species internal
    # Ex: HUMAN  # species leaf
    new_comment = ""
    comment_bits = clade_comment.split(":")
    for b in comment_bits:
        if b.startswith("S="):
            new_comment = b.replace("S=", "")
            break
    # Also grab ID
    an_id = ""
    for b in comment_bits:
        if b.startswith("ID="):
            an_id = b.replace("ID=", "")
            break
    ###
    new_comment = new_comment.replace("&&NHX:S=", "")
    new_comment = new_comment.replace("&&NXH:S=", "")
    if new_comment == "Opisthokonts":
        new_comment = "Opisthokonta"
    return new_comment, an_id


class PantherTreeGraph:
    def __init__(self, tree_name: str = None):
        self.graph = MultiDiGraph()
        self.name: str = tree_name
        self.ptn_to_an: Dict = {}
        self.an_to_ptn: Dict = {}
        self.an_to_sf: Dict = {}
        self.phylo: PantherTreePhylo = None

    # Recursive method to fill graph from Phylo clade, parsing out node accession and species name (if present)
    def add_children(self, parent_clade):
        self.add_node_from_clade(parent_clade)
        for child in parent_clade.clades:
            self.add_node_from_clade(child)
            self.graph.add_edge(parent_clade.name, child.name)

            if len(child.clades) > 0:
                self.add_children(child)

    def add_node_from_clade(self, clade):
        # Few cases:
        #  1. Leaf - no comment; name=AN#
        #       Add node child.name to graph
        #  2. Internal - AN# in comment; name not set; no species name in comment
        #       Parse ID from comment; set name=AN#; Add node child.name to graph
        #  3. Internal - AN# in comment; name not set; species name in comment
        #       Parse ID and species from comment; set name=AN#; Add node child.name to graph; Add node
        #       property of species
        species, id = extract_clade_name(clade.comment)
        if clade.name is None:
            clade.name = id
        if clade.name == "":
            clade.name = species
        if clade.name not in self.graph.nodes():
            self.graph.add_node(clade.name)
        if species:
            self.graph.nodes[clade.name]["species"] = species

    def extract_leaf_ids(self, tree_file):
        with open(tree_file) as tf:
            tf.readline()  # ignore first line, it's parsed already
            for l in tf.readlines():
                an_id, long_id = l.split(":", maxsplit=1)
                long_id = long_id.rstrip().rstrip(";")
                if an_id in self.graph:
                    self.graph.nodes[an_id]["long_id"] = long_id

    def extract_node_properties(self, node_dat_file: NodeDatFile):
        for entry in node_dat_file:
            family_name, an_id = entry.an_id.split(":", maxsplit=1)
            if self.name == family_name and an_id in self.graph:
                self.ptn_to_an[entry.ptn] = an_id
                self.an_to_ptn[an_id] = entry.ptn
                self.graph.nodes[an_id]["ptn"] = entry.ptn
                self.graph.nodes[an_id]["node_type"] = entry.node_type
                # event_type?
                # branch_length?

    def get_sf_for_an(self, an_id):
        if an_id in self.an_to_sf:
            return self.an_to_sf[an_id]
        else:
            parents = self.parents(an_id.split(":", maxsplit=1)[1])
            if parents:
                parent_an_id = "{}:{}".format(self.name, parents[0])  # Assuming always only one parent
                self.an_to_sf[parent_an_id] = self.get_sf_for_an(parent_an_id)
                return self.an_to_sf[parent_an_id]

    def extract_sf_assignments(self, an_to_sf_seed: Dict):
        self.an_to_sf = an_to_sf_seed

        for n in self.graph.nodes():
            full_an_id = "{}:{}".format(self.name, n)
            if full_an_id not in self.an_to_sf:
                self.an_to_sf[full_an_id] = self.get_sf_for_an(full_an_id)

    @staticmethod
    def parse(tree_file: str, tree_name: str = None, node_file: NodeDatFile = None):
        pthr_tree_graph = PantherTreeGraph(tree_name)

        # Parse Newick line
        phylo = PantherTreePhylo(tree_file)
        pthr_tree_graph.init_from_phylo(phylo)
        # Fill in long IDs on leaf nodes
        pthr_tree_graph.extract_leaf_ids(tree_file)
        # Fill in PTNs if node_file specified
        if node_file:
            pthr_tree_graph.extract_node_properties(node_file)

        return pthr_tree_graph

    def init_from_phylo(self, phylo: PantherTreePhylo):
        self.phylo: PantherTreePhylo = phylo
        # Fill networkx graph from Phylo obj
        self.add_children(phylo.tree.clade)

    def write(self, outpath):
        transformed_tree = copy.deepcopy(self.phylo.tree)
        self.traverse(transformed_tree.clade)
        Phylo.write(transformed_tree, outpath, 'newick')

    def traverse(self, c, parent_species=None):
        species, nid = extract_clade_name(c.comment)
        if nid == "":
            # Likely a leaf node
            cn = self.node(c.name)
            long_id = cn.get("long_id")
            species = long_id.split("|")[0]
            nid = long_id.split("|")[2].split("=")[1]
            if species == "":
                species = parent_species
            c.name = self.newick_name_fmt(species, nid)
        else:
            c.name = "1"
        # Transform event type values ("0>1" -> "S", "1>0" -> "D")
        if c.comment:
            # &&NHX:Ev=0>1:S=Amoebozoa:ID=AN7
            new_comment_elements = ["&&NHX"]
            if "Ev=0>1" in c.comment:
                new_comment_elements.append("Ev=S")  # speciation
            elif "Ev=1>0" in c.comment:
                new_comment_elements.append("Ev=D")  # duplication
            elif "Ev=0>0" in c.comment:
                new_comment_elements.append("Ev=D")  # horizontal transfer, but pretend like it's duplication
            c.comment = ":".join(new_comment_elements)
        for child_clade in c.clades:
            self.traverse(child_clade, parent_species=species)

    def prune_species(self, taxon_list: List):
        """
        Process:
        1. Find all terminal leaf nodes having taxon (OS code format) NOT in taxon_list. Delete these.
        2. Starting from the terminal nodes, traverse up, deleting all parent nodes until reaching a node with >1 children.
        3. Stop traversing that path and move on to traversing up the next terminal node
        :param taxon_list: The List of OS codes ('5-letter' OSCODES. Ex: HUMAN, MOUSE, SCHPO) that will remain in tree
        after pruning list non-members
        """
        for leaf in self.leaves():
            long_id = self.node(leaf)["long_id"]
            species = long_id.split("|")[0]
            if species not in taxon_list:
                self.prune_up(leaf)

    @staticmethod
    def newick_name_fmt(species, nid):
        # Name formats
        # LUCA_AN0 (internal speciation)
        # SALTY_AN159 (internal duplication)
        # ENTHI_C4M9L1 (leaf)
        return "_".join([species, nid])

    def node(self, node):
        return self.graph.nodes.get(node)

    def root(self):
        for n in self.graph.nodes():
            # This criteria is asking to be abused
            if self.parents(n) == []:
                return n

    def ancestors(self, node, reflexive=False):
        nodes = list(networkx.ancestors(self.graph, node))
        if reflexive:
            nodes.append(node)
        return nodes

    def descendants(self, node, reflexive=False):
        nodes = list(networkx.descendants(self.graph, node))
        if reflexive:
            nodes.append(node)
        return nodes

    def parents(self, node):
        return list(self.graph.predecessors(node))

    def children(self, node):
        return list(self.graph.successors(node))

    def leaves(self, node=None):
        leaves = []
        if node is None:
            node = self.root()
        for n in self.descendants(node):
            if self.children(n):
                continue  # Has children so not a leaf
            leaves.append(n)
        return leaves

    def subgraph(self, nodes: List):
        return self.graph.subgraph(nodes).copy()

    def subtree(self, split_node):
        pthr_tree_graph = PantherTreeGraph(tree_name=self.name)
        pthr_tree_graph.graph = self.subgraph(
            self.descendants(split_node, reflexive=True)
        )
        return pthr_tree_graph

    def nodes_between(self, ancestor_node, descendant_node):
        descendants_of_anc = self.descendants(ancestor_node)
        ancestors_of_desc = self.ancestors(descendant_node)
        return list(set(descendants_of_anc) & set(ancestors_of_desc))

    def prune_up(self, node):
        """
        remove_node(node) and, if node.parent has multiple children, prune_up(node.parent)
        :param node:
        :return:
        """
        parents = self.parents(node)
        if len(parents) > 1:
            print("WARNING: Tree node {} has multiple parents:".format(node), parents)
        if len(self.children(node)) < 2:
            if parents:
                self.prune_up(parents[0])
            self.remove_node(node)

    def remove_node(self, node):
        # Here, we remove from both graph and phylo
        self.graph.remove_node(node)
        if len(self) == 0:
            # Nothing left to "prune" (.prune() below will break) so we are done here
            return
        if self.phylo.tree.find_any(node):
            self.phylo.tree.prune(node)

    def __len__(self):
        return len(self.graph)
