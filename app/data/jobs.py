import datetime
import sqlalchemy
from sqlalchemy import orm
import db_session
from .db_session import SqlAlchemyBase
from users import User

user = User()
user.surname = "Scott"
user.name = "Ridley"
user.age = 21
user.position = "captain"
user.speciality = "research engineer"
user.address = "module_1"
user.email = "scott_chief@mars.org"
db_sess = db_session.create_session()
db_sess.add(user)
db_sess.commit()

user1 = User()
user1.surname = "Scotty"
user1.name = "Ridleyy"
user1.age = 21
user1.position = "not a captain"
user1.speciality = "not a research engineer"
user1.address = "module_4"
user1.email = "not_scott_chief@mars.org"
db_sess = db_session.create_session()
db_sess.add(user1)
db_sess.commit()

user2 = User()
user2.surname = "Hlaebaster"
user2.name = "Rid_of"
user2.age = 21
user2.position = "Doctor"
user2.speciality = "nurse"
user2.address = "module_0"
user2.email = "nurse@mars.org"
db_sess = db_session.create_session()
db_sess.add(user2)
db_sess.commit()

user3 = User()
user3.surname = "John"
user3.name = "Ridlei"
user3.age = 21
user3.position = 'bandit'
user3.speciality = "engineer"
user3.address = "module_123"
user3.email = "foreign@mars.org"
db_sess = db_session.create_session()
db_sess.add(user3)
db_sess.commit()


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

# id
# team_leader (id) (id руководителя, целое число)
# job (description) (описание работы)
# work_size (hours) (объем работы в часах)
# collaborators (list of id of participants) (список id участников)
# start_date (дата начала)
# end_date (дата окончания)
# is_finished (bool) (признак завершения)
