# Zenvisage Scatter Search

Scatter Search is a tool to explore large datasets by interacting with its scatter plot. The exploration reveals key insights about the dataset.

This application should be viewed as an implementation of ongoing research under the project Zenvisage at the University of Illinois at Urbana Champaign led by [Prof. Aditya Parameswaran][prof].

The in-progress research paper can be found [here][researchpaper]. (*Note: Update link*)

**In a nutshell, one should be able to**:
  - Select the columns one wants to explore (the XAxis, the YAxis and the ZAxis)
  - Draw the region(s) one wants to explore on the representative plot
  - Select the Ranking Algorithm
  - Get a ranked set of scatter plots

**Notes**:
  - The ZAxis represents the category, or the class, based on which the candidates are ranked.
  - The region(s) are 'drawn' on the representative plot in the form of polygons.
  - The ranking aims to find the order of prominence of candidates in the regions specified.

### Version
1.0.0

### Tech

Scatter Search uses a number of open source projects and modules to work properly:

* [D3] - combines powerful visualization components and a data-driven approach to DOM manipulation
* [Materialize] - A modern responsive front-end framework based on Material Design
* [Python 3.x][python] - evented I/O for the backend
* [Flask] - microframework for Python based on Werkzeug, Jinja 2 and good intentions
* [Numpy] - for computation 
* [Pickle] - a python module for object serialization
* [matplotlib] - for its Path.contains_points goodness
* [hopscotch] - An amazing framework to add product tours to their pages.
* [jQuery] - duh

And of course Scatter Search itself is open source with a [public repository][scattersearch]
 on GitHub.

### Getting started - Installation

#### OS X
Scatter Search requires [Python] 3.x to run.
```sh
$ brew install python3
```
Download the repository and then run pip to install all the dependencies.
```sh
$ git clone https://github.com/zenvisage/scatter-search
$ cd scatter-search
$ pip install --upgrade pip
$ pip install --upgrade -r requirements.txt
```

Then Run the Flask instance.
```sh
$ python scatter-search.py
```

#### Windows
Refer to https://www.python.org/downloads/windows/ for downloading and installing the latest version of Python 3.x

Also make sure you have git installed and added to the PATH.

Then run the following commands on the command line:
```sh
$ git clone https://github.com/zenvisage/scatter-search
$ cd scatter-search
$ python -m pip install --upgrade pip
$ python -m pip install --upgrade -r requirements.txt
$ python scatter-search.py
```

### Adding more datasets
To add a new dataset file, just add the file to the data/ folder.
As of now, only .csv and .txt are supported, but incase we'd like to include other formats, it's an easy update.

**Note:** The included datasets - iris, test, and diabetic_data represent three scenarios. Test wouldn't work because it has just one trivial row. Diabetic_data would be extremely slow and is not fit for the tool. Iris is the small (150 rows only) and easy dataset that I used during development.

### Extending: Adding indexing methods

The app uses Pickle to load and save datasets (in the form of python dictionaries). It's possible to compute and add more information to the dataset *before* saving the dictionary, to help improve performance the next time the dataset is used.
Also depickling instead of reading the .csv helps load datasets much faster.
```python
def index_data(data_dict):
    """
    This function might be used to index the data dictionary to be more useful
    in sophisticated algorithms.
    Note: In case the file is loaded as pickle, you shouldn't be calling this function.
    :param data_dict: dict, required
    :return: Indexed dictionary
    """
    return data_dict
```
*Note: More information about this section soon*

### Extending: Adding algorithms

*Note: This section is still in progress.*

Adding better, more sophisticated algorithms to the application is easy.

####Define your algorithm function in **utility/algorithms.py**.

Here is an example of how the existing naive algorithm is implemented. You should be able to see the output as a console log when you click 'Get Results'.

```python
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
```
Any algorithm takes three parameters:
- polygons
- candidates_info
- dataset

**polygons** are formatted to easily fit into the matplotlib.PATH object (they form a closed loop).
```python
:param polygons: {points: [[x1,y1],[x2,y2],...], type:'green'}
```

**candidates_info** is pretty much a map between the candidates and the number of points they have in the dataset.
```python
:param candidates_info: {'CandidateA':numOfOccurrencesInDataset, 'CandidateB'...}
```

The format of the **dataset** (as converted from .csv in the loadSaveDataset script) looks like this:
```python
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
```

####Add your algorithm name and function to the mapping dictionary.
```python
EXISTING_ALGORITHMS = {
    'Naive Algorithm': naive_algorithm,
    'Complex Algorithm': complex_algorithm
}
```

That's it! Now you should access to the algorithm on the web application.

### Todos

 - Implement naive algorithm
 - Add Results section (also provide a way to control number of top ranks)
 - Use Pickle to optimize load time
 - Use hopscotch to provide page tour
 - Update pending sections.
 - Add Usage section.
 - Add support for using multiple algorithms at once.

License
----

MIT

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [prof]: http://web.engr.illinois.edu/~adityagp/#
   [d3]: https://d3js.org/
   [materialize]: http://materializecss.com/
   [python]: https://www.python.org/
   [flask]: http://flask.pocoo.org/
   [numpy]: http://www.numpy.org/
   [pickle]:https://docs.python.org/3/library/pickle.html
   [jQuery]: <http://jquery.com>
   [hopscotch]: https://github.com/linkedin/hopscotch
   [scattersearch]: https://github.com/zenvisage/scatter-search
   [researchpaper]:http://web.engr.illinois.edu/~tsiddiq2/doc/zenvisage.pdf
