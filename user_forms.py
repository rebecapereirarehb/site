{% extends "base.html" %}
{% block title %}Criar Conta{% endblock %}

{% block content %}
<div class="auth-wrapper">
  <div class="auth-left">
    <div class="auth-brand">
      <div class="auth-brand-icon"><i class="bi bi-shield-lock-fill"></i></div>
      <span class="auth-brand-name">FlaskAuth</span>
    </div>
    <div class="auth-hero">
      <div class="auth-hero-icon"><i class="bi bi-person-plus-fill"></i></div>
      <h2>Crie sua conta agora</h2>
      <p>Rápido, seguro e gratuito.<br>Comece a usar o sistema em segundos.</p>
      <div class="auth-features">
        <div class="auth-feature"><i class="bi bi-lock-fill"></i><span>Dados protegidos com hash bcrypt</span></div>
        <div class="auth-feature"><i class="bi bi-grid-fill"></i><span>Painel personalizado por perfil</span></div>
        <div class="auth-feature"><i class="bi bi-check-circle-fill"></i><span>Validação completa de formulário</span></div>
      </div>
    </div>
  </div>

  <div class="auth-right">
    <div class="auth-form-container fade-in-up">
      <div class="auth-form-header">
        <h1 class="auth-form-title">Criar Conta</h1>
        <p class="auth-form-subtitle">Preencha os dados abaixo para se cadastrar</p>
      </div>

      <form method="POST" novalidate>
        {{ form.hidden_tag() }}

        <div class="mb-3">
          {{ form.full_name.label(class="form-label") }}
          {{ form.full_name(class="form-control" + (" is-invalid" if form.full_name.errors else "")) }}
          {% for e in form.full_name.errors %}<div class="invalid-feedback d-block">{{ e }}</div>{% endfor %}
        </div>

        <div class="mb-3">
          {{ form.username.label(class="form-label") }}
          {{ form.username(class="form-control" + (" is-invalid" if form.username.errors else "")) }}
          {% for e in form.username.errors %}<div class="invalid-feedback d-block">{{ e }}</div>{% endfor %}
        </div>

        <div class="mb-3">
          {{ form.email.label(class="form-label") }}
          {{ form.email(class="form-control" + (" is-invalid" if form.email.errors else "")) }}
          {% for e in form.email.errors %}<div class="invalid-feedback d-block">{{ e }}</div>{% endfor %}
        </div>

        <div class="mb-3">
          {{ form.password.label(class="form-label") }}
          <div class="position-relative">
            {{ form.password(class="form-control" + (" is-invalid" if form.password.errors else ""), id="password") }}
            <button type="button" class="btn p-0 border-0 position-absolute"
                    style="right:12px;top:50%;transform:translateY(-50%);color:var(--text-muted);"
                    data-toggle-pw="password"><i class="bi bi-eye"></i></button>
          </div>
          <div class="mt-2">
            <div style="height:4px;background:var(--border);border-radius:2px;overflow:hidden;">
              <div id="strengthBar" style="height:100%;width:0;transition:all .3s;border-radius:2px;"></div>
            </div>
            <span id="strengthText" style="font-size:11px;color:var(--text-muted);"></span>
          </div>
          {% for e in form.password.errors %}<div class="invalid-feedback d-block">{{ e }}</div>{% endfor %}
        </div>

        <div class="mb-4">
          {{ form.password2.label(class="form-label") }}
          {{ form.password2(class="form-control" + (" is-invalid" if form.password2.errors else "")) }}
          {% for e in form.password2.errors %}<div class="invalid-feedback d-block">{{ e }}</div>{% endfor %}
        </div>

        {{ form.submit(class="btn btn-primary w-100 btn-lg") }}
      </form>

      <div class="auth-divider">ou</div>
      <div class="auth-footer-link">
        Já tem conta? <a href="{{ url_for('auth.login') }}" class="fw-semibold">Entrar agora</a>
      </div>
    </div>
  </div>
</div>
{% endblock %}
