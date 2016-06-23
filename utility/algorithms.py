import numpy as np
import matplotlib.path as mplPath


def naive_algorithm(polygons, candidates_info, dataset, options):
    """

    :param polygons: {points: [[x1,y1],[x2,y2],...], type:'green'}
    :param candidates_info: {'CandidateA':{
                                                numOfPoints: 50,
                                                data: [[row1_val1, row1_val2,...],...]
                              },
                             'CandidateB'...}
    :param dataset: As described in loadSaveDataset.py
    :param options: {
                        algorithm: string,
                        xAxis: index,
                        yAxis: index,
                        zAxis: index
                    }
    :return: Must return full dictionaries (same format as dataset) for the top k candidates
    """
    description = "This algorithm counts the number of occurences of each " \
                  "candidate in the provided polygons and DOES NOT consider the total  " \
                  "occurences of the candidate althroughout the chart."

    x = options['xAxis']
    y = options['yAxis']
    z = options['zAxis']
    data = dataset['data']
    result = {}

    for candidate in candidates_info:
        result_element = {
            'dataset_name': candidate,
            'data': candidates_info[candidate]['data'],
            'column_names': dataset['column_names'],
            'numOfPoints': candidates_info[candidate]['numOfPoints'],
            'numOfPointsInPolygons': 0,
            'score': 0
        }
        result[candidate] = result_element

    for polygon in polygons:
        points = np.array(polygon['points'])
        path = mplPath.Path(points)
        total_points = 0
        for row in data:
            point = [float(row[x]), float(row[y])]
            if path.contains_point(point):
                result[row[z]]['numOfPointsInPolygons'] += 1

    result_array = []

    for candidate in result:
        candidate = result[candidate]
        candidate['score'] = candidate['numOfPointsInPolygons']
        result_array.append(candidate)

    result_array = sorted(result_array, key=lambda k: k['score'], reverse=True)
    return {'algorithm': 'Naive Algorithm', 'description' : description, 'category': dataset['column_names'][z], 'result': result_array, 'x': x,
            'y': y}


def naive_algorithm_normalized(polygons, candidates_info, dataset, options):
    """

    :param polygons: {points: [[x1,y1],[x2,y2],...], type:'green'}
    :param candidates_info: {'CandidateA':{
                                                numOfPoints: 50,
                                                data: [[row1_val1, row1_val2,...],...]
                              },
                             'CandidateB'...}
    :param dataset: As described in loadSaveDataset.py
    :param options: {
                        algorithm: string,
                        xAxis: index,
                        yAxis: index,
                        zAxis: index
                    }
    :return: Must return full dictionaries (same format as dataset) for the top k candidates
    """

    description = "This algorithm counts the number of occurences of each " \
                  "candidate in the provided polygons and normalizes the count by dividing it by the  " \
                  "occurences of the candidate althroughout the chart, respectively. Thus the score of" \
                  " each candidate can be inferred as 'the fraction of themselves in the polygons'."
    x = options['xAxis']
    y = options['yAxis']
    z = options['zAxis']
    data = dataset['data']
    result = {}

    for candidate in candidates_info:
        result_element = {
            'dataset_name': candidate,
            'data': candidates_info[candidate]['data'],
            'column_names': dataset['column_names'],
            'numOfPoints': candidates_info[candidate]['numOfPoints'],
            'numOfPointsInPolygons': 0,
            'score': 0
        }
        result[candidate] = result_element

    for polygon in polygons:
        points = np.array(polygon['points'])
        path = mplPath.Path(points)
        total_points = 0
        for row in data:
            point = [float(row[x]), float(row[y])]
            if path.contains_point(point):
                result[row[z]]['numOfPointsInPolygons'] += 1

    result_array = []

    for candidate in result:
        candidate = result[candidate]
        candidate['score'] = candidate['numOfPointsInPolygons'] / candidate['numOfPoints']
        result_array.append(candidate)

    result_array = sorted(result_array, key=lambda k: k['score'], reverse=True)
    return {'algorithm': 'Naive Algorithm Normalized', 'description' : description,'category': dataset['column_names'][z], 'result': result_array,
            'x': x,
            'y': y}


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
    'Naive Algorithm Normalized': naive_algorithm_normalized,
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
            dictOfCandidates[candidate]['numOfPoints'] += 1
            dictOfCandidates[candidate]['data'].append(row)
        else:
            dictOfCandidates[candidate] = {}
            dictOfCandidates[candidate]['numOfPoints'] = 1
            dictOfCandidates[candidate]['data'] = [row]
    return dictOfCandidates
