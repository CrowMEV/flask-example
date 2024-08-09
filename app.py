#! /usr/bin/env python
from flask import Flask

import users_api
from core.db import db
from core.settings import config


def create_app(db_url: str):
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = db_url
    db.init_app(app)

    app.add_url_rule(
        "/users", view_func=users_api.create_user, methods=["POST"]
    )
    return app


if __name__ == "__main__":
    app = create_app(config.dsn)
    app.run(debug=True)
