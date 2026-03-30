{% extends "base.html" %}
{% block title %}Alterar Senha{% endblock %}
{% block page_title %}Alterar Senha{% endblock %}

{% block content %}
<div class="row justify-content-center">
  <div class="col-lg-5">
    <div class="card fade-in-up">
      <div class="card-header"><i class="bi bi-key-fill me-2" style="color:var(--accent)"></i>Alterar Senha</div>
      <div class="card-body">
        <form method="POST" novalidate>
          {{ form.hidden_tag() }}

          <div class="mb-3">
            {{ form.current_password.label(class="form-label") }}
            <div class="position-relative">
              {{ form.current_password(class="form-control" + (" is-invalid" if form.current_password.errors else ""), id="current_password") }}
              <button type="button" class="btn p-0 border-0 position-absolute"
                      style="right:12px;top:50%;transform:translateY(-50%);color:var(--text-muted);"
                      data-toggle-pw="current_password"><i class="bi bi-eye"></i></button>
            </div>
            {% for e in form.current_password.errors %}<div class="invalid-feedback d-block">{{ e }}</div>{% endfor %}
          </div>

          <div class="mb-3">
            {{ form.new_password.label(class="form-label") }}
            <div class="position-relative">
              {{ form.new_password(class="form-control" + (" is-invalid" if form.new_password.errors else ""), id="password") }}
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
            {% for e in form.new_password.errors %}<div class="invalid-feedback d-block">{{ e }}</div>{% endfor %}
          </div>

          <div class="mb-4">
            {{ form.new_password2.label(class="form-label") }}
            {{ form.new_password2(class="form-control" + (" is-invalid" if form.new_password2.errors else "")) }}
            {% for e in form.new_password2.errors %}<div class="invalid-feedback d-block">{{ e }}</div>{% endfor %}
          </div>

          <div class="divider-h"></div>
          <div class="d-flex gap-2">
            {{ form.submit(class="btn btn-primary") }}
            <a href="{{ url_for('user.profile') }}" class="btn btn-outline-secondary">Cancelar</a>
          </div>
        </form>
      </div>
    </div>
  </div>
</div>
{% endblock %}
