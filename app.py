#! /usr/bin/env python
from flask import Flask, jsonify, request
import sqlalchemy as sa

from pydantic import ValidationError
import schemas
import models.user as model_user
from core.db import Session

app = Flask(__name__)


@app.route("/users", methods=["POST"])
def create_user():
    try:
        validate_data = schemas.UserCreate.model_validate_json(request.data)
    except ValidationError as e:
        return jsonify({"error": str(e)}), 400
    stmt = (
        sa.insert(model_user.User)
        .values(**validate_data.model_dump())
        .returning(model_user.User)
    )
    with Session() as session:
        user_db = session.scalar(stmt)
        session.commit()
    user = schemas.UserResponse(**user_db.to_dict)

    return jsonify(user.model_dump())


if __name__ == "__main__":
    app.run(debug=True)
