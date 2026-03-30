{% extends "base.html" %}
{% block title %}Editar Perfil{% endblock %}
{% block page_title %}Editar Perfil{% endblock %}

{% block content %}
<div class="row justify-content-center">
  <div class="col-lg-8">
    <div class="card fade-in-up">
      <div class="card-header"><i class="bi bi-pencil-square me-2" style="color:var(--accent)"></i>Editar Informações</div>
      <div class="card-body">
        <form method="POST" enctype="multipart/form-data" novalidate>
          {{ form.hidden_tag() }}

          <div class="row g-3">
            <div class="col-md-6">
              {{ form.full_name.label(class="form-label") }}
              {{ form.full_name(class="form-control" + (" is-invalid" if form.full_name.errors else "")) }}
              {% for e in form.full_name.errors %}<div class="invalid-feedback">{{ e }}</div>{% endfor %}
            </div>
            <div class="col-md-6">
              {{ form.username.label(class="form-label") }}
              {{ form.username(class="form-control" + (" is-invalid" if form.username.errors else "")) }}
              {% for e in form.username.errors %}<div class="invalid-feedback">{{ e }}</div>{% endfor %}
            </div>
            <div class="col-md-6">
              {{ form.email.label(class="form-label") }}
              {{ form.email(class="form-control" + (" is-invalid" if form.email.errors else "")) }}
              {% for e in form.email.errors %}<div class="invalid-feedback">{{ e }}</div>{% endfor %}
            </div>
            <div class="col-md-6">
              {{ form.phone.label(class="form-label") }}
              {{ form.phone(class="form-control" + (" is-invalid" if form.phone.errors else "")) }}
              {% for e in form.phone.errors %}<div class="invalid-feedback">{{ e }}</div>{% endfor %}
            </div>
            <div class="col-12">
              {{ form.bio.label(class="form-label") }}
              {{ form.bio(class="form-control" + (" is-invalid" if form.bio.errors else "")) }}
              {% for e in form.bio.errors %}<div class="invalid-feedback">{{ e }}</div>{% endfor %}
            </div>
            <div class="col-12">
              {{ form.avatar.label(class="form-label") }}
              {{ form.avatar(class="form-control" + (" is-invalid" if form.avatar.errors else "")) }}
              <div style="font-size:11px;color:var(--text-muted);margin-top:4px;">JPG, PNG ou GIF. Máx 2MB.</div>
              {% for e in form.avatar.errors %}<div class="invalid-feedback d-block">{{ e }}</div>{% endfor %}
            </div>
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
