import random
from travel import db, create_app
from travel.models import *
app = create_app()
ctx = app.app_context()
ctx.push()

db.session.add_all([
    Destination(name='Greece', description='Sunshine and beaches', currency='EUR', image='/static/image/greece.jpg'),
    Destination(name='Japan', description='Visiting in the Spring time to see the cherry blossoms in bloom is a must-see experience!', currency='JPY', image='/static/image/japan.jpg'),
    Destination(name='Australia', description='Visit the Great Barrier Reef!', currency='AUD', image='/static/image/australia.jpg'),
    Destination(name='Iceland', description='See the Northern Lights!', currency='ISK', image='/static/image/iceland.jpg'),
    Destination(name='Norway', description='Very very cold!', currency='NOK', image='/static/image/oslo_north.jpg'),
    Destination(name='Italy', description='Pizza and pasta!', currency='EUR', image='/static/image/italy.jpg'),
    Destination(name='France', description='Visit the Eiffel Tower!', currency='EUR', image='/static/image/france.jpg'),
    Destination(name='Spain', description='Visit the Sagrada Familia!', currency='EUR', image='/static/image/spain.jpg'),
    Destination(name='United States', description='Visit the Grand Canyon!', currency='USD', image='/static/image/usa.jpg'),
    Destination(name='Canada', description='Visit the CN Tower!', currency='CAD', image='/static/image/canada.jpg')
])
db.session.commit()

# generate random user
"""
class User(db.Model, UserMixin):
    __tablename__ = 'users' # good practice to specify table name
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), index=True, unique=True, nullable=False)
    emailid = db.Column(db.String(100), index=True, nullable=False)
	#password is never stored in the DB, an encrypted password is stored
	# the storage should be at least 255 chars long
    password_hash = db.Column(db.String(255), nullable=False)
    # relation to call user.comments and comment.created_by
    comments = db.relationship('Comment', backref='user')
"""



# generate random comments
"""
class Comment(db.Model):
    __tablename__ = 'comments'
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.String(400))
    created_at = db.Column(db.DateTime, default=datetime.now())
    # add the foreign keys
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    destination_id = db.Column(db.Integer, db.ForeignKey('destinations.id'))
"""