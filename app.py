#!flask/bin/python
from flask import Flask, jsonify, abort, make_response, request
from flask_restful import Api, reqparse, Resource
from base import People, db

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['PROPAGATE_EXCEPTIONS'] = True

db.init_app(app)
app.app_context().push()
db.create_all()


# To GET or POST name, height, and age from the database
class People_List(Resource):
    # Get details from the json data
    parser = reqparse.RequestParser()
    parser.add_argument('name', type=str, required=True, help='Name of the person')
    parser.add_argument('height', type=int, required=True, help='Height of the person')
    parser.add_argument('age', type=int, required=True, help='Age of the person')

    # Add details to the database
    def post(self):
        args = People_List.parser.parse_args()
        name = args['name']

        if People.query.filter_by(name=name).first():
            return {'Message': 'Person with the name {} already exists'.format(name)}, 500

        item = People(name, args['height'], args['age'], None, None)
        item.save_to()
        return item.json(), 201

# To GET or POST email, and number from the database
class Contact_List(Resource):
    # Get details from the json data
    parser = reqparse.RequestParser()
    parser.add_argument('email', type=str, required=True, help='Email of the person')
    parser.add_argument('number', type=str, required=True, help='Number of the person')

    # Add details to the database
    def post(self, id):
        args = Contact_List.parser.parse_args()
        email = args['email']
        number = args['number']

        if People.query.filter_by(email=email).first():
            return {'Message': 'Person with the email {} already exists'.format(email)}, 500
        elif People.query.filter_by(number=number).first():
            return {'Message': 'Person with the number {} already exists'.format(number)}, 500

        item = People.find_by_id(id)
        if item:
            item.email = email
            item.number = number
            item.save_to2()
            return item.json2(), 201
        return {'Message': 'Person with the id {} not found'.format(id)}, 500

# Return name, age, and height of everyone
class All_People(Resource):
    def get(self):
        return {'Persons': list(map(lambda x: x.json(), People.query.all()))}, 200

# Return email and number of everyone
class All_Contact(Resource):
    def get(self):
        return {'Contact': list(map(lambda x: x.json2(), People.query.all()))}, 200

# To get the details of a person based on the query parameters (name, email, number)
@app.route('/contacts/', methods=["GET"])
def api_filter():
    query_parameters = request.args

    name = query_parameters.get('name')
    email = query_parameters.get('email')
    number = query_parameters.get('number')

    item = None
    if name:
        item = People.query.filter_by(name=name).first()
    elif email:
        item = People.query.filter_by(email=email).first()
    elif number:
        item = People.query.filter_by(number=number).first()

    if item == None:
        return not_found(404)

    return item.jsonAll(), 200

api.add_resource(All_People, '/')
api.add_resource(People_List, '/people/')
api.add_resource(All_Contact, '/all_contacts/')
api.add_resource(Contact_List, '/people/<int:id>/contacts/')

# when no pages are found or there is error
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

if __name__ == '__main__':
    app.run(debug=True)