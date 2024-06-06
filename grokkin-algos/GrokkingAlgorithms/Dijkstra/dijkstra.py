import math

graph = {}
graph["START"] = {"A": 6, "B": 2}
graph["A"] = {"FIN": 1}
graph["B"] = {"A": 3, "FIN": 5}
graph["FIN"] = {}

# How long it takes to get to each of the nodes from the starting point
costs = {}
costs["A"] = 6
costs["B"] = 2
costs["FIN"] = math.inf

parents = {}
parents["A"] = "START"
parents["B"] = "START"
parents["FIN"] = None

processed = []

def find_lowest_cost_node(costs):
    lowest_cost = math.inf
    lowest_cost_node = None
    for node, cost in costs.items():
        if cost < lowest_cost:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

node = find_lowest_cost_node(costs)
while node is not None:
    cost = costs[node]
    # Distances from the current node to the close nodes
    neighbors = graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.append(node)
    node = find_lowest_cost_node(costs)

