# Guide TP : Servir un Modèle ML avec FastAPI 🚀

Ce guide accompagne le notebook `TP_FastAPI_Iris_Model.ipynb`. Vous allez apprendre à transformer un modèle de Machine Learning (notre classifieur Iris) en une API web utilisable par n'importe quelle application.

## Objectifs
- Créer une structure de données stricte pour l'entrée du modèle avec **Pydantic**.
- Implémenter une route API pour la prédiction.
- Comprendre les choix techniques : **POST vs GET** et **Sync vs Async**.

---

## Étape 1 : Préparation du Modèle
Dans le notebook, nous entraînons rapidement un modèle `RandomForest` simple au début. Dans la vraie vie, vous chargeriez un modèle sauvegardé (ex: `model.pkl`) créé par votre pipeline d'entraînement.

## Étape 2 : Définir le Contrat de Données (Pydantic)

**Tâche** : Complétez la classe `IrisInput`.

Le modèle a besoin de 4 caractéristiques (features) numériques pour fonctionner.
Au lieu d'accepter n'importe quel dictionnaire JSON, nous définissons un schéma strict.

**Pourquoi ?**
Si un utilisateur envoie du texte au lieu d'un nombre, ou oublie un champ, FastAPI retournera automatiquement une erreur claire (422 Unprocessable Entity) sans que vous ayez à écrire de "if/else" de validation.

---

## Étape 3 : Créer l'Endpoint de Prédiction

**Tâche** : Complétez la fonction `predict_species`.

### 1. Choix de la Méthode HTTP : pourquoi POST ?
Nous utilisons **POST** (et non GET) car nous envoyons des données (les caractéristiques de la fleur) dans le **corps (body)** de la requête.
*   *GET* : Pour lire/récupérer des données (paramètres dans l'URL).
*   *POST* : Pour envoyer/traiter des données (données dans le JSON body).

### 2. Sync (`def`) vs Async (`async def`)
C'est un point crucial en FastAPI pour le ML.

*   **`async def`** : À utiliser si votre code fait beaucoup d'attente (IO-bound) : appeler une autre API, une base de données asynchrone, etc. Pendant l'attente, FastAPI traite d'autres requêtes.
*   **`def` (Sync)** : À utiliser si votre code "calcule" (CPU-bound). C'est le cas typique de `model.predict()`. Scikit-learn bloque le processeur pendant le calcul.

**Si vous utilisez `async def` avec un modèle ML lourd** : Le serveur entier se fige pendant la prédiction.
**Si vous utilisez `def` (standard)** : FastAPI exécute intelligemment cette fonction dans un "threadpool" séparé, laissant le serveur réactif pour les autres utilisateurs.

**Conclusion** : Pour scikit-learn/pandas/numpy, utilisez **`def`**.

### 3. Post-processing
Le modèle retourne un chiffre (0, 1 ou 2). L'API doit être "compréhensible par un humain".
Transformez ce chiffre en nom d'espèce (`setosa`, `versicolor`, `virginica`) avant de le renvoyer.

---

## Étape 4 : Tester
Vérifiez que votre API fonctionne avec la commande `requests` fournie à la fin du notebook ou via Swagger UI (http://127.0.0.1:8000/docs).
