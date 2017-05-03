import itertools

import json


def calculate_length(path, graph):
    result = 0.0
    for i in range(0, len(path) - 1):
        start_vertex = path[i]
        end_vertex = path[i + 1]
        result += graph[start_vertex][end_vertex]
    return result


if __name__ == '__main__':
    with open('data.json') as data_file:
        graph = json.load(data_file)['graph']

    count_of_vertices = len(graph)
    vertices = [
        i for i in range(0, count_of_vertices)
    ]

    pathes = [
        path + (path[0],) for path in itertools.permutations(vertices)
    ]

    lengths = {
        path: calculate_length(path, graph) for path in pathes
    }

    best_length = min(lengths.values())

    best_pathes = [
        path for path in filter(
            lambda path: lengths[path] == best_length,
            pathes
        )
    ]

    with open('result.json', mode='wt') as result_file:
        json.dump(
            obj={
                'best_length': best_length,
                'best_pathes': best_pathes
            },
            fp=result_file,
            indent=2,
            sort_keys=True
        )
