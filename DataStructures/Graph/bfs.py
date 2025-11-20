from DataStructures.Map import map_linear_probing as map
from DataStructures.Graph import digraph as G
from DataStructures.List import array_list as al
def bfs(graph, source):

    visited_ht = map.new_map(num_elements=G.order(graph), load_factor=0.5)
    bfs_vertex(graph, source, visited_ht)
    return visited_ht

def bfs_vertex(graph, source, visited_ht):
    cam = al.new_list()
    al.add_last(cam, source)
    
    map.put(visited_ht, source, {
        "marked": True,
        "edge_to": None,
        "dist": 0
    })

    a = 0
    while a < al.size(cam):
        v = al.get_element(cam, a)
        a += 1

        info_v = map.get(visited_ht, v)
        dist_v = info_v["dist"]

        adyacentes = G.adjacents(graph, v)

        for i in range(al.size(adyacentes)):
            w = al.get_element(adyacentes, i) 
            if not map.contains(visited_ht, w):
                map.put(visited_ht, w, {
                    "marked": True,
                    "edge_to": v,
                    "dist": dist_v + 1
                })
                al.add_last(cam, w)


def has_path_to(vertex, visited_ht):
    return map.contains(visited_ht, vertex)


def path_to(vertex, visited_ht):
    if not has_path_to(vertex, visited_ht):
        return None
    list = [] 
    current = vertex
    while current is not None:
        list.append(current)
        info = map.get(visited_ht, current)
        current = info["edge_to"]
    list.reverse()
    path_list = al.new_list()
    for key in list:
        al.add_last(path_list, key)

    return path_list