import networkx as nx
import geopy.distance
from networkx.drawing.nx_agraph import write_dot

G = nx.Graph()

locations = {
    "Melbourne University": (-37.798248386903616, 144.9609632686033),
    "Monash University": (-37.907144361086004, 145.13717270067085),
    "Swinburne University": (-37.820634057054306, 145.03683630636752),
    "RMIT University": (-37.80674215563578, 144.96438807402902),
    "Victoria University": (-37.79331726178111, 144.89875939620745),
    "KFC": (-37.86817774432651, 144.729787441064),
    "McDonalds": (-37.89468475952529, 144.7529148686743),
    "Oporto": (-37.83391390548008, 144.69030112965373),
    "Hungry Jacks": (-37.87556724886548, 144.6819279538855)
}

suburbs = {
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
    "Me": ["Werribee", "Computer Science", "RMIT University", "Quiet", "EDM", "McDonalds"],
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
    friendList = friends.keys()
    for friend in friendList:
        locations[friend] = suburbs[friends[friend][0]] # set location of friend to location of suburb

    locationList = list(locations.keys()) # make list of locations
    locationList2 = locationList.copy() # duplicate list so we can remove elements to prevent edge duplication
    for i in locationList:
        for j in locationList2:
            if not i == j:
                # add node distances
                # add 1m to prevent edgy from null coercing the 0 with it's javascript code
                G.add_edge(i, j, weight=round(geopy.distance.distance(locations[i],locations[j]).km+0.001,3)) # round to nearest metre to reduce lag
        locationList2.remove(i) # prevent edge duplication

    for friend in friendList:
        G.nodes[friend]["nodetype"] = "friend"
        G.nodes[friend]["course"] = friends[friend][1]
        G.nodes[friend]["university"] = friends[friend][2]
        G.nodes[friend]["conversation"] = friends[friend][3]
        G.nodes[friend]["music"] = friends[friend][4]
        G.nodes[friend]["fastfood"] = friends[friend][5]

    uniList = ["Melbourne University", "Monash University", "Swinburne University", "RMIT University", "Victoria University"]
    for uni in uniList:
        G.nodes[uni]["nodetype"] = "university"
        G.nodes[uni]["shape"] = "circle"
        G.nodes[uni]["color"] = "red"
        G.nodes[uni]["course"] = "None"
        G.nodes[uni]["university"] = "None"
        G.nodes[uni]["conversation"] = "None"
        G.nodes[uni]["music"] = "None"
        G.nodes[uni]["fastfood"] = "None"

    restaurantList = ["KFC", "McDonalds", "Oporto", "Hungry Jacks"]
    for restaurant in restaurantList:
        G.nodes[restaurant]["nodetype"] = "fastfood"
        G.nodes[restaurant]['color'] = "pink"
        G.nodes[restaurant]["course"] = "None"
        G.nodes[restaurant]["university"] = "None"
        G.nodes[restaurant]["conversation"] = "None"
        G.nodes[restaurant]["music"] = "None"
        G.nodes[restaurant]["fastfood"] = "None"

make_graph()
write_dot(G, "finalalgograph.dot")
print('done')