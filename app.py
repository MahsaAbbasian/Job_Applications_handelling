from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)


@app.route('/submit-cv', methods=['POST'])
def submit_cv():
    cv_text = request.json['cvText']
    # Process the CV text here
    response_message = "CV processed successfully."  # Example response message
    return jsonify(message=response_message)


if __name__ == '__main__':
    app.run(debug=True)
