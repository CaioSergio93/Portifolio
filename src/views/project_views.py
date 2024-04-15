from flask import render_template
from src.models.project import Project
from src import app

@app.route('/')
def index():
    projects = [...]  # Obtenha projetos do banco de dados ou de outro lugar
    return render_template('index.htm', projects=projects)
