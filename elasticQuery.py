try:
    from flask import app,Flask
    from flask_restful import Resource, Api, reqparse
    from elasticsearch import Elasticsearch
except Exception as e:
    print("Modules Missing {}".format(e))

# Flask App
app = Flask(__name__)
# API the main entry point of the Application
# should be initialized with a flask application
api = Api(app)

# index name Elasticsearch
name = 'autocorrect'

# Getting Elasticsearch Connection
es = Elasticsearch([{'host': 'localhost', 'port': 9200}])


class ElasticSearch(Resource):

    # To auto_query for every input (Use of Constructor)
    def __init__(self):
        self.query = parser.parse_args().get("query", None)
        self.main_query ={
            "_source": "false",
            "size": 0,
            "suggest": {
                "auto": {
                    "prefix": "{}".format(self.query),
                    "completion": {
                        "field": "title",
                        "size" : 20,
                        "skip_duplicates": "true",
                        "fuzzy": {
                            "fuzziness": "auto"
                        }
                    }
                }
            }
        }

    def get(self):
        res = es.search(index=name, size=0, body=self.main_query)
        return res

# integrate with other packages that do the input/output stuff better
parser = reqparse.RequestParser()

# Adding argument for parsing
parser.add_argument("query", type=str, required=True)

# Adding resource to the api using Resource Class name
api.add_resource(ElasticSearch, '/autocomplete')

# Run the App
if __name__ == '__main__':
    app.run(debug=True, port=4000)
