from flask import render_template
from src.routes import routes
from src.controllers.project_controller import ProjectController

@routes.route('/')
def index():
    projects = ProjectController.get_all_projects()
    github_link = "https://github.com/CaioSergio93/my-profiles-web-node/tree/master"
    hosting_link = "https://my-profiles-web-node.vercel.app/"
    return render_template('index.htm', projects=projects,
                               github_link=github_link, hosting_link=hosting_link)
