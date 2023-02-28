from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

user = User()
user.surname = "Scott"
user.name = 'Ridley'
user.age = 21
user.position = 'captain'
user.speciality = 'research engineer'
user.address = 'module_1'
user.email = 'scott_chief@mars.org'
db_sess = db_session.create_session()
db_sess.add(user)
db_sess.commit()

user1 = User()
user1.surname = "Ababa"
user1.name = 'Oboboh'
user1.age = 21
user1.position = 'supreme_leader'
user1.speciality = 'do nothing and command'
user1.address = 'module_66'
user1.email = 'ababaoboboh@mars.org'
db_sess = db_session.create_session()
db_sess.add(user1)
db_sess.commit()

user2 = User()
user2.surname = "Petrov"
user2.name = 'Yaroslav'
user2.age = 21
user2.position = 'major'
user2.speciality = 'cleanner'
user2.address = 'module_17'
user2.email = 'j_a_r_o_s_l_a_v@mars.org'
db_sess = db_session.create_session()
db_sess.add(user2)
db_sess.commit()

user3 = User()
user3.surname = "Abdula"
user3.name = 'Isbamich'
user3.age = 93
user3.position = 'strong_man'
user3.speciality = 'spotsman'
user3.address = 'module_14'
user3.email = 'abdula@mars.org'
db_sess = db_session.create_session()
db_sess.add(user3)
db_sess.commit()


def main():
    db_session.global_init("db/blogs.db")
    app.run()


if __name__ == '__main__':
    main()
