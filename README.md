# Travail de Maturité de Chloé

---

Mise en place de l'environnement:

````shell
# Installer uv MacOS
brew install uv

# Créer l'environnement virtuel
uv venv
# Activer l'environnement virtuel
source .venv/bin/activate

# Installer les dépendances
uv sync
````

---

Exécution en mode graphique:

````shell
uv run app.py
````
puis clickez sur: http://127.0.0.1:5000

Ctrl-C pour arreter.

---

Exécution en mode texte:

````shell
uv run main.py
````

---
