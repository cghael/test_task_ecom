import os
import re
from dotenv import load_dotenv
from flask import Flask, jsonify, request
from pymongo import MongoClient


load_dotenv()

app = Flask(__name__)
print(os.getenv('MONGO_CONNECTION'))
client = MongoClient(os.getenv('MONGO_CONNECTION'))
db = client['mydb']
templates_collection = db['templates']


def validate_data(field, value):
    if field == "date" and not re.match(
            (r'\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$|'
             r'\d{2}\.\d{2}\.\d{4}'),
            value
    ):
        return "date"
    elif field == "phone" and not re.match(
            r'\+7 \d{3} \d{3} \d{2} \d{2}$',
            value
    ):
        return "phone"
    elif field == "email" and not re.match(r'\S+@\S+\.\S+', value):
        return "email"
    elif field == "text" and not value:
        return "text"
    else:
        return None


@app.route('/get_form', methods=['POST'])
def get_form():
    request_data = request.form.to_dict()
    form_templates = templates_collection.find()

    best_match = None
    max_matching_fields = 0

    for template in form_templates:
        template_keys = set(template.keys()) - {'_id', 'name'}
        request_data_keys = set(request_data.keys())

        matching_fields = len(template_keys.intersection(request_data_keys))

        if (matching_fields == len(template_keys)
                and matching_fields > max_matching_fields):
            max_matching_fields = matching_fields
            best_match = template

    if best_match:
        invalid_fields = {}
        for key, value in request_data.items():
            template_field = best_match.get(key)
            if template_field:
                error = validate_data(template_field, value)
                if error:
                    invalid_fields[key] = error

        if invalid_fields:
            return jsonify(invalid_fields), 400
        else:
            return jsonify({"template_name": best_match["name"]})
    return jsonify({"error": "Template not found"}), 404


if __name__ == '__main__':
    app.run(host=os.getenv('HOST'), port=os.getenv('PORT'))
