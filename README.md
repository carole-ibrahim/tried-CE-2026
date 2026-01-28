# tried-CE-2026

Code des travaux pratiques pour le module CE du master TRIED (Janvier 2026).

## Contenu

Le dossier `notebooks_TP/` contient les TPs à réaliser dans l'ordre :

1.   **TP_simple_ML_model.ipynb** : Entraînement et sérialisation d'un modèle simple.
2.   **TP_introduction_FastAPI.ipynb** : Découverte des bases de FastAPI.
3.   **TP_FastAPI_Iris_Model.ipynb** : Création d'une API pour servir le modèle de classification Iris.
4.  **TP_Docker_FastAPI.md** : Création d'un docker pour encapsuler la FastAPI.

## Prérequis

*   Python 3.13 ou supérieur
*   Git
*   Au choix : `uv` (recommandé), `conda` ou `pip`

## Installation

### Option 1 : uv + make (Recommandé)

C'est la méthode la plus rapide.

```bash
make setup
```

### Option 2 : uv + scripts

**macOS / Linux**
```bash
chmod +x setup_scripts/bootstrap.sh
./setup_scripts/bootstrap.sh
```

**Windows (PowerShell)**
```bash
powershell setup_scripts/bootstrap.ps1
```

### Option 3 : Conda

```bash
conda create --name ml_in_prod python=3.13
conda activate ml_in_prod
pip install -r requirements.txt
```

### Option 4 : Pip (Manuel)

```bash
git clone https://github.com/carole-ibrahim/tried-CE-2026.git
cd tried-CE-2026
python -m venv venv
source venv/bin/activate  # Sur Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Docker

Docker est requis pour certaines parties.

*   **Mac / Windows** : Installez [Docker Desktop](https://docs.docker.com/desktop/).
*   **Linux** : Installez [Docker Engine](https://docs.docker.com/engine/install).

## Licence

Ce projet est sous licence MIT.
