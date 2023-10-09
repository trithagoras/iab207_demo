from flask import Blueprint, render_template, request, redirect, url_for
from sqlalchemy import or_
from .models import Destination
from . import db

mainbp = Blueprint('main', __name__)

@mainbp.route('/')
def index():
    destinations = db.session.scalars(db.select(Destination)).all()    
    return render_template('index.html', destinations=destinations)

@mainbp.route('/search')
def search():
    if request.args['search'] and request.args['search'] != "":
        print(request.args['search'])
        query = "%" + request.args['search'] + "%"
        
        selection = db.select(Destination).where(
            or_(
                Destination.description.like(query), 
                Destination.name.like(query)
            )
        )
        destinations = db.session.scalars(selection).all()
        
        return render_template('index.html', destinations=destinations)
    else:
        return redirect(url_for('main.index'))