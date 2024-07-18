from flask_socketio import SocketIO,emit
from flask import Blueprint, render_template, redirect,url_for,session


bp_chat = Blueprint('chat',__name__)

# Cria uma instância de SocketIO
socketio = SocketIO()


def init_app(app):
    socketio.init_app(app)

@bp_chat.route('/chat')
def view_chat():
    username = session.get('username', None)
    if username == None:
        print(username)
        return redirect(url_for('register.register'))
    else:
        return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    print('Cliente conectado')

@socketio.on('message')
def chat(message):
    username = session.get('username', None)
    
    print(f'{username}: {message}')
    emit('message', {'username': username, 'message': message}, broadcast=True)
    