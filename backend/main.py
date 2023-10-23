# main.py
from flask import Flask
from blueprints.basic_endpoints import blueprint as basic_endpoints
from blueprints.jinja_endpoint import blueprint as jinja_template_blueprint
from blueprints.login_endpoints import blueprint as login

app = Flask(__name__)
app.register_blueprint(basic_endpoints)
app.register_blueprint(jinja_template_blueprint)
app.register_blueprint(login)

if __name__ == "__main__":
    app.run()