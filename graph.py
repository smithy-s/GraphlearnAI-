
import networkx as nx
from data import SKILLS, PREREQUISITES


# --------------------------------------------------
# CREATE KNOWLEDGE GRAPH
# --------------------------------------------------

def create_graph():
    graph = nx.Graph()

    # Add all available skills
    graph.add_nodes_from(SKILLS)

    # Validate and add prerequisite connections
    for item in PREREQUISITES:
        if not isinstance(item, (tuple, list)) or len(item) != 2:
            raise ValueError(
                f"Invalid prerequisite entry: {item!r}. "
                "Each entry must contain exactly two skill names."
            )

        prerequisite, skill = item

        if prerequisite not in SKILLS:
            raise ValueError(
                f"Unknown prerequisite skill: {prerequisite}"
            )

        if skill not in SKILLS:
            raise ValueError(
                f"Unknown target skill in prerequisites: {skill}"
            )

        graph.add_edge(prerequisite, skill)

    return graph


# --------------------------------------------------
# GENERATE LEARNING PATH
# --------------------------------------------------

def generate_learning_path(current_skill, target_skill):
    graph = create_graph()

    if current_skill not in graph:
        return []

    if target_skill not in graph:
        return []

    if current_skill == target_skill:
        return [current_skill]

    try:
        return nx.shortest_path(
            graph,
            source=current_skill,
            target=target_skill
        )

    except nx.NetworkXNoPath:
        return []

    except nx.NodeNotFound:
        return []