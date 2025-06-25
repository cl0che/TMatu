# Liste des métiers

Source Onisep: https://www.data.gouv.fr/fr/datasets/ideo-metiers-onisep/
En json données brutes: https://www.data.gouv.fr/fr/datasets/r/654b0138-da15-49a4-ab8e-c5662fa47349

## Filtrage des données

```json
  {
    "libelle_metier": "formateur \/ formatrice technique en agro\u00e9quipement",
    "lien_site_onisepfr": "https:\/\/www.onisep.fr\/http\/redirection\/metier\/slug\/MET.118",
    "nom_publication": "Les m\u00e9tiers de l'automobile",
    "collection": "Parcours",
    "annee": 2020,
    "gencod": 9782273015172,
    "gfe": "GFE A : agriculture",
    "code_rome": "",
    "libelle_rome": "",
    "lien_rome": "",
    "domainesous-domaine": "m\u00e9canique\/machinisme agricole| mati\u00e8res premi\u00e8res, fabrication, industries\/maintenance, qualit\u00e9| m\u00e9canique\/m\u00e9canique (g\u00e9n\u00e9ralit\u00e9s)"
  }
```

Filtrer les données brutes pour ne conserver que:
- ***libelle_metier***
- ***domainesous-domaine***

On a ainsi la liste de métiers avec pour chacun, ses catégories.


Ensuite, pour aider à construire les questions, il faut regrouper les domaines pour ne conserver qu'une liste de domaine unique.

De pôle emploi en json: http://www.nosdonnees.fr/dataset/51f20c04-79e5-471c-bdcc-6ed91757122b/resource/a4031fcf-0ded-47df-9d88-870c06c8321e/download/codesrometree.xls.json


