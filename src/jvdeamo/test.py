from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def welcome_message():
    return "Bem-vindo(a) ao App Senai!"

def redirect_to_menu():
    return redirect(url_for('menu'))

def redirect_to_exit():
    return redirect(url_for('exit'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/iniciar', methods=['POST'])
def iniciar():
    clear_screen()
    
    if 'nome' in request.form:
        return redirect_to_menu()
    elif 'sair' in request.form:
        return redirect_to_exit()

@app.route('/menu')
def menu():
    return render_template('menu.html', message=welcome_message())

@app.route('/exit', methods=['GET', 'POST'])
def exit():
    return render_template('exit.html')

if __name__ == "__main__":
    app.run(debug=True)
