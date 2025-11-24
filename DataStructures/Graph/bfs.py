from DataStructures.Map import map_linear_probing as map
from DataStructures.Graph import digraph as G
from DataStructures.List import array_list as al


def bfs(graph, source):

    visited_ht = map.new_map(
        num_elements=G.order(graph),
        load_factor=0.5
    )

    bfs_vertex(graph, source, visited_ht)
    return visited_ht


def bfs_vertex(graph, source, visited_ht):
    """
    BFS usando array_list como cola
    """
    queue = al.new_list()
    al.add_last(queue, source)

    map.put(visited_ht, source, {
        "marked": True,
        "edge_to": None,
        "dist": 0
    })

    index = 0
    while index < al.size(queue):
        v = al.get_element(queue, index)
        index += 1

        info_v = map.get(visited_ht, v)
        dist_v = info_v["dist"]

        adj = G.adjacents(graph, v)

        for i in range(al.size(adj)):
            w = al.get_element(adj, i)

            if not map.contains(visited_ht, w):
                map.put(visited_ht, w, {
                    "marked": True,
                    "edge_to": v,
                    "dist": dist_v + 1
                })
                al.add_last(queue, w)


def has_path_to(vertex, visited_ht):
    return map.contains(visited_ht, vertex)


def path_to(vertex, visited_ht):
    if not has_path_to(vertex, visited_ht):
        return None

    path = al.new_list()
    current = vertex

    while current is not None:
        al.add_last(path, current)
        info = map.get(visited_ht, current)
        current = info["edge_to"]

    path = reverse_array_list(path)
    return path


def reverse_array_list(lst):
    new = al.new_list()
    for i in range(al.size(lst)-1, -1, -1):
        al.add_last(new, al.get_element(lst, i))
    return new
