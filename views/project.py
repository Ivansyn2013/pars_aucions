from flask import url_for, Blueprint, request, render_template, current_app, \
    redirect
from werkzeug.exceptions import NotFound
from flask_login import current_user, login_required
from forms.project import CreateProjectForm
from models.init_db import db
from models.users import Project, User, Auction
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import joinedload
from logic.common_main import save_get_data_indb

project_app = Blueprint('project_app', __name__)


@project_app.route('/create/', methods=['POST', 'GET'], endpoint='create')
@login_required
def create_project():
    error = None
    form = CreateProjectForm(request.form)
    form.users.choices = [(user.id, user.first_name) for user in
                          User.query.all()]
    form.auctions.choices = [(auction.id, auction.event_description) for auction in Auction.query.order_by(
        'created_at')]

    if request.method == 'POST' and form.validate_on_submit():
        project = Project()
        project.name = form.name.data.strip()
        project.status = form.status.data
        project.author_id = current_user.id
        auctions = Auction.query.filter(Auction.id.in_(form.auctions.data))
        for auction in auctions:
            project.auctions.append(auction)

        selected_users = User.query.filter(User.id.in_(
            form.users.data))
        for user in selected_users:
            project.user.append(user)
        db.session.add(project)
        try:
            db.session.commit()
        except IntegrityError:
            current_app.logger.exception("Could not create a new project!")
            error = "Не получилось создать проект"
        else:
            db.session.flush()
            current_app.logger.info(f"Созан новый проект {project.name} пользователем {current_user.username}")
            message = f"Созан новый проект {project.name} пользователем {current_user.username}"
            return redirect(
                url_for("project_app.details", project_id=project.id, message=message))
    return render_template('project/create.html', form=form,
                           error=error)


@project_app.route('/details/<project_id>')
@login_required
def details(project_id):
    project = Project.query.filter_by(id=project_id).options(
        joinedload(Project.auctions)
    ).one_or_none()
    if project is None:
        return NotFound
    return render_template('project/details.html', project=project)


@project_app.route('/save_auction', methods=['POST'], endpoint='save_auction')
@login_required
def save_auction(claim_number):
    '''get tada from front and save auction in db'''
    if save_get_data_indb(claim_number):
        return True
    else:
        return False


@project_app.route('/list', methods=['GET'], endpoint='list')
@login_required
def projects_list():
    projects = Project.query.all()
    return render_template('project/list.html', projects=projects)
