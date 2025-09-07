import os

from flask import Flask, render_template, request, redirect, url_for, session
from common import *

app = Flask(__name__)

# La liste de questions pour le quiz
QUESTIONS = [
    {
        "question": "Quel est l'oiseau le plus rapide du monde ?",
        "options": ["Aigle royal", "Faucon pèlerin", "Martinet noir", "Autruche"],
        "answer": "Faucon pèlerin"
    },
    {
        "question": "Quelle est la capitale de l'Australie ?",
        "options": ["Sydney", "Melbourne", "Canberra", "Perth"],
        "answer": "Canberra"
    },
    {
        "question": "Combien de planètes compte le système solaire ?",
        "options": ["7", "8", "9", "10"],
        "answer": "8"
    }
]


# Route pour la page d'accueil (le quiz)
# @app.route('/')
# def quiz():
#     return render_template('index.html', questions=QUESTIONS)

@app.route('/')
def start_survey():
    # Clear any previous session data and start the survey
    session.clear()
    session['current_question'] = 0
    session['answers'] = {}
    return redirect(url_for('ask1'))


@app.route('/ask1', methods=['GET', 'POST'])
def ask1():
    current_q_index = session.get('current_question', 0)

    # Check if all questions have been asked
    if current_q_index >= len(QUESTIONS):
        return redirect(url_for('show_results'))

    question_text = QUESTIONS[current_q_index]['question']

    if request.method == 'POST':
        # Get the answer from the form
        user_answer = request.form['answer']

        # Save the answer to the session dictionary
        session['answers'][question_text] = user_answer

        # Increment the question index for the next question
        session['current_question'] += 1

        # Redirect back to the question route to display the next question
        return redirect(url_for('ask1'))

    # For a GET request, render the question page
    return render_template('question.html', question=question_text)


@app.route('/results')
def show_results():
    # Retrieve the saved answers from the session
    answers = session.get('answers', {})
    return render_template('results.html', answers=answers)


# # Route pour soumettre les réponses et calculer le score
# @app.route('/submit', methods=['POST'])
# def submit_quiz():
#     score = 0
#
#     # On parcourt les questions pour vérifier les réponses de l'utilisateur
#     # for i, q in questions:
#     for q in QUESTIONS:
#         # On récupère la réponse de l'utilisateur pour la question 'i'
#         # user_answer = request.form.get(f"question{i}")
#         user_answer = request.form.get(f"question: {q}")
#         # Si la réponse de l'utilisateur correspond à la bonne réponse, on incrémente le score
#         if user_answer == q['answer']:
#             score += 1
#
#     # On renvoie le résultat sur une autre page ou la même
#     return f"Ton score est de {score} sur {len(QUESTIONS)}."


if __name__ == '__main__':
    # A secret key is required for session security.
    app.secret_key = '57dcb026497fbae108daacaac229e8ef'
    # Get the secret key from an environment variable, with a fallback
    # app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'default_secret_key_for_dev')

    # Le mode debug permet de redémarrer le serveur automatiquement lors des modifications
    app.run(debug=True)
