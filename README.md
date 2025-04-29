# Domain-Driven Design

## Présentation globale

| Catégorie                   | Type de donnée                                               |
| --------------------------- | ------------------------------------------------------------ |
| **Musique**                 | Propriétés des musiques (Dansabilité, tempo...)              |
| **Utilisation des réseaux** | Part de la population utilisant les réseaux sociaux par pays |
| **Démographie**             | Répartition d'âge par pays                                   |

## Bounded contexts
- Création de playlists
- Analyse des données par pays
- Gestion des utilisateurs

## Rôles

| Permission \ Rôle              | playlist_creator | analyst | admin |
| :----------------------------- | :--------------: | :-----: | :---: |
| **Génération de playlists**    |        ✅         |    ❌    |   ✅   |
| **Accès aux données par pays** |        ❌         |    ✅    |   ✅   |
| **Gestion des utilisateurs**   |        ❌         |    ❌    |   ✅   |


## 🎵 Ubiquitous Language - Domaine "Musique & Données Sociales"
### Entités

- **Song (Chanson)** :  
  Représente une chanson disponible sur Spotify, enrichie d'attributs audio, de données d'album et de popularité, spécifique à un pays donné.

- **CountryStats (StatistiquesPays)** :  
  Représente un ensemble agrégé de caractéristiques musicales moyennes et de données démographiques pour un pays donné.

---

### Objets Métiers et Concepts Clés

| Terme métier               | Définition                                                                       |
| -------------------------- | -------------------------------------------------------------------------------- |
| **Spotify ID**             | Identifiant unique d'une chanson sur Spotify.                                    |
| **Nom complet du pays**    | Dénomination complète du pays lié à la chanson (ex: "United States of America"). |
| **Code du pays**           | Code ou abréviation simplifiée du pays en 2 caractères (ex: "US").               |
| **Nom de la chanson**      | Titre officiel de la chanson.                                                    |
| **Artistes**               | Liste des artistes associés à la chanson (séparés par une virgule).              |
| **Popularité**             | Score de popularité de la chanson sur Spotify (entre 0 et 100).                  |
| **Contenu explicite**      | Indicateur si la chanson contient du contenu explicite (`true` ou `false`).      |
| **Durée (ms)**             | Durée de la chanson en millisecondes.                                            |
| **Nom de l'album**         | Titre de l'album contenant la chanson.                                           |
| **Date de sortie d'album** | Date officielle de sortie de l'album. (YYYY-MM-DD)                               |

---

### Caractéristiques Audio d’une Chanson

| Attribut audio       | Signification                                                                  |
| -------------------- | ------------------------------------------------------------------------------ |
| **Danceability**     | Aptitude d'une chanson à faire danser (0.0 à 1.0).                             |
| **Energy**           | Niveau d'énergie globale de la chanson (0.0 à 1.0).                            |
| **Key**              | Tonalité musicale principale (notation numérique standardisée de 0 à 11).      |
| **Loudness**         | Volume moyen de la chanson (en dB). (Négatif ou positif)                       |
| **Mode**             | Mode musical : majeur (1) ou mineur (0).                                       |
| **Speechiness**      | Proportion de paroles parlées dans la chanson (0.0 à 1.0).                     |
| **Acousticness**     | Probabilité que la chanson soit acoustique (0.0 à 1.0).                        |
| **Instrumentalness** | Probabilité que la chanson soit instrumentale (0.0 à 1.0).                     |
| **Liveness**         | Probabilité que la chanson soit enregistrée en live / avec public (0.0 à 1.0). |
| **Valence**          | Positivité/joie véhiculée par la chanson (0.0 à 1.0).                          |
| **Tempo**            | Vitesse du morceau (en BPM).                                                   |
| **Time Signature**   | Nombre de temps par mesure musicale.                                           |

---

### Caractéristiques Sociales et Démographiques d'un Pays

| Attribut               | Définition                                                   |
| ---------------------- | ------------------------------------------------------------ |
| **Social Media Users** | Nombre total d'utilisateurs de réseaux sociaux dans le pays. |
| **Social Media %**     | Pourcentage de la population utilisant les réseaux sociaux.  |
| **Total Population**   | Population totale du pays.                                   |
| **Âge 0-4**            | Pourcentage de la population âgée de 0 à 4 ans.              |
| **Âge 5-14**           | Pourcentage de la population âgée de 5 à 14 ans.             |
| **Âge 15-24**          | Pourcentage de la population âgée de 15 à 24 ans.            |
| **Âge 25-64**          | Pourcentage de la population âgée de 25 à 64 ans.            |
| **Âge 65+**            | Pourcentage de la population âgée de plus de 65 ans.         |

---

# API REST
## Endpoints

### Authentification
```bash
http://localhost:8000/api/auth/login/ # POST 
{
  "username": "analyst",
  "password": "analyst"
}
```
```bash
http://localhost:8000/api/auth/logout/ # DELETE 

Headers{
  'Authorization': 'Token {token}'
}
```
```bash
http://localhost:8000/api/auth/groups/ # GET 
Headers{
  'Authorization': 'Token {token}'
}
```
### Pays
```bash
http://localhost:8000/countries/ # GET 
Headers{
  'Authorization': 'Token {token}'
}
```
```bash
http://localhost:8000/countries/names # GET 
Headers{
  'Authorization': 'Token {token}'
}
```
```bash
http://localhost:8000/countries/{name}/songs # GET 
Headers{
  'Authorization': 'Token {token}'
}
```
### Sons
```bash
http://localhost:8000/api/songs/generate-playlist/ # POST 
Headers{
  'Authorization': 'Token {token}'
}
```
### Utilisateurs
```bash
http://localhost:8000/api/users/ # GET 
Headers{
  'Authorization': 'Token {token}'
}
```
```bash
http://localhost:8000/api/users/{id} # DELETE 
Headers{
  'Authorization': 'Token {token}'
}
```

### Prérequis

Les librairies nécessaires pour ce projet sont dans le fichier requirements.txt.

- Pour lancer le projet :
> python manage.py runserver \
> python manage.py migrate \
> python manage.py createsuperuser

---

# Front
### Prérequis
Lancer les commandes suivantes afin de lancer le projet:

> npm install \
> npm run dev

# Utilisateurs par défaut
Liste des utilisateurs:
| Username             | Mot de passe     | Rôles            |
| -------------------- | ---------------- | ---------------- |
| **admin**            | admin            | admin            |
| **analyst**          | analyst          | analyst          |
| **playlist_creator** | playlist_creator | playlist_creator |
