# -*- coding: utf-8 -*-

"""
w2v_api.py
~~~~~~~~~~

This module implements API for Word2Vec model trained on Venmo data.

:copyright: (c) 2018 by Kemar Reid

USAGE:
    export FLASK_APP=w2v_api.py
    python -m flask run
    curl -i -H "Content-Type: application/json"\
    -X POST -d '{
    "positive": ["pizza"]
    "negative": [None]
    }' http://localhost:5000/w2v_venmo/api/v0.1/most_similar
"""

from os import environ

import emoji
import gensim
from flask import Flask, request, make_response, jsonify, abort

service_name = environ['SERVICE_NAME']
api_version = environ['API_VERSION']

# Create instance of web app
app = Flask(__name__)

# Load Word2Vec model
model = gensim.models.Word2Vec.load('model/model')


@app.route(f'/{service_name}/api/v{api_version}/most_similar',
           methods=['POST'])
def get_most_similar():
    """
    TODO:
    """
    if not request.json:
        abort(400)
    positive = request.json.get('positive', [])
    negative = request.json.get('negative', [])
    topn = request.json.get('topn', 1)
    try:
        result = model.wv.most_similar(
            positive=[emoji.emojize(word) for word in positive],
            negative=[emoji.emojize(word) for word in negative],
            topn=topn)
        return (jsonify({
            'similar': (result)
        }))
    except KeyError:
        return make_response(jsonify({
            'error': '%s not in vocabulary.' % 'Token(s)'
        }), 404)


@app.route(f'/{service_name}/api/v{api_version}/most_dissimilar',
           methods=['POST'])
def get_most_dissimilar():
    """
    TODO:
    """
    if not request.json:
        abort(400)
    words = request.json.get('words', [])
    try:
        result = model.wv.doesnt_match([emoji.emojize(word) for word in words])
        return jsonify({
            'dissimilar': (result)
        })
    except ValueError:
        return make_response(jsonify({
            'error': 'Empty list or %s not in vocabulary.' % 'token(s)'
        }), 404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
