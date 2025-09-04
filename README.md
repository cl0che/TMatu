# Travail de Maturité de Chloé

---

Mise en place de l'environnement:

````shell
# Installer uv
brew install uv

# Créer l'environnement virtuel
uv venv
# Activer l'environnement virtuel
source .venv/bin/activate

# Installer les dépendances
uv sync
````

Exécution:

````shell
uv run main.py
````
