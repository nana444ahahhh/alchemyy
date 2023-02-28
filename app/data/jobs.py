import datetime
import sqlalchemy
from sqlalchemy import orm
import db_session
from .db_session import SqlAlchemyBase
from users import User


class Jobs(SqlAlchemyBase):
    __tablename__ = 'news'

    job = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    work_size = sqlalchemy.Column(sqlalchemy.DateTime,
                                  default=datetime.datetime.now().hour)
    collaborators = sqlalchemy.Column(sqlalchemy.PickleType, default=True)

    team_leader = sqlalchemy.Column(sqlalchemy.Integer,
                                    sqlalchemy.ForeignKey("users.id"))
    start_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                   default=datetime.datetime.now)
    end_date = sqlalchemy.Column(sqlalchemy.DateTime,
                                 default=datetime.datetime.now)
    is_finished = sqlalchemy.Column(sqlalchemy.Boolean, default=False)



