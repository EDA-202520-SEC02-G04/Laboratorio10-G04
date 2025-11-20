from DataStructures.Graph import vertex as vx
from DataStructures.Graph import edge as eg
from DataStructures.Map import map_linear_probing as lp
from DataStructures.List import array_list as al
from DataStructures.Graph import digraph as g

def dfs(graph, source):
    visited_ht = lp.new_map(num_elements=g.order(graph), load_factor=0.5 )
    lp.put(visited_ht, source, {'marked': True, 'edge_from': None})
    dfs_vertex(graph, source, visited_ht)
    return visited_ht

def dfs_vertex(search, graph, vertex):
    adjlst = g.adjacents(graph, vertex)
    for w in range(al.size(adjlst)):
        visited = lp.get(search['visited'], w)
        if visited is None:
            lp.put(search['visited'],
                        w, {'marked': True, 'edgeTo': vertex})
            dfs_vertex(search, graph, w)
    return search

