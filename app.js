"""
app/routes/errors.py - Handlers de erro HTTP
"""
from flask import Blueprint, render_template

errors = Blueprint('errors', __name__)


@errors.app_errorhandler(403)
def forbidden(e):
    return render_template('errors/403.html', title='Acesso Negado'), 403


@errors.app_errorhandler(404)
def not_found(e):
    return render_template('errors/404.html', title='Página Não Encontrada'), 404


@errors.app_errorhandler(500)
def server_error(e):
    return render_template('errors/500.html', title='Erro Interno'), 500
