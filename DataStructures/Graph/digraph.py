from DataStructures.Graph import vertex as vx
from DataStructures.Graph import edge as eg
from DataStructures.Map import map_linear_probing as lp
from DataStructures.List import array_list as al
def new_graph(order):
    capacidad = max(11,order)
    grafo = {
        "vertices": lp.new_map(capacidad,0.5),
        "num_edges":0
    }
    return grafo


def insert_vertex(my_graph, key, value=None):
    if lp.contains(my_graph["vertices"], key):
        return my_graph
    vert = vx.new_vertex(key, value)
    my_graph["vertices"] = lp.put(my_graph["vertices"], key, vert)
    return my_graph


def contains_vertex(my_graph, key):
    return lp.contains(my_graph["vertices"], key)


def add_edge(my_graph, key_r, key_l, weight=0):
    origen = lp.get(my_graph["vertices"], key_r)
    if origen is None:
        origen = vx.new_vertex(key_r, None)
        my_graph["vertices"] = lp.put(my_graph["vertices"], key_r, origen)

    destino = lp.get(my_graph["vertices"], key_l)
    if destino is None:
        destino = vx.new_vertex(key_l, None)
        my_graph["vertices"] = lp.put(my_graph["vertices"], key_l, destino)
    existing_edge = vx.get_edge(origen, key_l)

    if existing_edge is None:
        vx.add_adjacent(origen, key_l, weight)
        my_graph["num_edges"] += 1
    else:
        eg.set_weight(existing_edge, weight)

    return my_graph

def order(my_graph):
    return lp.size(my_graph["vertices"])
def size(my_graph):
    return my_graph["num_edges"]

def degree(my_graph, key):
    vertex = lp.get(my_graph["vertices"], key)
    if vertex is None:
        return 0
    return vx.degree(vertex)

def adjacents(my_graph, key):
    vertex = lp.get(my_graph["vertices"], key)
    if vertex is None:
        return al.new_list()

    adj_map = vx.get_adjacents(vertex)  
    return lp.key_set(adj_map)

def vertices(my_graph):
    return lp.key_set(my_graph["vertices"])

def edges_vertex(my_graph, key):
    vertex = lp.get(my_graph["vertices"], key)
    if vertex is None:
        return al.new_list()

    adj_map = vx.get_adjacents(vertex)
    return lp.value_set(adj_map)

def get_vertex(my_graph, key):
    return lp.get(my_graph["vertices"], key)

def update_vertex_info(my_graph, key, new_value):
    vertex = lp.get(my_graph["vertices"], key)
    if vertex is None:
        return my_graph

    vx.set_value(vertex, new_value)
    return my_graph

def get_vertex_information(my_graph, key):
    vertex = lp.get(my_graph["vertices"], key)
    if vertex is None:
        return None
    return vx.get_value(vertex)