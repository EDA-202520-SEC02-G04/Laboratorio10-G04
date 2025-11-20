from DataStructures.Map import map_entry as map
from DataStructures.Graph import digraph as G
def bfs(graph, source):

    visited_ht = map.new_map(num_elements=G.order(graph), load_factor=0.5)
    bfs_vertex(graph, source, visited_ht)
    return visited_ht
def bfs_vertex(graph, source, visited_ht):
    pass
def has_path_to(vertex, visited_ht):
    pass
def path_to(vertex, visited_ht):
    pass