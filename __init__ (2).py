{% extends "base.html" %}
{% block title %}Login{% endblock %}

{% block content %}
<div class="auth-wrapper">
  <!-- Esquerda: visual -->
  <div class="auth-left">
    <div class="auth-brand">
      <div class="auth-brand-icon"><i class="bi bi-shield-lock-fill"></i></div>
      <span class="auth-brand-name">FlaskAuth</span>
    </div>

    <div class="auth-hero">
      <div class="auth-hero-icon">
        <i class="bi bi-box-arrow-in-right"></i>
      </div>
      <h2>Bem-vindo de volta!</h2>
      <p>Acesse sua conta para continuar.<br>Segurança e controle em um só lugar.</p>

      <div class="auth-features">
        <div class="auth-feature">
          <i class="bi bi-shield-check-fill"></i>
          <span>Autenticação segura com criptografia</span>
        </div>
        <div class="auth-feature">
          <i class="bi bi-people-fill"></i>
          <span>Controle de acesso por perfis</span>
        </div>
        <div class="auth-feature">
          <i class="bi bi-journal-code"></i>
          <span>Registro completo de atividades</span>
        </div>
      </div>
    </div>
  </div>

  <!-- Direita: formulário -->
  <div class="auth-right">
    <div class="auth-form-container fade-in-up">
      <div class="auth-form-header">
        <h1 class="auth-form-title">Entrar</h1>
        <p class="auth-form-subtitle">Informe suas credenciais para acessar o sistema</p>
      </div>

      <form method="POST" action="{{ url_for('auth.login') }}" novalidate>
        {{ form.hidden_tag() }}

        <div class="mb-3">
          {{ form.email.label(class="form-label") }}
          <div class="position-relative">
            {{ form.email(class="form-control" + (" is-invalid" if form.email.errors else ""), id="email") }}
            <i class="bi bi-envelope position-absolute" style="right:12px;top:50%;transform:translateY(-50%);color:var(--text-muted);pointer-events:none;"></i>
          </div>
          {% for e in form.email.errors %}
            <div class="invalid-feedback d-block">{{ e }}</div>
          {% endfor %}
        </div>

        <div class="mb-4">
          {{ form.password.label(class="form-label") }}
          <div class="position-relative">
            {{ form.password(class="form-control" + (" is-invalid" if form.password.errors else ""), id="password") }}
            <button type="button" class="btn p-0 border-0 position-absolute"
                    style="right:12px;top:50%;transform:translateY(-50%);color:var(--text-muted);"
                    data-toggle-pw="password">
              <i class="bi bi-eye"></i>
            </button>
          </div>
          {% for e in form.password.errors %}
            <div class="invalid-feedback d-block">{{ e }}</div>
          {% endfor %}
        </div>

        <div class="d-flex align-items-center justify-content-between mb-4">
          <div class="form-check">
            {{ form.remember_me(class="form-check-input") }}
            <label class="form-check-label" for="remember_me" style="font-size:13px;color:var(--text-secondary);">
              Lembrar de mim
            </label>
          </div>
          <a href="{{ url_for('auth.request_password_reset') }}" style="font-size:13px;">
            Esqueci a senha
          </a>
        </div>

        {{ form.submit(class="btn btn-primary w-100 btn-lg") }}
      </form>

      <div class="auth-divider">ou</div>

      <div class="auth-footer-link">
        Não tem uma conta?
        <a href="{{ url_for('auth.register') }}" class="fw-semibold">Criar conta gratuita</a>
      </div>
    </div>
  </div>
</div>
{% endblock %}
