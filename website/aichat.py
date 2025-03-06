from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import Message
from . import db
from flask_login import login_required, current_user
import json

aichat = Blueprint('aichat', __name__)


@aichat.route('/chat', methods=['GET', 'POST'])
@login_required
def chat():
    if request.method == 'POST':
        message = request.form.get('message')
        new_message = Message(content=message, user_id=current_user.id, sender=True)
        db.session.add(new_message)
        db.session.commit()
    
    messages = Message.query.order_by(Message.date).all()
    
    return render_template('aichat.html', user=current_user, messages=messages)
        
