from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import Message, Thread
from . import db
from flask_login import login_required, current_user
import json

aichat = Blueprint('aichat', __name__)

@aichat.route('/chat', methods=['GET', 'POST'])
@login_required
def chat():
    if request.method == 'POST':
        message_content = request.form.get('message')
        thread_id = request.form.get('thread_id')
        
        if not message_content:
            flash('Message cannot be empty!', category='error')
            return redirect(url_for('aichat.chat'))
        
        if not thread_id:
            # Create new thread for first message
            thread = Thread(
                title=message_content[:50] + "...",  # Use first 50 chars as title
                user_id=current_user.id
            )
            db.session.add(thread)
            db.session.commit()
            thread_id = thread.id
        else:
            thread = Thread.query.get(thread_id)
            if not thread or thread.user_id != current_user.id:
                flash('Invalid thread.', category='error')
                return redirect(url_for('threads.show_threads'))

        # Add user message
        user_message = Message(
            content=message_content,
            is_ai=False,
            thread_id=thread_id
        )
        db.session.add(user_message)
        
        # Add AI response (placeholder for now)
        ai_response = "This is a placeholder AI response."
        ai_message = Message(
            content=ai_response,
            is_ai=True,
            thread_id=thread_id
        )
        db.session.add(ai_message)
        db.session.commit()

        # Redirect back to the same chat with the thread_id
        return redirect(url_for('aichat.chat', thread_id=thread_id))
    
    # For GET requests or after processing POST
    active_thread_id = request.args.get('thread_id')
    if active_thread_id:
        thread = Thread.query.get(active_thread_id)
        if thread and thread.user_id == current_user.id:
            messages = thread.messages
        else:
            messages = []
    else:
        messages = []
        
    return render_template('aichat.html', 
                         user=current_user, 
                         messages=messages,
                         thread=thread)
        
