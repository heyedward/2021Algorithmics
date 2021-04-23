import networkx as nx
import matplotlib.pyplot as plt
from random import randint
from math import inf

G=nx.Graph()

def make_nodes():
    # node list
    nodes = ["Melbourne University", "Monash University", "Swinburne University", "RMIT University", "Victoria University", "My house"]
    n2 = nodes.copy()

    # add nodes
    for i in nodes:
        for j in n2:
            if not i == j:
                G.add_edge(i, j, weight=randint(1,10))
        n2.pop(0)

make_nodes()
uni = input("Select a University: ")

def say_friends():
    friends = {"Raida": ["Computer Science", "Melbourne University"], "Yuktha": ["Law", "Monash University"], "Phuong": ["Engineering", "Monash University"], "Levan": ["Science", "Melbourne University"]}

    keys = list(friends.keys())
    print("The friends you have to pick up are:")

    dest = []
    for i in range(3):
        loc = randint(0,len(keys)-1)
        name = keys[loc]
        keys.pop(loc)
        print(f"{name} studying {friends[name][0]} in {friends[name][1]}")
        dest.append(friends[name][1]) # append university
    return dest

def dijkstra():
    nx.set_node_attributes(G, inf, "dist")
    G.nodes["My house"]["dist"] = 0
    nx.set_node_attributes(G, None, "prev")

    unvisited = [node for node in G.nodes]

    while unvisited:
        current = min([(G.nodes[node]["dist"],node) for node in unvisited],key=lambda t: t[0])[1]
        unvisited.remove(current)

        edges = G.edges(current)
        for edge in edges:
            newdist = G.nodes[current]['dist'] + G.edges[edge]['weight']
            if newdist < G.nodes[edge[1]]['dist']:
                G.nodes[edge[1]]['dist'] = newdist
                G.nodes[edge[1]]['prev'] = current

dijkstra()

dests = say_friends()

# color map for nodes
color_map = []
for node in G:
    if node in dests:
        color_map.append('red')
    elif node == "My house":
        color_map.append('red')
    else:
        color_map.append('blue')

# render
pos = nx.spring_layout(G)
labels = nx.get_node_attributes(G, 'dist')
nx.draw(G, pos, node_color=color_map, labels=labels, with_labels=True)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
plt.show()
