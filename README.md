# Domain-Driven Design

## Définition des besoins

### 3 Niveaux d'utilisateurs
1. Rôle Administrateur \
Vu globale sur les différents écrans de l'application.

2. Rôle Analyste \
Comprendre les corélation, visualiser les graphiques

3. Créateur de playlist \
A partir d'une musique source et d'un pays cible, proposer une liste de musique similaire au créateur de playlist afin de s'implanter dans un pays en fonction des données musicale et démographique.

### Bounded context
- Analyse Musicale & Recommandation 
- Démographie et sociale
- Interface et visualisation

### Ubiquitous Language
Langage commun identifiant les termes métiers de l'application.
> `is_explicit` : Présence de contenu explicite d'une musique (langage vulgaire, violent, sexuel ou discriminatoire). \
> `danceability, energy, loudness, mode...` : Ensemble de termes relatant des données propre à une musique tels que le niveau d'énergie, le tempo, le mode harmonique, la présence de parole... \
> `social_media_pct` : Pourcentage de la population d'un pays active sur les réseaux sociaux.

## API REST

### Prérequis
pip install django-cors-headers

Pour lancer le projet :
> python manage.py runserver

> python manage.py migrate
> python manage.py createsuperuser
