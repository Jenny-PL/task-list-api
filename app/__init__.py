from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from dotenv import load_dotenv


db = SQLAlchemy()
migrate = Migrate()
load_dotenv()


def create_app(test_config=None):
    app=Flask(__name__,template_folder='templates')
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    if test_config is None:
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
            "SQLALCHEMY_DATABASE_URI")
    else:
        app.config["TESTING"] = True
        app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get(
            "SQLALCHEMY_TEST_DATABASE_URI")

    # Import models here for Alembic setup
    from app.models.task import Task
    from app.models.goal import Goal

    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints here
    from app.routes.routes_tasks import task_bp
    app.register_blueprint(task_bp)

    from app.routes.routes_goals import goal_bp
    app.register_blueprint(goal_bp)

    from app.routes.routes_tasks import task_home_bp
    app.register_blueprint(task_home_bp)

    # follows nina's structure... not sure what these are doing
    @app.route("/")
    @app.route("/main")
    @app.route("/index")
    @app.route("/about")
    def about():
        return "<h1> The Task List Project</h1>"    

    return app
