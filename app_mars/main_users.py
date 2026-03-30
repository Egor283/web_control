from flask import Flask
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key'


def main():
    db_session.global_init("db/mars.db")
    session = db_session.create_session()

    user = User()
    user.surname = "Ivan"
    user.name = "Ivanov"
    user.age = 25
    user.position = "captain"
    user.speciality = "research engineer"
    user.address = "module_1"
    user.email = "ivan@mars.org"
    user.set_password("cap")
    session.add(user)

    user = User()
    user.surname = "Rusik"
    user.name = "Ruseev"
    user.age = 20
    user.position = "medik"
    user.speciality = "vrach"
    user.address = "module_2"
    user.email = "rusik@mars.org"
    user.set_password("med")
    session.add(user)

    user = User()
    user.surname = "Casha"
    user.name = "Aleksandrov"
    user.age = 22
    user.position = "yborshik"
    user.speciality = "not"
    user.address = "module_3"
    user.email = "casha@mars.org"
    user.set_password("cl")
    session.add(user)

    user = User()
    user.surname = "Kosty"
    user.name = "Kostynov"
    user.age = 33
    user.position = "exploer"
    user.speciality = "scientist"
    user.address = "module_4"
    user.email = "kosty@mars.org"
    user.set_password("ex")
    session.add(user)
    session.commit()
    app.run()

if __name__ == '__main__':
    main()