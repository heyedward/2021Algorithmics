import networkx as nx
import matplotlib.pyplot as plt
from random import randint
from math import inf
import geopy.distance

G = nx.Graph()

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

# survey results (invalid or unsure responses set to N/A)
friends = {
    "Me": ["Werribee"],
    "Aaryan": ["Werribee", "Mechatronics", "Melbourne University", "Quiet", "Hiphop", "Hungry Jacks"],
    "James": ["Point Cook", "Psychology", "N/A", "Talking", "Hiphop", "KFC"],
    "Yuktha": ["Point Cook", "Law", "Melbourne University", "Quiet", "Pop", "Hungry Jacks"],
    "Alex": ["Wollert", "N/A", "Monash University", "Talking", "Rock", "McDonalds"],
    "Prabhas": ["Point Cook", "Medicine", "Monash University", "Talking", "N/A", "Oporto"],
    "Jay": ["Hoppers Crossing", "Science", "Monash University", "Talking", "Rock", "Hungry Jacks"],
    "Akira": ["Burnside", "Commerce", "Melbourne University", "Quiet", "Video Game Music", "KFC"],
    "Nathan": ["Tarneit", "N/A", "Melbourne University", "Quiet", "Pop", "KFC"],
    "Angna": ["Manor Lakes", "Law", "Melbourne University", "Quiet", "R&B", "Hungry Jacks"],
    "Yaseen": ["Gladstone Park", "N/A", "Melbourne University", "Talking", "Hiphop", "KFC"],
    "Nicky": ["Reservior", "Computer Science", "RMIT University", "Quiet", "Rock", "N/A"],
    "Lina": ["Altona North", "Psychology", "Melbourne University", "Quiet", "Rock", "KFC"],
    "Nehchal": ["Manor Lakes", "Equine Studies", "Monash University", "Quiet", "Hiphop", "N/A"],
    "Raaif": ["Manor Lakes", "Medicine", "Monash University", "Quiet", "EDM", "McDonalds"],
    "Cindy": ["Point Cook", "Law", "Monash University", "Quiet", "Rock", "Hungry Jacks"],
    "Ryan": ["Tarneit", "Science", "Monash University", "Quiet", "R&B", "McDonalds"]
}

def make_graph():
    ''' add the nodes and edges to the graph '''
    keys = list(locations.keys()) # make list of locations
    keys2 = keys.copy() # duplicate list so we can remove elements to prevent edge duplication
    for i in keys:
        for j in keys2:
            if not i == j:
                # add node distances
                G.add_edge(i, j, weight=round(geopy.distance.distance(locations[i],locations[j]).km,2)) # round to nearest 10m
        keys2.remove(i) # prevent edge duplication

    for i in friends.keys():
        G.add_edge(friends[i][0], i, weight=0) # add friends to suburbs with edge weight 0 (since they are in that suburb)
        # add preferences as node attributes
        if i == "Me":
            continue # i don't have attributes
        G.nodes[i]["course"] = friends[i][1]
        G.nodes[i]["university"] = friends[i][2]
        G.nodes[i]["conversation"] = friends[i][3]
        G.nodes[i]["music"] = friends[i][4]
        G.nodes[i]["restaurant"] = friends[i][5]

make_graph()

# print 3 random friends (I'll make the algorithm for choosing them later maybe with graph partitioning or something)
def say_friends():
    uni = input("Pick a university: ")
    keys = list(friends.keys())
    keys.remove("Me")
    print("The friends you have to pick up are:")

    dest = []
    # choosing random friends for now
    for i in range(3):
        loc = randint(0,len(keys)-1)
        name = keys[loc]
        keys.pop(loc)
        print(f"{name} studying {friends[name][1]} in {friends[name][2]}")
        university = friends[name][2]
        if not friends[name][2] in dest:
            dest.append(friends[name][2]) # append university
        if not friends[name][5] in dest:
            dest.append(friends[name][5])
        dest.append(name) # add friend
    return dest

nx.set_edge_attributes(G, False, "red") # by default edges are not colored

def dijkstra(start, dest):
    ''' Dijkstra's algorithm on networkx '''
    nx.set_node_attributes(G, inf, "dist")
    G.nodes[start]["dist"] = 0
    nx.set_node_attributes(G, None, "prev")

    unvisited = list(G.nodes)#[node for node in G.nodes]

    while unvisited:
        current = min([(G.nodes[node]["dist"],node) for node in unvisited],key=lambda t: t[0])[1]
        unvisited.remove(current)

        if current == dest:
            break

        edges = G.edges(current)
        for edge in edges:
            newdist = G.nodes[current]['dist'] + G.edges[edge]['weight']
            if newdist < G.nodes[edge[1]]['dist']:
                G.nodes[edge[1]]['dist'] = newdist
                G.nodes[edge[1]]['prev'] = current
    
    lst = []
    weight = 0
    d = dest
    lst.append(start)
    while True:
        prev = G.nodes[d]['prev']
        lst.append(prev)
        G.edges[(d,prev)]['red'] = True
        weight = weight + G.edges[(d,prev)]['weight']
        if prev == start:
            break
        else:
            d = prev
    return lst,weight

dests = say_friends()

start = "Me"
total_weight = 0
path = []
for i in dests:
    if not i == "N/A":
        end = i
        print(end)
        lst,w = dijkstra(start, end)
        print(lst)
        path = path + lst
        total_weight = total_weight + w
        start = i

print(f"Total Path Weight: {total_weight}km")
for i in range(len(path)-1):
    print(f"{path[i]}->{path[i+1]}")

# color map for nodes
# color_map = []
# for node in G:
#     if node in dests:
#         color_map.append('red')
#     elif node == "Me":
#         color_map.append('red')
#     else:
#         color_map.append('blue')

edge_colors = ['red' if G.edges[e]['red'] else 'black' for e in G.edges]
edge_widths = [4 if G.edges[e]['red'] else 1 for e in G.edges]

# render
pos = nx.random_layout(G)

#labels = nx.get_node_attributes(G, 'dist')

nx.draw(G, pos, edge_color=edge_colors, width=edge_widths, with_labels=True)
nx.draw_networkx_nodes(G,pos,nodelist=["Melbourne University", "Monash University", "Swinburne University", "RMIT University", "Victoria University"],node_shape="s",node_color="red")
nx.draw_networkx_nodes(G,pos,nodelist=["KFC", "McDonald's", "Oporto", "Hungry Jacks"],node_color="pink")
nx.draw_networkx_nodes(G,pos,nodelist=["Werribee","Point Cook","Hoppers Crossing","Burnside","Tarneit","Manor Lakes","Gladstone Park","Wollert","Reservior","Altona North"],node_color="purple")
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
plt.show()