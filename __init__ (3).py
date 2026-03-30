{% extends "base.html" %}
{% block title %}Recuperar Senha{% endblock %}
{% block content %}
<div class="auth-wrapper">
  <div class="auth-left">
    <div class="auth-brand">
      <div class="auth-brand-icon"><i class="bi bi-shield-lock-fill"></i></div>
      <span class="auth-brand-name">FlaskAuth</span>
    </div>
    <div class="auth-hero">
      <div class="auth-hero-icon"><i class="bi bi-key-fill"></i></div>
      <h2>Recupere seu acesso</h2>
      <p>Informe seu e-mail cadastrado e enviaremos um link seguro para redefinir sua senha.</p>
    </div>
  </div>
  <div class="auth-right">
    <div class="auth-form-container fade-in-up">
      <div class="auth-form-header">
        <h1 class="auth-form-title">Esqueceu a senha?</h1>
        <p class="auth-form-subtitle">Digite seu e-mail para receber o link de recuperação</p>
      </div>
      <form method="POST" novalidate>
        {{ form.hidden_tag() }}
        <div class="mb-4">
          {{ form.email.label(class="form-label") }}
          {{ form.email(class="form-control" + (" is-invalid" if form.email.errors else "")) }}
          {% for e in form.email.errors %}<div class="invalid-feedback d-block">{{ e }}</div>{% endfor %}
        </div>
        {{ form.submit(class="btn btn-primary w-100 btn-lg") }}
      </form>
      <div class="auth-footer-link mt-3">
        <a href="{{ url_for('auth.login') }}"><i class="bi bi-arrow-left me-1"></i>Voltar ao login</a>
      </div>
    </div>
  </div>
</div>
{% endblock %}
