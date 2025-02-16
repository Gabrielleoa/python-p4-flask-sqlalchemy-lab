#!/usr/bin/env python3

from flask import Flask, make_response
from flask_migrate import Migrate

from models import db, Zookeeper, Enclosure, Animal

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

# @app.route('/animal/<int:id>')
# def animal_route(id):
    # animal = Animal.query.filter(Animal.id == id).first()

    # response_body= f'''
    #     <h1>Information for {animal.name}</h1>
    #     <h2>Pet Species is {animal.species}</h2>
    #     <h2>Pet Owner is
    # '''


    # response = make_response(response_body, 200)


    # pass

@app.route('/')
def home():
    return '<h1>Zoo app</h1>'

@app.route('/animal/<int:id>')
def animal_by_id(id):

    animal = Animal.query.filter(Animal.id == id).first()
    response_body = f'''
    <ul>
        <li>ID: {animal.id} </li>
        <li>Name: {animal.name}</li>
        <li> Species: {animal.species}</li>
        <li>Zookeper: {animal.zookeepername}</li>
        <li>Enclosure: {animal.enclosure}</li>
    </ul>
''',
    200
    response = make_response(response_body,200)
    return response 




@app.route('/zookeeper/<int:id>')
def zookeeper_by_id(id):
    zookeeper = Zookeeper.query.filter(Animal.id == id). first()
    response_body = f'''
    <ul>
        <li>ID: {zookeeper.id}</li>
        <li>Name: {zookeeper.name}</li>
        <li>Birthday: {zookeeper.birthday}</li>
        <li>Animal: {zookeeper.animals}</li>
    </ul>
    ''',
    200
    response = make_response(response_body,200)
    return response


@app.route('/enclosure/<int:id>')
def enclosure_by_id(id):
    enclosure = Enclosure.query.filter(Enclosure.id==id).first()
    response_body = f'''
    <ul>
        <li>ID: {enclosure.id}</li>
        <li>Environment{enclosure.environment}</li>
        <li>Open to Visitors: {enclosure.opentovisitors}</li>
        <li>Animals {enclosure.listofanimals}</li>
    </ul>
    ''',
    200
    response = make_response(response_body,200)
    return response


if __name__ == '__main__':
    app.run(port=5555, debug=True)
