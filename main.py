from operator import truediv

import yaml
from pprint import pprint
from clint.textui import colored, puts, prompt, validators
from common import *


def ask_1(question: dict, categories: list[str]):
    description: str = f" ({question['description']})" if question['description'] else ''
    response = prompt.query(
        f"{colored.green(question['question'])}{description}  " + colored.green('o') + '/' + colored.red('n'),
        default='o')
    if response.lower() == 'o':
        _to_add = question['categories_ajout']
        for _category in _to_add:
            if _category not in categories:
                categories.append(_category)


def is_domain_in_user_categories(question_domain: str, user_categories: list[str], all_domains: list):
    # Les catégories de la question sont elles présentes dans les catégories des réponses de l'utilisateur?
    for _item in all_domains:
        if _item['domain'] == question_domain:
            _question_domains = _item['categories']

            for _user_category in user_categories:
                if _user_category in _question_domains:
                    return True

    print(f"  ------> Domain '{question_domain}' is not in user categories, ignoring question")
    return False


def ask_2(question: dict, categories: list[str], domains: list):
    if question:
        _domain: str = question['domain']
        if is_domain_in_user_categories(_domain, categories, domains):
            response = prompt.query(
                f"{colored.green(question['question'])} ({_domain}) " + colored.green('o') + '/' + colored.red('n'),
                default='o')
            if response.lower() == 'o':
                _to_remove = question['categories_retrait_oui']
            else:
                _to_remove = question['categories_retrait_non']
            for _category in _to_remove:
                if _category in categories:
                    categories.remove(_category)


def show_jobs(categories: list):
    _all_jobs: dict = load_jobs()
    _jobs: set = set()
    for category in categories:
        for _item in _all_jobs:
            if category in _item['categories']:
                _jobs.add(_item['metier'])

    # Tri des résultats
    _jobs_lst: list = list(_jobs)
    _jobs_lst.sort()

    # Affichage des métiers
    for job in _jobs_lst:
        print(f" - " + colored.cyan(job))


def start():
    print("\n\nBonjour, on va vous aider à faire un choix de metier!")
    choix = prompt.query('On continue? ' + colored.green('o') + '/' + colored.red('n') + '  ', default='o')
    if choix.lower() == 'o':
        print("Allez c'est parti!")
        print('')
        print('__________________________________________________________________')
        print('')
    else:
        print("Au revoir")
        return

    categories: list[str] = []

    # Questions 1 - determiner les catégories favorites
    questions: dict = load_questions_1()
    for question in questions:
        ask_1(question, categories)

    print("\n\n")
    if len(categories) == 0:
        print("Bon, au vu des réponses: Rentier !!!")
        return
    else:
        puts(f"D'après vos réponses, on a {len(categories)} catégorie(s) retenue(s). ")
        puts(colored.green('On va essayer d\'afiner ces réponses.'))
        # print("D'après vos réponses, voici la/les categorie(s) retenue(s): ")
        input('Appuyez sur [Entrée] ...')

    categories.sort()
    pprint(categories, indent=2, sort_dicts=True, compact=True, width=80)
    # categories.append('santé')
    # categories.append('agriculture')

    print('')
    print('__________________________________________________________________')
    print('')

    domains: dict = load_domains()

    # Questions 2 - afiner les catégories
    questions: dict = load_questions_2()
    for question in questions:
        ask_2(question, categories, domains)

    puts(f"D'après vos réponses, on a maintenant {len(categories)} catégorie(s) retenue(s). ")
    # for _category in categories:
    #     print(f" - {_category}")

    pprint(categories, indent=2, sort_dicts=True, compact=True, width=80)

    print("Cela correspond aux métiers suivants:")
    show_jobs(categories)


##########
## MAIN ##
##########
if __name__ == '__main__':
    start()
