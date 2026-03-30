from flask import jsonify, Blueprint, make_response, request
import flask
from data import db_session
from data.jobs import Jobs

blueprint = flask.Blueprint(
    'jobs_api',
    __name__,
    template_folder='templates'
)


@blueprint.route('/api/jobs', methods=["GET"])
def get_jobs():
    db_ses = db_session.create_session()
    jobs = db_ses.query(Jobs).all()

    return jsonify(
        {
        'jobs':
            [item.to_dict(only=('id', 'team_leader', 'job', 'work_size', 'collaborators',
                                'start_date', 'end_date', 'is_finished')) for item in jobs]
        }
    )

@blueprint.route('/api/jobs/<job_id>', methods=["GET"])
def get_one_job(job_id):
    db_ses = db_session.create_session()
    job = db_ses.query(Jobs).get(job_id)
    if not isinstance(job_id, int) or job_id <= 0:
        return make_response(jsonify({'error': 'Invalid value'}))
    if not job:
        return make_response(jsonify({'error': 'Not found'}), 404)
    return jsonify({'jobs': job.to_dict(only=('id', 'team_leader', 'job', 'work_size', 'collaborators',
                                              'start_date', 'end_date', 'is_finished'))})

@blueprint.route('/api/jobs', methods=["POST"])
def create_job():
    if not request.json:
        return make_response(jsonify({'error': 'Empty request'}), 404)
    elif not all(key in request.json for key in ['job', 'team_leader', 'work_size', 'collaborators']):
        return make_response(jsonify({'error': 'Bad request'}), 404)

    db_ses = db_session.create_session()
    job = Jobs(
        job=request.json['job'],
        team_leader = request.json['team_leader'],
        work_size=request.json['work_size'],
        collaborators=request.json['collaborators'],
        is_finished=request.json['is_finished']
    )
    db_ses.add(job)
    db_ses.commit()
    return jsonify({'id': job.id})