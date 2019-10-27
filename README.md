# Word2Vec as a web service (model trained on 400M Venmo transactions) 

> [Overview]


## Usage


```bash
$ http POST localhost:5000/w2v_venmo/api/v0.1/most_similar \
positive:='["", "", ""]'
```
