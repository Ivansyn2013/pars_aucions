from flask import url_for, Blueprint, request, render_template, current_app, \
    redirect
from werkzeug.exceptions import NotFound
from flask_login import current_user, login_required
from forms.project import CreateProjectForm
from models.init_db import db
from models.users import Project, User, Auction
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import joinedload

project_app = Blueprint('project_app',__name__)

@project_app.route('/create/', methods=['POST','GET'], endpoint='create')
@login_required
def create_project():
    error = None
    form = CreateProjectForm(request.form)
    form.users.choices = [(user.id, user.first_name) for user in
                           User.query.all()]
    form.auctions.choices = [auction.event_description for auction in Auction.query.order_by(
        'created_at')]

    if request.method == ['POST'] and form.validate_on_submit():
        project = Project()
        project.name = form.name.data.strip()
        project.status = form.status.data
        project.auctions = Auction.query.filter(Auction.id ==
            form.auctions.data).all()


        selected_users = User.query.filter(User.id.in_(
            form.users.data)).one_or_none()
        for user in selected_users:
            project.user.append(user)
        db.session.add(project)
        try:
            db.session.commit()
        except IntegrityError:
            current_app.logger.exception("Could not create a new project!")
            error = "Could not create project!"
        else:
            return redirect(
                url_for("project_app.details", project_id=project.id))
    return render_template('project/create.html', form=form,
                           error=error)

@project_app.route('/details/<project_id>')
@login_required
def details(project_id):
    project = Project.query.filert_by(id=project_id).options(
        joinedload(Project.auctions, Project.user)
    ).one_or_none()
    if project is  None:
        return NotFound
    return render_template('project/details.html', project=project)


