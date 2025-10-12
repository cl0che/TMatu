import yaml


def load_questions_1() -> dict:
    with open("data/questions_niveau1.yaml") as yaml_file:
        return yaml.safe_load(yaml_file)


def load_questions_2() -> dict:
    with open("data/questions_niveau2.yaml") as yaml_file:
        return yaml.safe_load(yaml_file)


def load_categories() -> list:
    with open("data/categories.yaml") as yaml_file:
        return yaml.safe_load(yaml_file)


def load_domains() -> dict:
    with open("data/categories_by_domains.yaml") as yaml_file:
        return yaml.safe_load(yaml_file)


def load_jobs() -> list:
    with open("data/jobs_onisep.yaml") as yaml_file:
        return yaml.safe_load(yaml_file)


def is_domain_in_user_categories(question_domain: str, user_categories: list[str], all_domains: dict):
    # Les catégories de la question sont elles présentes dans les catégories des réponses de l'utilisateur?
    for _item in all_domains:
        if _item['domain'] == question_domain:
            _question_domains = _item['categories']

            for _user_category in user_categories:
                if _user_category in _question_domains:
                    return True

    print(f"  ------> Domain '{question_domain}' is not in user categories, ignoring question")
    return False


def get_domain_from_category(category: str, all_domains: dict):
    for _item in all_domains:
        for _catgory in _item['categories']:
            if _catgory == category:
                return _item['domain']
    return None


def get_jobs_from_category(category: str, all_jobs: list) -> list:
    _jobs_set: set = set()
    for _item in all_jobs:
        if category in _item['categories']:
            _jobs_set.add(_item['metier'])
    _jobs: list = list(_jobs_set)
    _jobs.sort()
    return _jobs
