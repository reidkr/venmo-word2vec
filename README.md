# Simple Word2Vec web service, model pre-trained on Venmo dataset 

> API serves Word2Vec model pre-trained on about 400M public Venmo transactions posted between 2014 and 2017. The model consists 200-dimensional vectors for 100,000+ words and emojis used on the payment platform. Word2Vec maps words to vectors in such a way that words that have similar meanings or that occur in similar contexts (based on their usage patterns) have vectors that are close together.    

## Getting started

### w/ Pipenv

This project uses [Pipenv](https://pipenv.readthedocs.io/en/latest/) to manage dependencies (described in the `Pipfile`) and Python virtual environments.

To get started, install Pipenv with pip:

`$ pip install -U pipenv`

On macOS, pipenv can also be installed _via_ [Homebrew](https://brew.sh/):

`$ brew install pipenv`

To install the projects' dependencies, in the project's root folder run:

`$ pipenv install --dev`

Then run the web service:

`pipenv run python -m flask run`


<!-- 
:TODO:
### w/ Docker

Alternatively, to run the service as a containerized application use docker. 

-->

## Usage

> Word2Vec automatically learns patterns and relationships in user interactions and the transactions they make.

To interact with the model, visit the `http://localhost:5000/w2v_venmo/api/v0.1/most_similar` endpoint. It accepts a list of words that contribute positively or negatively to a similarity measure between word vectors and returns the top-N most similar words.

```bash
$ curl http://localhost:5000/w2v_venmo/api/v0.1/most_similar \
    --request POST \
    --header "Content-Type: application/json" \
    --data '{"positive": [""], "negative": [""], "topn": 1}'
```

### Examples

```bash
# The word vectors encode associations that reflect the usage patterns of emojis. 
# For instance, users most often use the 'eggplant' and 'peach' emojis in the same context.
curl http://localhost:5000/w2v_venmo/api/v0.1/most_similar \
    --request POST \
    --header "Content-Type: application/json" \
    --data '{"positive": ["🍆"]}'

''' 
Out:
"similar": [("🍑", 0.777)]
'''

# Word2Vec also learns slang for certain transactions.
curl http://localhost:5000/w2v_venmo/api/v0.1/most_similar \
    --request POST \
    --header "Content-Type: application/json" \
    --data '{"positive": ["marijuana"]}'

''' 
Out:
"similar": [("weed", 0.751), ("kush", 0.621)]
'''

# The model also infers concepts related to combinations of words 
curl http://localhost:5000/w2v_venmo/api/v0.1/most_similar \
    --request POST \
    --header "Content-Type: application/json" \
    --data '{"positive": ["pizza", "football", "party"]}'

''' 
Out:
"similar": [("superbowl", 0.489)]
'''
```

<!-- These are just a few examples of the patterns lurking in user interactions and transactions on Venmo that Word2Vec is able to uncover. -->