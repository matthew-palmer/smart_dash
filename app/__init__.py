from flask import Flask, render_template
import logging
import logging.handlers

from .resource.cache import cache

from .modules.weather.routes import weather_blueprint


def create_app():
    app = Flask(__name__,
                instance_relative_config=True,
                template_folder="ui/templates",
                static_folder="ui/static")
    app.config.from_pyfile("config.py")

    # logging
    handler = logging.handlers.RotatingFileHandler(app.config["LOG_FILE"],
                                                   maxBytes=app.config["LOG_SIZE"],
                                                   backupCount=app.config["LOG_FILE_COUNT"])
    handler.setLevel(app.config["LOG_LEVEL"])
    handler.setFormatter(logging.Formatter("[%(asctime)s] %(levelname)s [%(pathname)s at %(lineno)s]: %(message)s",
                                           "%Y-%m-%d %H:%M:%S"))
    app.logger.addHandler(handler)

    # Cache init
    app_config = {
        "DEBUG": True,
        "CACHE_TYPE": "filesystem",
        "CACHE_DEFAULT_TIMEOUT": 300,
        "CACHE_DIR": ".dashboard_cache"
    }
    cache.init_app(app, config=app_config)

    with app.app_context():
        app.register_blueprint(weather_blueprint)

        @app.route("/")
        def index():
            return render_template("index.html")

        @app.errorhandler(404)
        def page_not_found(e):
            print(e)
            return render_template("404.html"), 404

        @app.errorhandler(500)
        def internal_server_error(e):
            print(e)
            return render_template("500.html"), 500

    return app
