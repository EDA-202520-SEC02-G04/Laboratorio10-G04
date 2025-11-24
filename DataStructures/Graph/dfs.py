from DataStructures.Graph import vertex as vx
from DataStructures.Graph import edge as eg
from DataStructures.Map import map_linear_probing as lp
from DataStructures.List import array_list as al
from DataStructures.Graph import digraph as G


def dfs(graph, source):
    visited = lp.new_map(G.order(graph), 0.5)

    def explore(v):
        adj_list = G.adjacents(graph, v)

        for i in range(al.size(adj_list)):
            w = al.get_element(adj_list, i)

            if lp.get(visited, w) is None:
                lp.put(visited, w, {"marked": True, "edgeTo": v})
                explore(w)

    lp.put(visited, source, {"marked": True, "edgeTo": None})
    explore(source)

    return visited


def dfs_vertex(search, graph, vertex):
    adjlst = G.adjacents(graph, vertex)
    for w in range(al.size(adjlst)):
        visited = lp.get(search['visited'], w)
        if visited is None:
            lp.put(search['visited'],
                        w, {'marked': True, 'edgeTo': vertex})
            dfs_vertex(search, graph, w)
    return search

