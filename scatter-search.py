import os
from flask import Flask, render_template, request, jsonify
import json
from utility import algorithms as alg
import utility.loadSaveDataset as loadSaveDataset
from os import sys

app = Flask(__name__)

# Global variable that stores the current dataset in use
current_dataset = {}

@app.route('/')
def index_page():
    dataset_list = loadSaveDataset.get_csv_list();
    return render_template('index.html', datasets = dataset_list)

@app.route('/load')
def show_loading():
    dataset_name = request.args.get('dataset')
    return render_template('loading-page.html', dataset_name=dataset_name)


@app.route('/main')
def render_main_page():
    global current_dataset
    return render_template('main.html', dataset = current_dataset, algorithms = alg.EXISTING_ALGORITHMS)


@app.route('/setDataset', methods=['GET'])
def set_dataset():
    dataset_name = request.args.get('dataset')
    global current_dataset
    current_dataset = loadSaveDataset.get_data_dict(dataset_name,skip_header=1);
    if('error' in current_dataset):
        return json.dumps(current_dataset)
    return json.dumps({'status':'ok'})


@app.route('/getResults', methods=['POST'])
def get_results():
    d = request.get_json()
    polygons = d['polygons']
    options = d['options']
    algorithm = options['algorithm']
    candidates_info = alg.get_candidates_info(current_dataset['data'], options['zAxis'])
    results = alg.EXISTING_ALGORITHMS[algorithm](polygons,candidates_info,current_dataset,options)
    return render_template('results.html', results = results)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
