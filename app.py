import os

from flask import Flask, render_template, request, redirect, url_for, session
from common import *

app = Flask(__name__)

QUESTIONS_1: dict = load_questions_1()
QUESTIONS_2: dict = load_questions_2()

categories: list[str] = []
domains: dict = load_domains()
jobs: list = load_jobs()


@app.route('/')
def start_survey():
    # Clear any previous session data and start the survey
    session.clear()
    session['current_question_step1'] = 0
    session['answers_step1'] = {}
    session['current_question_step2'] = 0
    session['answers_step2'] = {}
    session['categories'] = []
    session['domains'] = {}
    return redirect(url_for('ask_step1'))


@app.route('/step2')
def start_step2():
    # Clear any previous step2 session data and start the step2
    session['current_question_step2'] = 0
    session['answers_step2'] = {}
    session['domains'] = load_domains()
    return redirect(url_for('ask_step2'))


@app.route('/ask_step1', methods=['GET', 'POST'])
def ask_step1():
    current_q_index = session.get('current_question_step1', 0)

    # Check if all questions have been asked
    if current_q_index >= len(QUESTIONS_1):
        return redirect(url_for('show_results_step1'))

    question_text = QUESTIONS_1[current_q_index]['question']
    description = QUESTIONS_1[current_q_index]['description']

    if request.method == 'POST':
        # Get the answer from the form
        user_answer = request.form['answer']

        # Save the answer to the session dictionary
        session['answers_step1'][question_text] = user_answer

        if user_answer == 'Oui':
            _to_add = QUESTIONS_1[current_q_index]['categories_ajout']
            for _category in _to_add:
                if _category not in categories:
                    categories.append(_category)
            session['categories'] = categories

        # Increment the question index for the next question
        session['current_question_step1'] += 1

        # Redirect back to the question route to display the next question
        return redirect(url_for('ask_step1'))

    # For a GET request, render the question page
    return render_template('question_step1.html', question=question_text, description=description)


@app.route('/ask_step2', methods=['GET', 'POST'])
def ask_step2():
    current_q_index = session.get('current_question_step2', 0)

    # Check if all questions have been asked
    if current_q_index >= len(QUESTIONS_2):
        return redirect(url_for('show_results_step2'))

    question_text = QUESTIONS_2[current_q_index]['question']
    _domain: str = QUESTIONS_2[current_q_index]['domain']

    if is_domain_in_user_categories(_domain, categories, domains):

        if request.method == 'POST':
            # Get the answer from the form
            user_answer = request.form['answer']

            if user_answer.lower() == 'oui':
                _to_remove = QUESTIONS_2[current_q_index]['categories_retrait_oui']
            else:
                _to_remove = QUESTIONS_2[current_q_index]['categories_retrait_non']

            for _category in _to_remove:
                if _category in categories:
                    categories.remove(_category)
            session['categories'] = categories

            # Save the answer to the session dictionary
            session['answers_step2'][question_text] = user_answer

            # Increment the question index for the next question
            session['current_question_step2'] += 1

            # Redirect back to the question route to display the next question
            return redirect(url_for('ask_step2'))

        # For a GET request, render the question page
        return render_template('question_step2.html', question=question_text, domain=_domain, categories=categories)

    session['current_question_step2'] += 1
    return redirect(url_for('ask_step2'))


@app.route('/results_step1')
def show_results_step1():
    # Retrieve the saved answers from the session
    answers = session.get('answers_step1', {})
    return render_template('results_step1.html', answers=answers)


@app.route('/results_step2')
def show_results_step2():
    # Retrieve the saved answers from the session
    answers = session.get('answers_step2', {})
    return render_template('results_step2.html', answers=answers)


def retrieve_jobs(categories: list):
    _all_jobs: list = load_jobs()
    _jobs: set = set()
    for category in categories:
        for _item in _all_jobs:
            if category in _item['categories']:
                _jobs.add(_item['metier'])

    # Tri des résultats
    _jobs_lst: list = list(_jobs)
    _jobs_lst.sort()
    return _jobs


@app.route('/view_results')
def view_results():
    #
    _results: dict = {}
    _categories = session.get('categories', {})
    _categories.sort()
    _domains_set: set = set()

    for _category in _categories:
        _domain = get_domain_from_category(_category, domains)
        _domains_set.add(_domain)
        _jobs = get_jobs_from_category(_category, jobs)
        if _domain in _results:
            _cats: dict = _results[_domain]
            _cats[_category] = _jobs
        else:
            _cats: dict = {_category: _jobs}
        _results[_domain] = _cats

    if len(_results) == 0:
        _results = {'Rêve': {'Inaccessible': ['Rentier']}}

    return render_template('view_results.html', results=_results)


if __name__ == '__main__':
    # A secret key is required for session security.
    # Get the secret key from an environment variable, with a fallback
    app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'default_secret_key_for_dev')

    _port = os.environ.get('FLASK_PORT')
    _host = os.environ.get('FLASK_HOST')

    # Le mode debug permet de redémarrer le serveur automatiquement lors des modifications
    app.run(host=_host, port=_port, debug=False)