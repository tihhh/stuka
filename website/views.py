from flask import Blueprint, render_template

views = Blueprint('views', __name__)

@views.route('/')
def home():
    return render_template("home.html")

@views.route('/test')
def test():
    return "<h1>This is a test route</h1>"