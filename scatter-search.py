import os
from flask import Flask, render_template, request, jsonify
import json
import utility.algorithms as alg
import utility.loadSaveDataset as loadSaveDataset
from os import sys

app = Flask(__name__)

# Global variable that stores the current dataset in use
current_dataset = {}

@app.route('/')
def index_page():
    dataset_list = loadSaveDataset.get_csv_list();
    print(dataset_list)
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
    # try:
    candidates_info = alg.get_candidates_info(current_dataset['data'], d['options']['zAxis'])
    polygons = d['polygons']
    # except Exception as e:
    #     exc_type, exc_obj, exc_tb = sys.exc_info()
    #     fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)
    #     print(exc_type, fname, exc_tb.tb_lineno)
    return json.dumps(alg.EXISTING_ALGORITHMS[d['options']['algorithm']](polygons,candidates_info,current_dataset))

@app.route('/renderDashboard')
def renderDashboard():
    global current_dataset
    return jsonify(current_dataset)


if __name__ == '__main__':
    app.run()(debug=True)
