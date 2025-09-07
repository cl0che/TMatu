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


def load_domains() -> list:
    with open("data/categories_by_domains.yaml") as yaml_file:
        return yaml.safe_load(yaml_file)


def load_jobs() -> dict:
    with open("data/jobs_onisep.yaml") as yaml_file:
        return yaml.safe_load(yaml_file)

