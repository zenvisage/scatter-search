import numpy as np
import matplotlib.path as mplPath


def naive_algorithm(polygons, candidates_info, dataset, options):
    """

    :param polygons: {points: [[x1,y1],[x2,y2],...], type:'green'}
    :param candidates_info: {'CandidateA':numOfOccurrencesInDataset, 'CandidateB'...}
    :param dataset: As described in loadSaveDataset.py
    :param options: {algorithm: string, xAxis: index, yAxis: index, zAxis: index}
    :return: Must return full dictionaries (same format as dataset) for the top k candidates
    """
    x = options['xAxis']
    y = options['yAxis']
    z = options['zAxis']
    data = dataset['data']
    total_points_array = []
    for polygon in polygons:
        points = np.array(polygon['points'])
        path = mplPath.Path(points)
        total_points = 0
        for row in data:
            point = [row[x], row[y]]
            if path.contains_point(point):
                total_points += 1
        total_points_array.append(total_points)
    return {'algorithm': 'Naive Algorithm', 'total_points_array': total_points_array}


def complex_algorithm(polygons, candidates_info, dataset, options):
    """

    :param polygons:
    :param candidates_info:
    :param dataset:
    :param options:
    :return:
    """
    return {'algorithm': 'Complex Algorithm'}



EXISTING_ALGORITHMS = {
    'Naive Algorithm': naive_algorithm,
    'Complex Algorithm': complex_algorithm
}


def get_candidates_info(dataset, zAxis):
    """
    Returns a map of the candidate value and its occurrences in the dataset
    :param dataset: Same as described in loadSaveDataset.py
    :param zAxis: Candidates are split based on this column
    :return:
    """
    dictOfCandidates = dict()
    for row in dataset:
        candidate = row[zAxis]
        if candidate in dictOfCandidates:
            dictOfCandidates[candidate] += 1
        else:
            dictOfCandidates[candidate] = 1
    return dictOfCandidates
