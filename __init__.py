{% extends "base.html" %}
{% block title %}Meu Perfil{% endblock %}
{% block page_title %}Meu Perfil{% endblock %}

{% block content %}
<div class="profile-hero fade-in-up">
  <div class="profile-avatar-lg">
    {{ current_user.full_name[0].upper() if current_user.full_name else 'U' }}
  </div>
  <div class="profile-info flex-grow-1">
    <h3>{{ current_user.full_name or current_user.username }}</h3>
    <p><i class="bi bi-envelope me-1"></i>{{ current_user.email }}</p>
    {% if current_user.bio %}
      <p class="mt-1" style="font-size:14px;color:var(--text-secondary);">{{ current_user.bio }}</p>
    {% endif %}
  </div>
  <div class="d-flex flex-column gap-2">
    <a href="{{ url_for('user.edit_profile') }}" class="btn btn-primary btn-sm">
      <i class="bi bi-pencil-square"></i> Editar
    </a>
    <a href="{{ url_for('user.change_password') }}" class="btn btn-outline-secondary btn-sm">
      <i class="bi bi-key"></i> Senha
    </a>
  </div>
</div>

<div class="row g-3">
  <!-- Informações -->
  <div class="col-lg-5 fade-in-up delay-1">
    <div class="card h-100">
      <div class="card-header"><i class="bi bi-person me-2" style="color:var(--accent)"></i>Informações</div>
      <div class="card-body">
        <div class="row g-3">
          {% set fields = [
            ('bi-person', 'Nome de usuário', current_user.username),
            ('bi-envelope', 'E-mail', current_user.email),
            ('bi-telephone', 'Telefone', current_user.phone or '—'),
            ('bi-shield', 'Perfil', current_user.role.name|title if current_user.role else '—'),
            ('bi-check-circle', 'Status', 'Ativo' if current_user.is_active else 'Inativo'),
            ('bi-calendar', 'Cadastro', current_user.created_at.strftime('%d/%m/%Y') if current_user.created_at else '—'),
            ('bi-clock', 'Último login', current_user.last_login.strftime('%d/%m/%Y %H:%M') if current_user.last_login else '—'),
          ] %}
          {% for icon, label, value in fields %}
          <div class="col-12">
            <div style="font-size:11px;text-transform:uppercase;letter-spacing:.5px;color:var(--text-muted);margin-bottom:3px;">
              <i class="bi {{ icon }} me-1"></i>{{ label }}
            </div>
            <div style="font-size:14px;color:var(--text-primary);">{{ value }}</div>
          </div>
          {% endfor %}
        </div>
      </div>
    </div>
  </div>

  <!-- Atividades -->
  <div class="col-lg-7 fade-in-up delay-2">
    <div class="card h-100">
      <div class="card-header"><i class="bi bi-journal-text me-2" style="color:var(--accent)"></i>Histórico de Atividades</div>
      <div class="card-body p-0">
        {% if logs %}
          <div class="table-responsive">
            <table class="table mb-0">
              <thead>
                <tr>
                  <th>Ação</th>
                  <th>Status</th>
                  <th>Data</th>
                </tr>
              </thead>
              <tbody>
                {% for log in logs %}
                <tr>
                  <td style="font-size:13px;">{{ log.action|replace('_',' ')|title }}</td>
                  <td>
                    <span class="log-badge log-{{ log.status }}">{{ log.status }}</span>
                  </td>
                  <td style="font-size:12px;color:var(--text-muted);">
                    {{ log.created_at.strftime('%d/%m/%Y %H:%M') }}
                  </td>
                </tr>
                {% endfor %}
              </tbody>
            </table>
          </div>
        {% else %}
          <div class="text-center py-4" style="color:var(--text-muted);">
            <i class="bi bi-inbox fs-3 d-block mb-2"></i>
            Nenhum registro encontrado.
          </div>
        {% endif %}
      </div>
    </div>
  </div>
</div>
{% endblock %}
