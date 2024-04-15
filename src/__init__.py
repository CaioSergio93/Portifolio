from flask import Flask

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sua_chave_secreta'

from src.routes import routes
app.register_blueprint(routes)
app = Flask(__name__, template_folder='templates')
