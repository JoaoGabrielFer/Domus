from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class Teste(Resource):
    def get(self, name):
        return {"data": name}
    
    def put(self, name):
        print(request.form["likes"])
        return {}
    
api.add_resource(Teste, "/<string:name>")

if __name__ == "__main__":
    app.run(debug=True)
