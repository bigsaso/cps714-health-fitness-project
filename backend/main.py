# main.py
from flask import Flask
from blueprints.basic_endpoints import blueprint as basic_endpoints
from blueprints.jinja_endpoint import blueprint as jinja_template_blueprint
from blueprints.login_endpoints import blueprint as login
from blueprints.sleep_data_api import blueprint as sleep_data_api
from blueprints.steptracker_api import blueprint as steptracker_api
from blueprints.exercise_api import exercise_api as exercise_api
#from blueprints.mood_api import blueprint as mood_api
from blueprints.calorie_api import blueprint as calorie_api

app = Flask(__name__)
app.register_blueprint(basic_endpoints)
app.register_blueprint(jinja_template_blueprint)
app.register_blueprint(login)
app.register_blueprint(sleep_data_api)
app.register_blueprint(steptracker_api)
app.register_blueprint(exercise_api)
#app.register_blueprint(mood_api)
app.register_blueprint(calorie_api)

if __name__ == "__main__":
    app.run()
