# Guide TP : Introduction à FastAPI

Ce guide accompagne le notebook `3-introduction_to_fastapi_student.ipynb`. Votre objectif est de comprendre les bases de FastAPI en complétant les parties de code manquantes et en répondant aux questions de compréhension.

## Objectifs Pédagogiques
- Comprendre la structure d'une application FastAPI.
- Créer des routes API (GET, POST, PUT, DELETE).
- Utiliser la validation de données avec Pydantic.
- Manipuler les paramètres de chemin (Path) et de requête (Query).

---

## Partie 1 : Création de la première application (First App)

**Contexte** : Une application FastAPI commence toujours par une instance de la classe `FastAPI`.

**Tâche 1** : Dans la section **2. Creating Your First FastAPI App**, complétez la fonction `read_root`.
- La fonction doit retourner un dictionnaire JSON simple (ex: `{"message": "Hello World"}`).

**Question 1** : À quelle URL pouvez-vous consulter la documentation automatique (Swagger UI) une fois le serveur lancé ?

---

## Partie 2 : Méthodes HTTP (GET)

**Contexte** : La méthode GET est utilisée pour récupérer des données.

**Tâche 2** : Dans la section **3. Understanding HTTP Methods**, complétez la fonction `get_item`.
- Vérifiez si l'`item_id` existe dans `items_db`.
- Si non, levez une `HTTPException` avec le code 404.
- Si oui, retournez l'objet correspondant.

---

## Partie 3 : Modèles Pydantic et POST

**Contexte** : Pydantic permet de valider les données entrantes. POST est utilisé pour créer des ressources.

**Tâche 3** : Dans la section **4. Pydantic Models for Request/Response**, complétez la fonction `create_item`.
- Générez un nouvel ID (auto-incrément).
- Ajoutez le nouvel item dans `items_db`.
- Retournez l'objet créé en respectant le `response_model`.

**Question 2** : Quel est l'avantage d'utiliser un modèle Pydantic comme `Item` en paramètre de la fonction plutôt qu'un simple dictionnaire ?

---

## Partie 4 : Mise à jour et Suppression (PUT & DELETE)

**Contexte** : PUT remplace/met à jour une ressource, DELETE la supprime.

**Tâche 4** : Dans la section **5. Path Parameters vs Query Parameters** (Note: dans le notebook étudiant, ceci pourrait être une section dédiée PUT/DELETE), complétez `update_item` et `delete_item`.
- Pour `update_item` : Mettez à jour les champs de l'objet existant avec les nouvelles valeurs fournies. Gérer le cas où l'objet n'existe pas.
- Pour `delete_item` : Supprimez l'objet du dictionnaire `items_db` et retournez un message de confirmation.

---

## Partie 5 : Paramètres de Requête (Query Parameters)

**Contexte** : Les paramètres de requête ("?q=...") sont souvent utilisés pour le filtrage ou la recherche.

**Tâche 5** : Dans la section sur les paramètres de requête, complétez la logique de filtrage dans `search_items`.
- Si `q` est fourni, filtrez les items dont le nom contient la chaîne `q`.
- Si `min_price` est fourni, ne gardez que les items dont le prix est supérieur.

**Question 3** : Quelle est la différence fondamentale entre un paramètre de chemin (ex: `/items/{item_id}`) et un paramètre de requête (ex: `/items?q=abc`) ?

---

## Exercices Avancés (Bonus)

Si vous avez terminé le notebook :
1. Ajoutez un endpoint `/health` qui retourne `{"status": "ok"}`.
2. Ajoutez un champ `category` au modèle `Item` et essayez de créer un nouvel objet avec ce champ.

## Vérification

À la fin du notebook, exécutez la section **8. Testing Our API** pour vérifier que toutes vos implémentations passent les tests (codes 200/201 et non 404/500).
