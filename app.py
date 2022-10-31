"""Flask app for Cupcakes"""

from flask import Flask, request, jsonify, render_template

from models import db, connect_db, Cupcake

app = Flask(__name__)
app.app_context().push()

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///cupcakes'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = "oh-so-secret"

connect_db(app)

@app.route('/')
def display_root():
  '''Show simple home page.'''
  cupcakes = Cupcake.query.all()
  return render_template('index.html', cupcakes=cupcakes)

@app.route('/api/cupcakes')
def show_cupcakes():
  '''return json with all info.'''
  all_cupcakes = [cupcake.serialize() for cupcake in Cupcake.query.all()]
  return jsonify(cupcakes=all_cupcakes)

@app.route('/api/cupcakes', methods=['POST'])
def add_cupcake():
  '''update db with cupcake.'''
  data = request.json
  cupcake = Cupcake(flavor=data['flavor'], size=data['size'], rating=data['rating'], image=data['image'] or None)
  db.session.add(cupcake)
  db.session.commit()
  return (jsonify(cupcake=cupcake.serialize()), 201)

@app.route('/api/cupcakes/<int:cupcake_id>', methods=['GET'])
def show_cupcake(cupcake_id):
  '''return json with info on specific cupcake.'''
  cupcake = Cupcake.query.get_or_404(cupcake_id)
  json_cupcake = cupcake.serialize()
  return jsonify(cupcake=json_cupcake)

@app.route('/api/cupcakes/<int:cupcake_id>', methods=['PATCH'])
def edit_cupcake(cupcake_id):
  '''return json with info on specific cupcake.'''
  cupcake = Cupcake.query.get_or_404(cupcake_id)
  data = request.json
  cupcake.flavor = data['flavor']
  cupcake.size = data['size']
  cupcake.rating = data['rating']
  cupcake.image = data['image']

  db.session.add(cupcake)
  db.session.commit()
  return jsonify(cupcake=cupcake.serialize())

@app.route('/api/cupcakes/<int:cupcake_id>', methods=['DELETE'])
def delete_cupcake(cupcake_id):
  '''delete specific cupcake.'''
  cupcake = Cupcake.query.get_or_404(cupcake_id)
  db.session.delete(cupcake)
  db.session.commit()
  return jsonify(message='deleted')
