from DataStructures.Map import map_linear_probing as mp
from DataStructures.Priority_queue import priority_queue as pq
from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as sl
from DataStructures.Graph import digraph as G
from math import inf

# ---------------------------------------------------------
#     ESTRUCTURA DE DIJKSTRA (ya la tienes)
# ---------------------------------------------------------

def new_dijsktra_structure(source, g_order):
    structure = {
        "source": source,
        "visited": mp.new_map(g_order, 0.5),
        "pq": pq.new_heap(is_min_pq=True)
    }
    return structure


# ---------------------------------------------------------
#     FUNCIÓN PRINCIPAL DIJKSTRA
# ---------------------------------------------------------

def dijkstra(my_graph, source):

    structure = new_dijsktra_structure(source, G.order(my_graph))

    # Inicialización
    mp.put(structure["visited"], source,
           {"marked": True, "edge_from": None, "dist_to": 0})

    pq.insert(structure["pq"], 0, source)

    # ---- LOOP PRINCIPAL ----
    while not pq.is_empty(structure["pq"]):

        v = pq.remove(structure["pq"])  # vértice con menor distancia

        dist_v = mp.get(structure["visited"], v)["dist_to"]

        # Obtener aristas salientes de v
        edges = G.edges_vertex(my_graph, v)

        for i in range(al.size(edges)):
            edge = al.get_element(edges, i)
            w = edge["to"]
            weight = edge["weight"]

            # distancia propuesta
            new_dist = dist_v + weight

            info_w = mp.get(structure["visited"], w)

            # Caso: w NO está en visited
            if info_w is None:
                mp.put(structure["visited"], w,
                       {"marked": True, "edge_from": v, "dist_to": new_dist})
                pq.insert(structure["pq"], new_dist, w)

            else:
                # Caso: ya existe pero encontramos mejor camino
                if new_dist < info_w["dist_to"]:
                    info_w["dist_to"] = new_dist
                    info_w["edge_from"] = v

                    # actualizar prioridad en la cola
                    pq.improve_priority(structure["pq"], w, new_dist)

    return structure


# ---------------------------------------------------------
#     CONSULTA dist_to
# ---------------------------------------------------------

def dist_to(vertex, structure):
    info = mp.get(structure["visited"], vertex)
    if info is None:
        return inf
    return info["dist_to"]


# ---------------------------------------------------------
#     CONSULTA has_path_to
# ---------------------------------------------------------

def has_path_to(vertex, structure):
    return mp.contains(structure["visited"], vertex)


# ---------------------------------------------------------
#     CONSULTA path_to
# ---------------------------------------------------------

def path_to(vertex, structure):
    if not has_path_to(vertex, structure):
        return None

    path = sl.new_list()
    current = vertex

    while current is not None:
        sl.add_first(path, current)
        info = mp.get(structure["visited"], current)
        current = info["edge_from"]

    return path
