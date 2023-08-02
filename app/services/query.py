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
    response_json = response.json()

    # If all is good, build a clean json and return with 200
    if response.status_code == 200:
        # Build up a cleaner output
        clean_json = {}
        for item in response_json['related']:
            clean_json[item['@id'].split('/')[-1]] = item['weight']

        return jsonify(clean_json), 200
    else:
        return jsonify({"error": "There was a problem querying ConceptNet's API."}), response.status_code
