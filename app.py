from flask import Flask, render_template, redirect, url_for, jsonify, request
from firebase_sender import FirebaseSender
import random


app = Flask(__name__)
firebase_instance = FirebaseSender()

questions = firebase_instance.get(key="preguntas")


question = ''

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/start', methods=['POST'])
def start():
    return redirect(url_for('start'))


@app.route('/start')
def show_question():
    player1_score = firebase_instance.get_score()['player1_score']
    player2_score = firebase_instance.get_score()['player2_score']
    choices = random.randint(0, len(questions) - 1)
    if questions:
        selected_question = questions[choices]
        print('SELECTED QUESTION', selected_question)
        return render_template('start.html', data = {'question':selected_question,'player1_score':player1_score,'player2_score':player2_score})
    else:
        return "No questions found in the database"

@app.route('/submit_answer', methods=['POST'])
def submit_answer():
    data = request.form['answer']
    print('[DATA]: ', data)
    print("Respuesta correcta")
    player1_score = firebase_instance.get_score()['player1_score']
    player2_score = firebase_instance.get_score()['player2_score']
    firebase_instance.post_score(player1_score + 1, player2_score)
    return render_template('start.html')

@app.route('/reset', methods=['POST'])
def reset():
    firebase_instance.post_score(0, 0)
    return render_template('start.html')






if __name__ == '__main__':
    app.run()

