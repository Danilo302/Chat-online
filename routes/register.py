from flask import Blueprint, render_template, request,redirect,url_for,session

bp_register = Blueprint('register', __name__)

username = None

@bp_register.route('/', methods=['GET', 'POST'])
def register():
    global username
    if request.method == 'POST':
        username = request.form['username']
        print(username) 
        # if not username or username == '':
        #     error = 'Nome de usuário obrigatório'
        session['username'] = username
        return redirect(url_for('chat.view_chat'))
        
    else:       

        return render_template('register.html')

