"""Models for Cupcake app."""
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

default_img = 'https://tinyurl.com/demo-cupcake'

def connect_db(app):
  '''Connect to db.'''
  db.app = app
  db.init_app(app)

class Cupcake(db.Model):
  '''Cupcake.'''

  __tablename__ = 'cupcakes'

  id = db.Column(db.Integer, primary_key=True, autoincrement=True)
  flavor = db.Column(db.Text, nullable=False)
  size = db.Column(db.Text, nullable=False)
  rating = db.Column(db.Float, nullable=False)
  image = db.Column(db.Text, default=default_img, nullable=False)

  def serialize(self):
    '''Make json for each instance.'''
    return {
      'id': self.id,
      'flavor': self.flavor,
      'size': self.size,
      'rating': self.rating,
      'image': self.image
    }
