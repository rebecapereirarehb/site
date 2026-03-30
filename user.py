{% extends "base.html" %}
{% block title %}Dashboard{% endblock %}
{% block page_title %}Dashboard{% endblock %}

{% block content %}
<!-- Welcome -->
<div class="welcome-card fade-in-up">
  <h2>Olá, {{ current_user.full_name.split()[0] if current_user.full_name else current_user.username }}! 👋</h2>
  <p>Bem-vindo ao seu painel. Aqui você pode gerenciar sua conta e acompanhar suas atividades.</p>
</div>

<!-- Stats -->
<div class="row g-3 mb-4">
  <div class="col-sm-6 col-lg-3 fade-in-up delay-1">
    <div class="stat-card">
      <div class="stat-icon purple"><i class="bi bi-person-circle"></i></div>
      <div class="stat-info">
        <div class="stat-value">{{ current_user.role.name|title if current_user.role else '—' }}</div>
        <div class="stat-label">Perfil</div>
      </div>
    </div>
  </div>
  <div class="col-sm-6 col-lg-3 fade-in-up delay-2">
    <div class="stat-card">
      <div class="stat-icon green"><i class="bi bi-check-circle-fill"></i></div>
      <div class="stat-info">
        <div class="stat-value">{{ 'Ativa' if current_user.is_active else 'Inativa' }}</div>
        <div class="stat-label">Status da Conta</div>
      </div>
    </div>
  </div>
  <div class="col-sm-6 col-lg-3 fade-in-up delay-3">
    <div class="stat-card">
      <div class="stat-icon blue"><i class="bi bi-journal-text"></i></div>
      <div class="stat-info">
        <div class="stat-value">{{ recent_logs|length }}</div>
        <div class="stat-label">Atividades Recentes</div>
      </div>
    </div>
  </div>
  <div class="col-sm-6 col-lg-3 fade-in-up delay-4">
    <div class="stat-card">
      <div class="stat-icon yellow"><i class="bi bi-clock-fill"></i></div>
      <div class="stat-info">
        <div class="stat-value" style="font-size:16px;">
          {{ current_user.last_login.strftime('%d/%m') if current_user.last_login else '—' }}
        </div>
        <div class="stat-label">Último Acesso</div>
      </div>
    </div>
  </div>
</div>

<div class="row g-3">
  <!-- Ações rápidas -->
  <div class="col-lg-4 fade-in-up delay-1">
    <div class="card h-100">
      <div class="card-header"><i class="bi bi-lightning-fill me-2" style="color:var(--accent)"></i>Ações Rápidas</div>
      <div class="card-body d-flex flex-column gap-2">
        <a href="{{ url_for('user.edit_profile') }}" class="btn btn-outline-secondary w-100 text-start">
          <i class="bi bi-pencil-square me-2"></i>Editar Perfil
        </a>
        <a href="{{ url_for('user.change_password') }}" class="btn btn-outline-secondary w-100 text-start">
          <i class="bi bi-key me-2"></i>Alterar Senha
        </a>
        <a href="{{ url_for('user.profile') }}" class="btn btn-outline-secondary w-100 text-start">
          <i class="bi bi-person-circle me-2"></i>Ver Perfil Completo
        </a>
      </div>
    </div>
  </div>

  <!-- Atividades recentes -->
  <div class="col-lg-8 fade-in-up delay-2">
    <div class="card h-100">
      <div class="card-header d-flex align-items-center justify-content-between">
        <span><i class="bi bi-activity me-2" style="color:var(--accent)"></i>Atividades Recentes</span>
      </div>
      <div class="card-body p-0">
        {% if recent_logs %}
          <div class="table-responsive">
            <table class="table mb-0">
              <tbody>
                {% for log in recent_logs %}
                <tr>
                  <td>
                    <span class="log-badge log-{{ log.status }}">
                      <i class="bi bi-circle-fill" style="font-size:7px;"></i>
                      {{ log.status }}
                    </span>
                  </td>
                  <td style="color:var(--text-primary);font-size:13px;">{{ log.action|replace('_',' ')|title }}</td>
                  <td style="color:var(--text-muted);font-size:12px;">
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
            Nenhuma atividade ainda.
          </div>
        {% endif %}
      </div>
    </div>
  </div>
</div>
{% endblock %}
