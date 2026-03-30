"""
app/routes/main.py - Rotas principais
"""
from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user

main = Blueprint('main', __name__)


@main.route('/')
def index():
    """Página inicial - redireciona conforme autenticação"""
    if current_user.is_authenticated:
        if current_user.is_admin():
            return redirect(url_for('admin.dashboard'))
        return redirect(url_for('user.dashboard'))
    return render_template('main/index.html', title='Bem-vindo')
