from flask import Flask, render_template
from src.controllers.project_controller import ProjectController

app = Flask(__name__)

@app.route('/')
def index():
    projects = ProjectController.get_all_projects()
    return render_template('index.htm', projects=projects)

@app.route('/test')
def about():
    return 'About page'

if __name__ == '__main__':
    app.run(debug=True)
