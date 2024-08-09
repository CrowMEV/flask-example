import sqlalchemy as sa
from flask import abort, jsonify, request
from pydantic import ValidationError
from sqlalchemy.exc import IntegrityError

import models.user as model_user
import schemas
from core.db import db


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
    try:
        user_db = db.session.scalar(stmt)
        db.session.commit()
    except IntegrityError as err:
        if "ix_users_email" in err.orig.pgerror:
            abort(400, description="Hello!!!")
        else:
            raise err

    user = schemas.UserResponse(**user_db.to_dict)

    return jsonify(user.model_dump())
