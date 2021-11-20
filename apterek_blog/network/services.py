from network.draw_network_graph import draw_topology
from datetime import datetime
from network.network_parser import unique_network_map, create_network_map


def create_topology_pict(filenames: list, user: str) -> None:
    path_topology_save = f"../media/network_topology/{user}/{datetime.now()}.png"
    draw_topology(unique_network_map(create_network_map(filenames)), path_topology_save)
