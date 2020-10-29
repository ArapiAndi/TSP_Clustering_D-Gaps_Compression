from __future__ import print_function

import numpy
from ortools.constraint_solver import routing_enums_pb2
from ortools.constraint_solver import pywrapcp
from src.Clustering import distance_jaccard

START = 0

def find_centrality_medoid(graph_matrix):
    k, j_max, j = 0, 1, 0
    n = len(graph_matrix)
    for i in range(n):
        j += sum(graph_matrix[i, :])

        if j < j_max:
            j_max = j
            k = i
        j = 0
    return k


def create_graph_matrix(medoids):
    n = len(medoids)
    graph_matrix = numpy.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if not i == j:
                graph_matrix[j][i] = distance_jaccard((medoids[i])[1], (medoids[j])[1])
                graph_matrix[i][j] = graph_matrix[j][i]
    return graph_matrix


def create_data_model(graph_matrix):
    """Stores the data for the problem."""
    data = {}
    data['distance_matrix'] = graph_matrix
    data['num_vehicles'] = 1
    START = find_centrality_medoid(graph_matrix)
    data['depot'] = START
    return data


def get_routing(manager, routing, solution):
    """Prints solution on console."""
    rout = []
    index = routing.Start(START)
    while not routing.IsEnd(index):
        rout.append(manager.IndexToNode(index))
        index = solution.Value(routing.NextVar(index))
    return rout


def call_TSP(medoids):
    """Entry point of the program."""
    # Instantiate the data problem.
    data = create_data_model(create_graph_matrix(medoids))

    # Create the routing index manager.
    manager = pywrapcp.RoutingIndexManager(len(data['distance_matrix']),
                                           data['num_vehicles'], data['depot'])

    # Create Routing Model.
    routing = pywrapcp.RoutingModel(manager)

    def distance_callback(from_index, to_index):
        """Returns the distance between the two nodes."""
        # Convert from routing variable Index to distance matrix NodeIndex.
        from_node = manager.IndexToNode(from_index)
        to_node = manager.IndexToNode(to_index)
        return data['distance_matrix'][from_node][to_node]

    transit_callback_index = routing.RegisterTransitCallback(distance_callback)

    # Define cost of each arc.
    routing.SetArcCostEvaluatorOfAllVehicles(transit_callback_index)

    # Setting first solution heuristic.
    search_parameters = pywrapcp.DefaultRoutingSearchParameters()
    search_parameters.first_solution_strategy = (
        routing_enums_pb2.FirstSolutionStrategy.PATH_CHEAPEST_ARC)

    # Solve the problem.
    solution = routing.SolveWithParameters(search_parameters)

    # get solution on console.
    if solution:
        return get_routing(manager, routing, solution)
