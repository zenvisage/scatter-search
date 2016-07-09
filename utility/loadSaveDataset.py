import os
import numpy
import pickle
from os import listdir

# Data Folder Configuration
DATA_DIRECTORY = "data"
ALLOWED_EXTENSIONS = set(['txt', 'csv'])

def allowed_file(filename, allowed_extensions):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in allowed_extensions

def get_csv_list():
    """
    Fetches the list of all available csvs in the csv directory
    :return:jsonDump of list of csvs
    """
    # os.chdir("C:\\Users\\an5ra\\PycharmProjects\\untitled5")
    dataset_list = []
    all_files = listdir(DATA_DIRECTORY)
    for file in all_files:
        if(allowed_file(file,ALLOWED_EXTENSIONS)):
            dataset_list.append(file)

    return dataset_list

def get_data_dict(dataset_name, skip_header=0):
    """
    Function to get a python dictionary representation of a dataset.
    Only CSVs are supported as of now.
    TODO: Add pickling/depickling.
    :param file_path:   str, required
                        Eg: 'data/iris.csv'
    :param skip_header: int, optional
                        Defaults to 0, otherwise skips the given number of rows
                        Using the last skipped row as column names
    :return:    A python dictionary
                {
                    dataset_name: str,
                    column_names:[str],
                    data: [[row1_val1, row1_val2,...],...],
                    cols: int,
                    rows: int,
                    loaded_from_pickle: bool
                }
                or if an exception was thrown:
                {
                    error: str
                }
    """
    dataset_file_path = DATA_DIRECTORY + '/' + dataset_name
    data_dict = dict()
    dataset = []

    try:
        dataset = numpy.genfromtxt(dataset_file_path, delimiter=',', dtype=str)
    except OSError:
        return ({'error': "File not found"})
    except ValueError:
        return ({'error': 'Error with dataset (probably missing values)'})
    except:
        return ({'error': 'Unexpected error. Please report the issue on github.'})

    try:
        no_of_columns = dataset.shape[1]
        no_of_rows = dataset.shape[0]
    except:
        return ({'error': 'Too few rows or columns'})

    col_names = []

    if (skip_header > 0):
        for i in range(0, no_of_columns):
            col_names.append(dataset[skip_header-1][i])
        dataset = dataset[skip_header:]
    else:
        for i in range(0, no_of_columns):
            col_names.append("Column " + str(i + 1) + "")

    data_dict['dataset_name'] = dataset_name
    data_dict['column_names'] = col_names
    data_dict['data'] = dataset.tolist()
    data_dict['cols'] = no_of_columns
    data_dict['rows'] = no_of_rows

    pickle_file_name = 'pickles/' + dataset_name + '.pickle'
    with open(pickle_file_name, 'wb') as f:
        pickle.dump(data_dict,f,pickle.HIGHEST_PROTOCOL,)
    data_dict['loaded_from_pickle'] = False

    return data_dict


def index_data(data_dict):
    """
    This function might be used to index the data dictionary to be more useful
    in sophisticated algorithms.
    Note: In case the file is loaded as pickle, you shouldn't be calling this function.
    :param data_dict: dict, required
    :return: Indexed dictionary
    """
    return data_dict

