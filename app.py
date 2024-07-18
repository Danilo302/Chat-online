from flask import Flask, render_template
from routes.chat import socketio, init_app, bp_chat
from routes.register import bp_register

# Cria uma instância do Flask
app = Flask(__name__)
app.secret_key = 'jdefnbys@J#'

# Inicializa o SocketIO com o aplicativo Flask
init_app(app)


if __name__ == '__main__':
    app.register_blueprint(bp_chat)
    app.register_blueprint(bp_register)
    socketio.run(app)
