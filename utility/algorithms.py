def naive_algorithm(polygons, candidates_info, dataset):
    """

    :param polygons: {points: [[x1,y1],[x2,y2],...], type:'green'}
    :param candidates_info: {'CandidateA':numOfOccurrencesInDataset, 'CandidateB'...}
    :param dataset: As described in loadSaveDataset.py
    :return: Must return full dictionaries (same format as dataset) for the top k candidates
    """
    return {'comment': 'Hello from the Naive Algorithm'}


def complex_algorithm(polygons, candidates_info, dataset):
    """

    :param polygons:
    :param candidates_info:
    :param dataset:
    :return:
    """
    return {'comment': 'Hello from the Complex Algorithm'}


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
