from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def index():
    return {
        'message': 'This is the index',
        'method': request.method
    }

@app.route('/hello-world')
def hello_world():
    return {
        'message': 'Hello World from server',
        'method': request.method
    }



@app.route('/py-api/entities', methods=['GET', 'POST'])
def entities():
    if request.method == "GET":
        return {
            'message': 'This endpoint should return a list of entities',
            'method': request.method
        }
    if request.method == "POST":
        return {
            'message': 'This endpoint should create an entity',
            'method': request.method,
            'body': request.json
        }


@app.route('/py-api/entities/<int:entity_id>',
           methods=['GET', 'PUT', 'DELETE'])
def entity(entity_id):
    if request.method == "GET":
        return {
            'id': entity_id,
            'message':
            f'This endpoint should return the entity {entity_id} details',
            'method': request.method
        }

    if request.method == "PUT":
        return {
            'id': entity_id,
            'message': f'This endpoint should update the entity {entity_id}',
            'method': request.method,
            'body': request.json
        }

    if request.method == "DELETE":
        return {
            'id': entity_id,
            'message': f'This endpoint should delete the entity {entity_id}',
            'method': request.method
        }


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='80')

# CRUD
# Esquemas son: ->
#               ->
