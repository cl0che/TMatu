# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import yaml
from clint.textui import colored, puts, prompt, validators


reponses = {}

def load_questions() -> dict:
    with open("data/questions_niveau1.yaml") as yaml_file:
        return yaml.safe_load(yaml_file)


def load_categories() -> list:
    with open("data/categories.yaml") as yaml_file:
        return yaml.safe_load(yaml_file)


def start():
    print("Bonjour, on va vous aider à faire un choix de metier!")
    choix = input("On continue? O/n  ")
    if choix == 'O' or choix == 'o':
        print("Allez c'est parti!")
    else:
        print("Au revoir")
        return

    # categories: list = load_categories()
    categories: list[str] = []
    questions: dict = load_questions()
    for question in questions:
        print(f"{question['question']} o/n")
        if question['description']:
            print(f"  {question['description']}")
        response = input(f" ->  ")
        if response == 'o' or response == 'O':
            _to_add = question['categories_ajout']
            for _category in _to_add:
                if _category in categories:
                    categories.append(_category)

    print("\n\n")
    if len(categories)==0:
        print("Bon, au vu des réponses : Rentier !!!")
    else:
        print("D'après vos réponses, voici la/les categorie(s) retenue(s): ")
        for _category in categories:
            print(f" - {_category}")

   # manuel_intel = man_intel()
   # int_ext = interieur_exterieur()

   # puts('Voici vos réponses:')
    #puts(' - ' + colored.green(manuel_intel.capitalize()))
   # puts(' - ' + colored.green(int_ext.capitalize()))


#def man_intel():
   # choix = prompt.query('Tu prefères les metiers manuels ou intelectuels ? m/i', default='m')
   # return 'manuel' if choix.lower() == 'm' else 'intelo'


#def interieur_exterieur() -> str:
    #choix = prompt.query('Plutôt en interieur ou en exterieur ? i/e', default='i')
   # return 'interieur' if choix.lower() == 'i' else 'exterieur'


##########
## MAIN ##
##########
if __name__ == '__main__':
    start()

# import json
#
# # Charger le fichier JSON
# with open("jobs_onisep_raw.json", "r", encoding="utf-8") as f:
#     data = json.load(f)
#
# # Extraire les champs souhaités
# resultat = []
# for item in data:
#     if "libelle_metier" in item and "domainesous-domaine" in item:
#         resultat.append({
#             "libelle_metier": item["libelle_metier"],
#             "domainesous-domaine": item["domainesous-domaine"]
#         })
#
# # Afficher ou utiliser le résultat
# #for r in resultat:
#    # print(r)
#
#
# # Rechercher le métier "acheteur"
# for item in data:
#     if item.get("libelle_metier", "").lower() == "acheteur":
#         print("Domaine sous-domaine :", item.get("domainesous-domaine"))
#         break
#
# count = 0
# for item in data:
#     if "acheteur" in item.get("libelle_metier", "").lower():
#         count += 1
# print("Nombre de métiers contenant 'acheteur' :", count)
#
# # Stocker les domaines sans répétition
# #domaines_uniques = set()
#
# # Parcourir tous les éléments
# #for item in data:
#    # domaine = item.get("domainesous-domaine")
#     #if domaine:
#       #  domaines_uniques.add(domaine)
#
# # Afficher les résultats sans doublons
# #for domaine in sorted(domaines_uniques):
#     #print(domaine)
#
