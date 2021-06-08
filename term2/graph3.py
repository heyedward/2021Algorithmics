import networkx as nx
import matplotlib.pyplot as plt
from random import randint
from math import inf
import googlemaps
import geopy.distance

G = nx.Graph()

#API_key = 'AIzaSyCXUaUUui1aABbpsfuDh83HQ-NqioG0MzU'
#gmaps = googlemaps.Client(key=API_key)

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

friends = {
    "Me": ["Werribee", "Computer Science", "Monash University", "Quiet", "EDM"],
    "Aaryan": ["Werribee", "Mechatronics", "Melbourne University", "Quiet", "Hiphop"],
    "James": ["Point Cook", "Psychology", "N/A", "Talking", "Hiphop"],
    "Yuktha": ["Point Cook", "Law", "Melbourne University", "Quiet", "Pop"],
    "Alex": ["Wollert", "N/A", "Monash University", "Talking", "Rock"],
    "Prabhas": ["Point Cook", "Medicine", "Monash University", "Oporto", "Talking", "N/A"],
    "Jay": ["Hoppers Crossing", "Science", "Monash University", "Talking", "Rock"],
    "Akira": ["Burnside", "Commerce", "Melbourne University", "Quiet", "Video Game Music"],
    "Nathan": ["Tarneit", "N/A", "Melbourne University", "Quiet", "Pop"],
    "Angna": ["Manor Lakes", "Law", "Melbourne University", "Quiet", "R&B"],
    "Yaseen": ["Gladstone Park", "N/A", "Melbourne University", "Talking", "Hiphop"],
    "Nicky": ["Reservior", "Computer Science", "RMIT", "Quiet", "Rock"],
    "Lina": ["Altona North", "Psychology", "Melbourne University", "Quiet", "Rock"],
    "Nehchal": ["Manor Lakes", "Equine Studies", "Monash University", "Quiet", "Hiphop"],
    "Raaif": ["Manor Lakes", "Medicine", "Monash University", "Quiet", "EDM"],
    "Cindy": ["Point Cook", "Law", "Monash University", "Quiet", "Rock"],
    "Ryan": ["Tarneit", "Science", "Monash University", "Quiet", "R&B"]
}

def make_graph():
    # add nodes
    keys = list(locations.keys()) # make list of locations
    keys2 = keys.copy() # duplicate list so we can remove elements to prevent edge duplication
    for i in keys:
        for j in keys2:
            if not i == j:
                G.add_edge(i, j, weight=round(0,2))
                #G.add_edge(i, j, weight=round(gmaps.distance_matrix(locations[i], locations[j], mode='driving')["rows"][0]["elements"][0]["distance"]["value"],2))
                G.add_edge(i, j, weight=round(geopy.distance.distance(locations[i],locations[j]).km,2)) # round to nearest 10m
        keys2.remove(i) # prevent edge duplication

    for i in friends.keys():
        G.add_edge(friends[i][0], i, weight=0) # add friends to suburbs with edge weight 0 (since they are in that suburb)
        G.nodes[i]["course"] = friends[i][1]
        G.nodes[i]["university"] = friends[i][2]
        G.nodes[i]["conversation"] = friends[i][3]
        G.nodes[i]["music"] = friends[i][4]

make_graph()
#uni = input("Select a University: ")

def say_friends():
    keys = list(friends.keys())
    print("The friends you have to pick up are:")

    dest = []
    # choosing random friends for now
    for i in range(3):
        loc = randint(0,len(keys)-1)
        name = keys[loc]
        keys.pop(loc)
        print(f"{name} studying {friends[name][1]} in {friends[name][2]}")
        dest.append(friends[name][1]) # append university
    return dest

def dijkstra():
    nx.set_node_attributes(G, inf, "dist")
    G.nodes["Me"]["dist"] = 0
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
# color_map = []
# for node in G:
#     if node in dests:
#         color_map.append('red')
#     elif node == "Me":
#         color_map.append('red')
#     else:
#         color_map.append('blue')

# render
pos = nx.random_layout(G)

#labels = nx.get_node_attributes(G, 'dist')

nx.draw(G, pos, with_labels=True)
nx.draw_networkx_nodes(G,pos,nodelist=["Melbourne University", "Monash University", "Swinburne University", "RMIT University", "Victoria University"],node_shape="s",node_color="red")
nx.draw_networkx_nodes(G,pos,nodelist=["KFC", "McDonald's", "Oporto", "Hungry Jacks"],node_color="pink")
nx.draw_networkx_nodes(G,pos,nodelist=["Werribee","Point Cook","Hoppers Crossing","Burnside","Tarneit","Manor Lakes","Gladstone Park","Wollert","Reservior","Altona North"],node_color="purple")
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
plt.show()