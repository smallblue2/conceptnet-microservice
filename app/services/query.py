from re import sub
from flask import Blueprint, current_app, request, jsonify
import requests

query_blueprint = Blueprint('queryconceptnet', __name__)

# ENDPOINT /getrelated?term=<TERM HERE>
#
# Used to get related terms, returns keypair of related terms with weight
@query_blueprint.route('/getrelated', methods=['GET'])
def get_related():
    # Extract our term from the GET request
    term = request.args.get('term')
    # Build our url
    url = f'{current_app.config["CONCEPTNET_API_URL"]}/related/c/en/{term}?filter={current_app.config["CONCEPTNET_LANG_FILTER"]}'

    # Make a get request to the url & extract json
    response = requests.get(url)

    # If all is good, build a clean json and return with 200
    if response.status_code == 200:
        # Get the json
        response_json = response.json()

        # Build up a cleaner output
        clean_json = {}
        for index, item in enumerate(response_json['related']):
            clean_json[index] = {
                "concept": item['@id'].split('/')[-1],
                "weight": item['weight']
            }

        return jsonify(clean_json), 200
    else:
        return jsonify({"error": "There was a problem querying ConceptNet's API."}), response.status_code

# ENDPOINT /IsA?subject=<CONCEPT>&prednom=<PREDICATE NOMITAVE>
# both ?subject and ?prednom are optional, but one is required
#
# Used to get the IsA relationship of two terms
@query_blueprint.route('/IsA', methods=['GET'])
def is_a():
    # Extract our term from the GET request
    subject = request.args.get('subject')
    pred_nom = request.args.get('prednom')

    # Make sure they gave us something
    if not subject and not pred_nom:
        return jsonify({"error": "No argument given, please state ?prednom and/or ?subject."}), 400

    # Big fat complicated url
    #
    # If only subject is stated, we will query "<subject> is a X"
    # If only pred_nom is stated, we will query "X is a <pred_nom>"
    # If both are stated, we will query the strength of "<subject> is a <pred_nom>"
    url = f'{current_app.config["CONCEPTNET_API_URL"]}/query?{f"start=/c/en/{subject}" if subject else ""}{"&" if subject and pred_nom else ""}{f"end=/c/en/{pred_nom}" if pred_nom else ""}&rel=/r/IsA&filter={current_app.config["CONCEPTNET_LANG_FILTER"]}'

    # Make a get request to the url & extract json
    response = requests.get(url)

    # If all is good, build a clean json and return with 200
    if response.status_code == 200:
        # Get the json
        response_json = response.json()

        # Clean our json
        clean_json = {}
        for index, edge in enumerate(response_json["edges"]):
            edge_subject = edge['start']['label']
            edge_pred_nom = edge['end']['label']
            clean_json[index] = {
                'sentence': f"[{edge_subject}] is a kind of [{edge_pred_nom}]",
                'subject': edge_subject,
                'pred_nom': edge_pred_nom,
                'weight': edge['weight']
                }

        return jsonify(clean_json), 200
    else:
        return jsonify({"error": "There was a problem querying ConceptNet's API."}), response.status_code
