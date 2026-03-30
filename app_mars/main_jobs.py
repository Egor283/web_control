from flask import Flask
from data import db_session
from data.jobs import Jobs

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key'


def main():
    db_session.global_init("db/mars.db")
    session = db_session.create_session()

    job = Jobs()
    job.team_leader = 1
    job.job = 'deployment of residential modules 1 and 2'
    job.work_size = 15
    job.collaborators = '2, 4'
    job.is_finished = False
    session.add(job)

    job = Jobs()
    job.team_leader = 3
    job.job = 'clean'
    job.work_size = 9
    job.collaborators = '3'
    job.is_finished = False
    session.add(job)

    job = Jobs()
    job.team_leader = 4
    job.job = 'advance'
    job.work_size = 15
    job.collaborators = '2'
    job.is_finished = False
    session.add(job)

    session.commit()
    app.run()


if __name__ == '__main__':
    main()