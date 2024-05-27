
from flask import Flask, render_template, request, redirect, url_for, session
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/register')
def register():
  return render_template('register.html')

@app.route('/profile')
def profile():
  return render_template('profile.html')

@app.route('/game')
def game():
  return render_template('game.html')

@app.route('/chat')
def chat():
  return render_template('chat.html')

@app.route('/analysis')
def analysis():
  return render_template('analysis.html')

@socketio.on('connect')
def connect():
  emit('my response', {'data': 'Connected'})

@socketio.on('disconnect')
def disconnect():
  print('Client disconnected')

if __name__ == '__main__':
  socketio.run(app)
