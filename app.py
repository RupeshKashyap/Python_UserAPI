import json
from flask_mysqldb import MySQL
from flask import Flask, request, Response, abort, g
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy
import uuid

JSON_MIME_TYPE = 'application/json'

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABADE_URI'] = 'mysql://root:12345@localhost/userapi' 

db = SQLAlchemy(app)

class users(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	first_name = db.Column(db.String(20))
	last_name = db.Column(db.String(20))
	company_name = db.Column(db.String(20))
	age = db.Column(db.Numeric(3))
	city = db.Column(db.String(20))
	state = db.Column(db.String(20))
	zip = db.Column(db.Numeric(6))
	email = db.Column(db.String(30))
	web = db.Column(db.String(30))
	


@app.route('/user', methods=['GET'])
def get_all_user():

    all_users = users.query.all()

    output = []

    for user in users:
        user_data = {}
        user_data['id'] = user.id
        user_data['first_name'] = user.first_name
        user_data['last_name'] = user.last_name
        user_data['company_name'] = user_data.company_name
        user_data['age'] = user_data.age
        user_data['city'] = user_data.city
        user_data['state'] = user_data.state
        user_data['zip'] = user_data.zip
        user_data['email'] = user_data.email
        user_data['web'] = user_data.web
        output.append(user_data)
    return jsonify({'user': output})

@app.route('/user/<id>', methods=['GET'])
def get_one_user(id):

    user = users.query.filter_by(id=id).first()

    if not user:
        return jsonify({'message': 'No User Found!'})
    
    else:
	    user_data = {}
	    user_data['id'] = user.id
	    user_data['first_name'] = user.first_name
	    user_data['last_name'] = user.last_name
	    user_data['company_name'] = user_data.company_name
	    user_data['age'] = user_data.age
	    user_data['city'] = user_data.city
	    user_data['state'] = user_data.state
	    user_data['zip'] = user_data.zip
	    user_data['email'] = user_data.email
	    user_data['web'] = user_data.web
	    return jsonify({'user': user_data})


@app.route('/user', methods=['POST'])
def create_user():
    data = request.get_json()

    new_user = users(id=str(uuid.uuid4()),
    				first_name=data['first_name'],
    				last_name=data['last_name'],
    				company_name=data['company_name'],
    				age=data['age'],
    				city=data['city'],
    				state=data['state'],
    				zip=data['zip'],
    				email=data['email'],
    				web=data['web'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'New User Created!'})


@app.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
    user = users.query.filter_by(id=id).first()

    if not user:
        return jsonify({'message': 'No user found!'})

    db.session.delete(user)
    db.session.commit()
    return jsonify({'message': 'The user has been deleted'})

if __name__ == '__main__':
	app.run(debug=True)