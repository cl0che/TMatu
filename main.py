# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from clint.textui import colored, puts, prompt, validators


reponses = {}


def start():
    print("Bonjour, on va vous aider à faire un choix de metier!")
    choix = input("On continue? O/n  ")
    if choix == 'O' or choix == 'o':
        print("Allez c'est parti!")
    else:
        print("Au revoir")
        return

    manuel_intel = man_intel()
    int_ext = interieur_exterieur()

    puts('Voici vos réponses:')
    puts(' - ' + colored.green(manuel_intel.capitalize()))
    puts(' - ' + colored.green(int_ext.capitalize()))


def man_intel():
    choix = prompt.query('Tu prefères les metiers manuels ou intelectuels ? m/i', default='m')
    return 'manuel' if choix.lower() == 'm' else 'intelo'


def interieur_exterieur() -> str:
    choix = prompt.query('Plutôt en interieur ou en exterieur ? i/e', default='i')
    return 'interieur' if choix.lower() == 'i' else 'exterieur'


##########
## MAIN ##
##########
if __name__ == '__main__':
    start()
