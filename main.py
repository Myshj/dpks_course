from math import inf

from numpy import matrix, full

import json


def dijkstra(
        graph: matrix,
        source: int,
        destination: int,
):
    shape = graph.shape
    unknown_vertices = set(range(0, shape[0]))
    distances = full(shape[0], inf)
    previous = full(shape[0], -1)

    distances[source] = 0

    while len(unknown_vertices) != 0:
        min_distance = inf
        current_best_vertex = None
        for vertex in unknown_vertices:
            if distances[vertex] <= min_distance:
                min_distance = distances[vertex]
                current_best_vertex = vertex

        if current_best_vertex == destination:
            sequence = []
            while previous[current_best_vertex] != -1:
                sequence.append(current_best_vertex)
                current_best_vertex = previous[current_best_vertex]

            sequence.append(current_best_vertex)
            sequence.reverse()
            return sequence, min_distance

        unknown_vertices.remove(current_best_vertex)

        for vertex in unknown_vertices:
            alt = distances[current_best_vertex] + graph[current_best_vertex, vertex]
            if alt < distances[vertex]:
                distances[vertex] = alt
                previous[vertex] = current_best_vertex


if __name__ == '__main__':
    result = []
    for i in range(0, N):
        for j in range(0, N):
            r = dijkstra(graph, i, j)
            l = [
                int(v) for v in r[0]
            ]
            result.append({
                'source': i,
                'destination': j,
                'sequence': l,
                'weight': float(r[1])
            })

    with open('result.json', mode='w') as result_file:
        json.dump(result, result_file, sort_keys=True, indent=4)