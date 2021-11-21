def parse_cdp_neighbors(command_output: str) -> dict:
    hostname = []
    parser_dict = {}
    for line in command_output.split('\n'):
        columns = line.split()
        if ">" in line:
            hostname = line.split(">")[0]
        elif len(columns) >= 5 and columns[3].isdigit():
            r_router, t_intf_l, n_intf_l, *other, t_intf_r, n_intf_r = columns
            parser_dict[hostname, t_intf_l + n_intf_l] = (r_router, t_intf_r + n_intf_r)
    return parser_dict


def create_network_map(filenames: list) -> dict:
    dict_back = {}
    for file in filenames:
        dict_parse = parse_cdp_neighbors(file.read().decode("utf-8"))
        dict_back.update(dict_parse)
    return dict_back


def unique_network_map(topology_dict: dict) -> dict:
    network_map = {}
    for key, value in topology_dict.items():
        key, value = sorted([key, value])
        network_map[key] = value
    return network_map
