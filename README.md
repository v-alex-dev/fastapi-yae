# FastAPI Learning Project

## 1. Création de l'environnement virtuel

```bash
python -m venv venv
source venv/bin/activate   # Linux / Mac
venv\Scripts\activate      # Windows
```

## 2. Installation des dépendances

```bash
pip install -r requirements.txt
```

## 3. Configuration

Copier le fichier `.env.example` en `.env` et adapter les valeurs
à votre installation PostgreSQL locale :

```bash
cp .env.example .env
```

## 4. Lancement du serveur

```bash
uvicorn app.main:app --reload
```

L'API est alors disponible sur http://127.0.0.1:8000
La documentation interactive (Swagger) sur http://127.0.0.1:8000/docs

## 5. Test du endpoint de santé

```bash
curl http://127.0.0.1:8000/health/
```
