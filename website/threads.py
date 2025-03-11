from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user

import json


from . import db
from .models import Thread

threads = Blueprint('threads', __name__)

@threads.route('/threads')
@login_required
def show_threads():
    # Get all threads for the current user, ordered by most recent first
    user_threads = Thread.query.filter_by(user_id=current_user.id).order_by(Thread.created_date.desc()).all()
    return render_template("threads.html", user=current_user, threads=user_threads)

@threads.route('/thread/<int:thread_id>')
@login_required
def view_thread(thread_id):
    thread = Thread.query.get_or_404(thread_id)
    if thread.user_id != current_user.id:
        flash('Access denied.', category='error')
        return redirect(url_for('threads.show_threads'))
    return redirect(url_for('aichat.chat', thread_id=thread_id))