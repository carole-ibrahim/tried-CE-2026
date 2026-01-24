# tried-CE-2026

Repository containing the practical work code for the CE module intervention in the TRIED master's program (January 2026).

## 📋 Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Running the Project](#running-the-project)
- [Contributing](#contributing)
- [License](#license)

## Overview

This repository contains practical exercises and solutions for the **Citizen Engineering (CE)** module, part of the TRIED (Transforming Research into Engineering and Data) master's program.

**Tech Stack:**
- Python 3.13+
- FastAPI (API framework)
- MLflow (ML tracking)
- Scikit-learn (ML library)
- Pandas (data processing)

## Prerequisites

- Python 3.13 or higher
- Git
- One of the following package managers:
  - `uv` + `make` (recommended)
  - `conda`
  - `pip`

## Installation

### Option 1: Using uv + make (Recommended) ⭐

The fastest and simplest setup method:

```bash
make setup
```

### Option 2: Using uv + bash scripts

#### macOS / Linux
```bash
chmod +x setup_scripts/bootstrap.sh
./setup_scripts/bootstrap.sh
```

#### Windows (PowerShell)
```bash
pwsh setup_scripts/bootstrap.ps1
```

Or with execution policy bypass:
```bash
pwsh -ExecutionPolicy Bypass setup_scripts/bootstrap.ps1
```

### Option 3: Using conda

1. Install conda if not already installed by following the [conda-forge documentation](https://conda-forge.org/download/)

2. Create a new conda environment and install requirements:
```bash
conda create --name ml_in_prod --file requirements.txt
conda activate ml_in_prod
```

### Option 4: Using pip (Manual setup)

```bash
git clone https://github.com/carole-ibrahim/tried-CE-2026.git
cd tried-CE-2026
pip install virtualenv
virtualenv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

## Install Docker:
Make sure you have docker installed on your machine, for Mac users, download the docker desktop app (emulates docker like a linux machine)
[install docker desktop ](https://docs.docker.com/desktop/) (easier for all platforms) otherwise for linux users you can install [docker engine](https://docs.docker.com/engine/install)

## License

This project is licensed under the terms of the MIT License.
