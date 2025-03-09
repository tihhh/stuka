from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user

import json


from . import db
from .models import Thread

threads = Blueprint('threads', __name__)

@threads.route('/threads')
@login_required
def show_threads():
    return render_template("threads.html", user=current_user)