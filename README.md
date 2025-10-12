# Travail de Maturité de Chloé

---

Mise en place de l'environnement local:

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

Exécution local en mode graphique:

````shell
uv run app.py
````
puis clickez sur: http://127.0.0.1:5000

Ctrl-C pour arreter.

---

Exécution local en mode texte:

````shell
uv run main.py
````

---


Mise à jour et exécution depuis serveur distant:

````shell
# Connection au serveur distant
ssh -i ~/.ssh/private_key ubuntu@xxx.xxx.xxx.xxx

# Installation d'uv
sudo snap install astral-uv --classic
# Récuperation du code
git clone https://github.com/cl0che/TMatu.git
cd TMatu/
uv sync
# Création fichier d'environnement
echo "FLASK_PORT=5000" > .env
echo "FLASK_HOST=xxx.xxx.xxx.xxx" >> .env
echo "FLASK_SECRET_KEY=default_secret_key_for_dev" >> .env
# Execution en arrière plan
nohup uv run --env-file .env app.py &
# Visualisation des logs
tail -f nohup.out

# Retrouver le process
ps -ef | grep nohup
# Stopper le process
kill -9 XXXXX
````
