# TP6 – Dataclasses Python
### Objectif
Apprendre à utiliser les dataclasses en Python pour modéliser des entités métiers réelles, en respectant l’immuabilité, la sérialisation JSON et la comparaison d’objets.

## Exercice 1 – Classe Livre
### Consignes
Créer une classe Livre avec les champs :
titre (str)
auteur (str)
prix (float)
L’objet doit être immuable (frozen=True) et optimisé (slots=True).
Ajouter une méthode promo(prix_reduit) qui retourne un nouveau livre avec le prix modifié.
Ajouter les méthodes to_json() et from_json() pour la sérialisation et la désérialisation JSON.
Permettre la comparaison des livres par prix (ordre croissant).

### Fonctionnalités principales
Immuabilité garantie par frozen=True.
Optimisation mémoire avec slots=True.
Tri possible grâce à order=True.
Sérialisation/désérialisation JSON.
Création de nouvelles instances modifiées avec promo().
<img width="689" height="187" alt="image" src="https://github.com/user-attachments/assets/bc492bb0-486d-42f1-b399-3708cdea4924" />

## Exercice 2 – Classe Film
### Consignes
Créer une classe Film avec les champs 
titre (str)
realisateur (str)
annee (int)
note (float de 0 à 10)
L’objet doit être immuable (frozen=True) et optimisé (slots=True).
Ajouter une méthode est_classique() qui retourne True si le film est antérieur à 2000.
Ajouter les méthodes to_json() et from_json() pour la sérialisation et la désérialisation JSON.
Ajouter une méthode promo(note_reduite) pour créer un nouveau film avec une note modifiée.
Implémenter une liste de films favoris et permettre leur tri par note croissante.

## Fonctionnalités principales
Validation des champs note et annee dans __post_init__.
Immuabilité et optimisation mémoire.
Tri possible grâce à order=True.
Sérialisation/désérialisation JSON.
Création de nouvelles instances modifiées avec promo().
Gestion d’une liste de favoris avec tri par note.
<img width="686" height="165" alt="image" src="https://github.com/user-attachments/assets/39a9b5f7-e404-4f41-9fd6-16ad5c9826a9" />
