from flask import Blueprint, render_template, request, redirect, url_for, g, session

from app.auth import login_required

from .models import MyAPP, User
from app import db

bp = Blueprint('myapp', __name__, url_prefix='/myapp')

@bp.route('/')
@login_required
def index():
    myapps= MyAPP.query.all()
    return render_template('myapp/index.html', myapps=myapps)

@bp.route('/create', methods=('GET','POST'))
@login_required
def create():
    if request.method == 'POST':
        title= request.form['title']
        desc= request.form['desc']

        myapp = MyAPP(g.user.id, title, desc)

        db.session.add(myapp)
        db.session.commit()
        return redirect(url_for('myapp.index'))
    return render_template('myapp/create.html')

def get_myapp(id):
    myapp= MyAPP.query.get_or_404(id)
    return myapp

@bp.route('/update/<int:id>', methods=('GET','POST'))
@login_required
def update(id):

    myapp= get_myapp(id)

    if request.method == 'POST':
        myapp.title= request.form['title']
        myapp.desc= request.form['desc']
        myapp.state= True if request.form.get('state') == 'on' else False

        db.session.commit()
        return redirect(url_for('myapp.index'))
    return render_template('myapp/update.html', myapp= myapp)

@bp.route('/delete/<int:id>')
@login_required
def delete(id):
    myapp = get_myapp(id)
    db.session.delete(myapp)
    db.session.commit()
    return redirect(url_for('myapp.index'))