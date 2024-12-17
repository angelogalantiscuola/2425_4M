## Livelli di Progetto Python (1-3) <!-- omit in toc -->

- [Struttura Base Comune](#struttura-base-comune)
- [Setup Base](#setup-base)
- [README.md](#readmemd)
  - [Esempio di README.md](#esempio-di-readmemd)
- [Livello 1](#livello-1)
  - [Livello 1: To-Do List 📝](#livello-1-to-do-list-)
  - [Livello 1: Gestore Biblioteca 📚](#livello-1-gestore-biblioteca-)
- [Livello 2](#livello-2)
  - [Livello 2: Quiz Game 🎮](#livello-2-quiz-game-)
  - [Livello 2: Password Manager 🔑](#livello-2-password-manager-)
  - [Livello 2: Budget Tracker 💰](#livello-2-budget-tracker-)
  - [Livello 2: Image Gallery Manager 🖼](#livello-2-image-gallery-manager-)
- [Livello 3](#livello-3)
  - [Livello 3: Weather Dashboard 🌤](#livello-3-weather-dashboard-)
  - [Livello 3: Social Media Analytics 📊](#livello-3-social-media-analytics-)
  - [Livello 3: Blog Platform con Flask e SQLModel 📝](#livello-3-blog-platform-con-flask-e-sqlmodel-)


### Struttura Base Comune
```plaintext
project/
├── .gitignore
├── README.md
├── requirements.txt
├── src/
│   ├── __init__.py
│   ├── models/
│   ├── utils/
│   └── main.py
└── tests/
    └── __init__.py
```

### Setup Base
```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```


### README.md
Il file `README.md` deve essere ben documentato e spiegare il funzionamento del progetto. Deve includere:
1. Descrizione del progetto
2. Istruzioni per l'installazione
3. Esempi di utilizzo
4. Informazioni sugli autori
5. Licenza

#### Esempio di README.md
```markdown
# Nome del Progetto

## Descrizione
Breve descrizione del progetto e delle sue funzionalità principali.

## Installazione
Istruzioni per installare le dipendenze e configurare l'ambiente di sviluppo:

    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt

## Utilizzo
Esempi di utilizzo del progetto:

    python src/main.py

## Autori
- Nome Cognome - email@example.com

## Licenza
Questo progetto è distribuito sotto la licenza MIT. Vedi il file LICENSE per ulteriori dettagli.
```

### Livello 1

#### Livello 1: To-Do List 📝
**Steps:**
1. Classe Task con priorità e deadline
2. Salvataggio su file JSON
3. Operazioni CRUD basilari
4. Interfaccia da terminale
5. README.md ben documentato

```python
class Task:
    def __init__(self, title, priority=1, deadline=None):
        self.title = title
        self.priority = priority
        self.deadline = deadline
        self.completed = False

    def to_dict(self):
        return {
            "title": self.title,
            "priority": self.priority,
            "deadline": self.deadline,
            "completed": self.completed
        }
```

#### Livello 1: Gestore Biblioteca 📚
**Piano di Sviluppo:**
1. Classe semplice `Libro`
2. Salvataggio dati su file CSV
3. Operazioni base (aggiungi/rimuovi libri)
4. Menu testuale semplice
5. README.md ben documentato


```python
class Libro:
    def __init__(self, titolo, autore, anno):
        self.titolo = titolo
        self.autore = autore
        self.anno = anno
        self.prestato = False
```

### Livello 2


#### Livello 2: Quiz Game 🎮
**Piano di Sviluppo:**
1. Classi Question e Quiz
2. Caricamento domande da JSON
3. Sistema punteggio e timer
4. CLI colorata con `colorama`
5. README.md ben documentato

```python
from dataclasses import dataclass
import json
from typing import List
import colorama
from colorama import Fore, Style
import time

@dataclass
class Question:
    text: str
    options: List[str]
    correct_answer: int
    points: int = 1

class QuizGame:
    def __init__(self, quiz_file: str):
        self.questions = []
        self.score = 0
        self.load_questions(quiz_file)
        colorama.init()

    def load_questions(self, filename: str):
        with open(filename, 'r') as f:
            data = json.load(f)
            self.questions = [Question(**q) for q in data]

    def run(self):
        for q in self.questions:
            self.display_question(q)
            if self.check_answer(q):
                self.score += q.points
```


#### Livello 2: Password Manager 🔑
**Steps:**
1. Classi per Password e Categoria
2. Crittografia base con cryptography
3. Storage JSON criptato
4. CLI con click
5. README.md ben documentato

```python
from cryptography.fernet import Fernet

class PasswordManager:
    def __init__(self):
        self.key = Fernet.generate_key()
        self.cipher_suite = Fernet(self.key)
        self.passwords = {}

    def add_password(self, service, password):
        encrypted_pwd = self.cipher_suite.encrypt(password.encode())
        self.passwords[service] = encrypted_pwd
```



#### Livello 2: Budget Tracker 💰
**Piano di Sviluppo:**
1. Classi Transaction e Budget
2. Database SQLite
3. GUI con customtkinter
4. README.md ben documentato

```python
from datetime import datetime
import sqlite3
import customtkinter as ctk
from dataclasses import dataclass

@dataclass
class Transaction:
    amount: float
    category: str
    description: str
    date: datetime = datetime.now()
    type: str = "expense"  # expense/income

class BudgetTracker:
    def __init__(self, db_path: str):
        self.conn = sqlite3.connect(db_path)
        self.setup_database()
        
    def setup_database(self):
        cursor = self.conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY,
                amount REAL,
                category TEXT,
                description TEXT,
                date TEXT,
                type TEXT
            )
        """)
        self.conn.commit()

    def add_transaction(self, transaction: Transaction):
        cursor = self.conn.cursor()
        cursor.execute("""
            INSERT INTO transactions (amount, category, description, date, type)
            VALUES (?, ?, ?, ?, ?)
        """, (
            transaction.amount,
            transaction.category,
            transaction.description,
            transaction.date.isoformat(),
            transaction.type
        ))
        self.conn.commit()
```

#### Livello 2: Image Gallery Manager 🖼
**Piano di Sviluppo:**
1. Classe per gestione immagini
2. Miniature con `Pillow`
3. Metadata con `exif`
4. UI con `tkinter`
5. README.md ben documentato

```python
from PIL import Image
import os
from dataclasses import dataclass
from typing import List
import exif

@dataclass
class ImageInfo:
    filename: str
    path: str
    size: tuple
    format: str
    metadata: dict

class GalleryManager:
    def __init__(self, gallery_path: str):
        self.gallery_path = gallery_path
        self.thumbnails_path = os.path.join(gallery_path, "thumbnails")
        os.makedirs(self.thumbnails_path, exist_ok=True)
        
    def create_thumbnail(self, image_path: str, size=(128, 128)):
        with Image.open(image_path) as img:
            img.thumbnail(size)
            filename = os.path.basename(image_path)
            thumbnail_path = os.path.join(self.thumbnails_path, filename)
            img.save(thumbnail_path)
            
    def get_image_info(self, image_path: str) -> ImageInfo:
        with Image.open(image_path) as img:
            with open(image_path, 'rb') as img_file:
                exif_data = exif.Image(img_file)
            return ImageInfo(
                filename=os.path.basename(image_path),
                path=image_path,
                size=img.size,
                format=img.format,
                metadata=exif_data.get_all()
            )
```


### Livello 3

#### Livello 3: Weather Dashboard 🌤
**Steps:**
1. Classe WeatherData e Location
2. API OpenWeatherMap
3. Grafici con matplotlib
4. Cache con sqlite
5. README.md ben documentato

```python
import requests
from datetime import datetime

class WeatherData:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"

    def get_weather(self, city):
        params = {
            'q': city,
            'appid': self.api_key,
            'units': 'metric'
        }
        response = requests.get(self.base_url, params=params)
        return response.json()
```

#### Livello 3: Social Media Analytics 📊

**Step by Step:**
1. API Integration (Twitter/Reddit)
2. Data Collection & Storage
3. Sentiment Analysis
4. Visualizzazione Dati
5. Report Generator

```python
from textblob import TextBlob
import tweepy
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
import sqlite3

class SocialAnalyzer:
    def __init__(self, api_key, api_secret):
        self.auth = tweepy.OAuthHandler(api_key, api_secret)
        self.api = tweepy.API(self.auth)
        self.conn = sqlite3.connect('social_data.db')
        
    def analyze_topic(self, keyword, count=100):
        tweets = self.api.search_tweets(q=keyword, count=count)
        sentiments = []
        
        for tweet in tweets:
            analysis = TextBlob(tweet.text)
            sentiments.append({
                'text': tweet.text,
                'sentiment': analysis.sentiment.polarity,
                'date': tweet.created_at
            })
            
        return pd.DataFrame(sentiments)
```

#### Livello 3: Blog Platform con Flask e SQLModel 📝

**Step-by-Step Plan:**
1. Setup Progetto
   - Struttura cartelle
   - Dipendenze
2. Modelli Dati
   - User
   - Post
   - Comment
3. API Routes
4. Templates
5. Auth System

```plaintext


blog/
├── src/
│   ├── __init__.py
│   ├── models.py
│   ├── routes.py
│   ├── auth.py
│   └── templates/
│       ├── base.html
│       ├── index.html
│       └── post.html
└── requirements.txt
```

```python
from typing import Optional, List
from datetime import datetime
from sqlmodel import Field, Session, SQLModel, Relationship

class User(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str = Field(unique=True, index=True)
    password: str
    posts: List["Post"] = Relationship(back_populates="author")

class Post(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str
    content: str
    image_path: Optional[str]
    created_at: datetime = Field(default_factory=datetime.utcnow)
    author_id: int = Field(foreign_key="user.id")
    author: User = Relationship(back_populates="posts")
    comments: List["Comment"] = Relationship(back_populates="post")

class Comment(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    content: str
    created_at: datetime = Field(default_factory=datetime.utcnow)
    post_id: int = Field(foreign_key="post.id")
    post: Post = Relationship(back_populates="comments")
```

```python
from flask import Flask, render_template, request
from sqlmodel import Session, select
from .models import Post, User, Comment
from .database import engine

app = Flask(__name__)

@app.route("/posts")
def list_posts():
    with Session(engine) as session:
        statement = select(Post).order_by(Post.created_at.desc())
        posts = session.exec(statement).all()
        return render_template("index.html", posts=posts)

@app.route("/api/posts", methods=["GET"])
def api_posts():
    with Session(engine) as session:
        statement = select(Post)
        posts = session.exec(statement).all()
        return [post.dict() for post in posts]

@app.route("/post/<int:post_id>")
def view_post(post_id: int):
    with Session(engine) as session:
        post = session.get(Post, post_id)
        return render_template("post.html", post=post)
```

```
flask==2.0.1
sqlmodel==0.0.8
python-jose==3.3.0
python-multipart==0.0.5
python-dotenv==0.19.0
pillow==8.3.1
```

```html
{% extends "base.html" %}
{% block content %}
<div class="container mt-4">
    <article>
        <h1>{{ post.title }}</h1>
        {% if post.image_path %}
        <img src="{{ url_for('static', filename=post.image_path) }}" class="img-fluid">
        {% endif %}
        <div class="content mt-3">
            {{ post.content }}
        </div>
        <small class="text-muted">
            Posted by {{ post.author.username }} on {{ post.created_at.strftime('%Y-%m-%d') }}
        </small>
    </article>
</div>
{% endblock %}
```