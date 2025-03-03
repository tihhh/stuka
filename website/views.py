from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user

import json


from . import db
from .models import Note

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        if len(note) < 1:
            flash('Note is too short!', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added!', category='success')

    return render_template("home.html", user=current_user)

@views.route('/test')
def test():
    return "<h1>This is a test route</h1>"

@views.route('/delete-note', methods=['POST'])
@login_required
def delete_note():
    try:
        note = json.loads(request.data)
        noteId = note['noteId']
        note = Note.query.get(noteId)
        if note:
            if note.user_id == current_user.id:
                db.session.delete(note)
                db.session.commit()
                return jsonify({"success": True})
            return jsonify({"error": "Unauthorized"}), 401
        return jsonify({"error": "Note not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 400