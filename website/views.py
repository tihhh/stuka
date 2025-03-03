from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html")

@views.route('/test')
def test():
    return "<h1>This is a test route</h1>"