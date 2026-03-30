"""
app/routes/admin.py - Rotas do painel administrativo
"""
from functools import wraps
from flask import (Blueprint, render_template, redirect, url_for,
                   flash, request, abort)
from flask_login import login_required, current_user
from app import db
from app.models.user import User, Role
from app.models.activity import ActivityLog
from app.forms.admin_forms import AdminEditUserForm, AdminCreateUserForm

admin = Blueprint('admin', __name__)


def admin_required(f):
    """Decorator que exige que o usuário seja administrador"""
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or not current_user.is_admin():
            flash('Acesso negado. Você precisa ser administrador.', 'danger')
            abort(403)
        return f(*args, **kwargs)
    return decorated_function


@admin.route('/dashboard')
@login_required
@admin_required
def dashboard():
    """Dashboard administrativo com métricas"""
    total_users = User.query.count()
    active_users = User.query.filter_by(is_active=True).count()
    admin_count = User.query.join(Role).filter(Role.name == 'admin').count()
    recent_logs = ActivityLog.query.order_by(
        ActivityLog.created_at.desc()
    ).limit(10).all()
    new_users = User.query.order_by(User.created_at.desc()).limit(5).all()

    return render_template('admin/dashboard.html',
                           title='Painel Admin',
                           total_users=total_users,
                           active_users=active_users,
                           admin_count=admin_count,
                           recent_logs=recent_logs,
                           new_users=new_users)


@admin.route('/users')
@login_required
@admin_required
def users_list():
    """Lista todos os usuários com paginação"""
    page = request.args.get('page', 1, type=int)
    search = request.args.get('search', '', type=str)

    query = User.query
    if search:
        query = query.filter(
            (User.username.ilike(f'%{search}%')) |
            (User.email.ilike(f'%{search}%')) |
            (User.full_name.ilike(f'%{search}%'))
        )

    pagination = query.order_by(User.created_at.desc()).paginate(
        page=page, per_page=10, error_out=False
    )

    return render_template('admin/users_list.html',
                           title='Gerenciar Usuários',
                           pagination=pagination,
                           users=pagination.items,
                           search=search)


@admin.route('/users/create', methods=['GET', 'POST'])
@login_required
@admin_required
def create_user():
    """Cria novo usuário pelo admin"""
    form = AdminCreateUserForm()
    if form.validate_on_submit():
        role = Role.query.filter_by(name=form.role.data).first()
        user = User(
            username=form.username.data.lower().strip(),
            full_name=form.full_name.data.strip(),
            email=form.email.data.lower().strip(),
            role=role
        )
        user.password = form.password.data
        db.session.add(user)
        db.session.commit()

        ActivityLog.log('admin_create_user', f'Admin criou usuário: {user.email}',
                        user_id=current_user.id)
        flash(f'Usuário {user.username} criado com sucesso!', 'success')
        return redirect(url_for('admin.users_list'))

    return render_template('admin/create_user.html', form=form, title='Criar Usuário')


@admin.route('/users/<int:user_id>/edit', methods=['GET', 'POST'])
@login_required
@admin_required
def edit_user(user_id):
    """Edita usuário pelo admin"""
    target_user = User.query.get_or_404(user_id)
    form = AdminEditUserForm()

    if form.validate_on_submit():
        target_user.full_name = form.full_name.data.strip()
        target_user.username = form.username.data.lower().strip()
        target_user.email = form.email.data.lower().strip()
        target_user.is_active = form.is_active.data

        role = Role.query.filter_by(name=form.role.data).first()
        target_user.role = role
        db.session.commit()

        ActivityLog.log('admin_edit_user', f'Admin editou usuário: {target_user.email}',
                        user_id=current_user.id)
        flash(f'Usuário {target_user.username} atualizado!', 'success')
        return redirect(url_for('admin.users_list'))

    elif request.method == 'GET':
        form.full_name.data = target_user.full_name
        form.username.data = target_user.username
        form.email.data = target_user.email
        form.is_active.data = target_user.is_active
        form.role.data = target_user.role.name if target_user.role else 'user'

    return render_template('admin/edit_user.html',
                           form=form, target_user=target_user, title='Editar Usuário')


@admin.route('/users/<int:user_id>/toggle', methods=['POST'])
@login_required
@admin_required
def toggle_user(user_id):
    """Ativa ou desativa um usuário"""
    target_user = User.query.get_or_404(user_id)

    if target_user.id == current_user.id:
        flash('Você não pode desativar sua própria conta.', 'warning')
        return redirect(url_for('admin.users_list'))

    target_user.is_active = not target_user.is_active
    db.session.commit()

    status = 'ativado' if target_user.is_active else 'desativado'
    action = 'admin_activate_user' if target_user.is_active else 'admin_deactivate_user'
    ActivityLog.log(action, f'Admin {status} usuário: {target_user.email}',
                    user_id=current_user.id, status='warning')
    flash(f'Usuário {target_user.username} foi {status}.', 'success')
    return redirect(url_for('admin.users_list'))


@admin.route('/users/<int:user_id>/delete', methods=['POST'])
@login_required
@admin_required
def delete_user(user_id):
    """Exclui um usuário (apenas admin)"""
    target_user = User.query.get_or_404(user_id)

    if target_user.id == current_user.id:
        flash('Você não pode excluir sua própria conta.', 'danger')
        return redirect(url_for('admin.users_list'))

    username = target_user.username
    db.session.delete(target_user)
    db.session.commit()

    ActivityLog.log('admin_delete_user', f'Admin excluiu usuário: {username}',
                    user_id=current_user.id, status='warning')
    flash(f'Usuário {username} excluído com sucesso.', 'success')
    return redirect(url_for('admin.users_list'))


@admin.route('/logs')
@login_required
@admin_required
def activity_logs():
    """Exibe logs de atividade do sistema"""
    page = request.args.get('page', 1, type=int)
    filter_status = request.args.get('status', '', type=str)

    query = ActivityLog.query
    if filter_status:
        query = query.filter_by(status=filter_status)

    pagination = query.order_by(ActivityLog.created_at.desc()).paginate(
        page=page, per_page=20, error_out=False
    )

    return render_template('admin/logs.html',
                           title='Logs do Sistema',
                           pagination=pagination,
                           logs=pagination.items,
                           filter_status=filter_status)
