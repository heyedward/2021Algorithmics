import networkx as nx
import matplotlib.pyplot as plt
from random import randint
from math import inf
import geopy.distance

G=nx.Graph()

def make_nodes():
    # node list
    locations = {
        "Melbourne University": (-37.798248386903616, 144.9609632686033),
        "Monash University": (-37.907144361086004, 145.13717270067085),
        "Swinburne University": (-37.820634057054306, 145.03683630636752),
        "RMIT University": (-37.80674215563578, 144.96438807402902),
        "Victoria University": (-37.79331726178111, 144.89875939620745),
        "KFC": (-37.86817774432651, 144.729787441064),
        "McDonald's": (-37.89468475952529, 144.7529148686743),
        "Oporto": (-37.83391390548008, 144.69030112965373),
        "Hungry Jacks": (-37.87556724886548, 144.6819279538855),
        "Werribee": (-37.89869509112579, 144.66345105480698),
        "Point Cook": (-37.918329529191574, 144.74669353277324),
        "Hoppers Crossing": (-37.86233985503369, 144.68476425340285),
        "Burnside": (-37.753250721869605, 144.75228098106768),
        "Tarneit": (-37.808604569947896, 144.66686217407914),
        "Manor Lakes": (-37.8736488572485, 144.58036378564364),
        "Gladstone Park": (-37.69183386250476, 144.89449104693733),
        "Wollert": (-37.60740317084443, 145.03031352102934),
        "Reservior": (-37.71298544191029, 145.0060242796427),
        "Altona North": (-37.83764214052825, 144.84601862975424)
    }

    # add nodes
    for i in locations.keys():
        for j in locations.keys():
            if not i == j:
                G.add_edge(i, j, weight=geopy.distance.distance(locations[i],locations[j]).km)

    friends = {
        "Me": ["Werribee"],
        "Aaryan": ["Werribee"],
        "James": ["Point Cook"],
        "Yuktha": ["Point Cook"],
        "Andy": ["Point Cook"],
        "Prabhas": ["Point Cook"],
        "Jay": ["Hoppers Crossing"],
        "Akira": ["Burnside"],
        "Tarneit": ["Nathan"],
        "Manor Lakes": ["Angna"],
        "Gladstone Park": ["Yaseen"],
        "Wollert": ["Alex"],
        "Reservior": ["Nicky"],
        "Altona North": ["Lina"]
    }

    for i in friends.keys():
        for j in friends[i]:
            G.add_edge(j, i, weight=0)

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
    G.nodes["Werribee"]["dist"] = 0
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
    elif node == "Werribee":
        color_map.append('red')
    else:
        color_map.append('blue')

# render
pos = nx.random_layout(G)
#labels = nx.get_node_attributes(G, 'dist')
nx.draw(G, pos, node_color=color_map, with_labels=True)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
plt.show()
