{% extends 'tracker/base.html' %}
{% block title %}Setup Profile – FitTrack{% endblock %}
{% block content %}
<div class="d-flex justify-content-center" style="padding-top: 24px;">
    <div style="width: 100%; max-width: 500px;">
        <div class="page-header text-center">
            <h2>⚙️ Setup Your Profile</h2>
            <p style="color:var(--text-muted);">Tell us about yourself for accurate BMI & health calculations</p>
        </div>
        <div class="card p-4">
            <form method="post">
                {% csrf_token %}
                <div class="row g-3">
                    <div class="col-6">
                        <label class="form-label">Date of Birth</label>
                        <input type="date" name="date_of_birth" class="form-control" value="{{ form.date_of_birth.value|default:'' }}">
                    </div>
                    <div class="col-6">
                        <label class="form-label">Gender</label>
                        <select name="gender" class="form-select">
                            <option value="">-- Select --</option>
                            <option value="M" {% if form.gender.value == 'M' %}selected{% endif %}>Male</option>
                            <option value="F" {% if form.gender.value == 'F' %}selected{% endif %}>Female</option>
                            <option value="O" {% if form.gender.value == 'O' %}selected{% endif %}>Other</option>
                        </select>
                    </div>
                    <div class="col-6">
                        <label class="form-label">Height (cm)</label>
                        <input type="number" step="0.1" name="height_cm" class="form-control" placeholder="e.g. 175" value="{{ form.height_cm.value|default:'' }}">
                    </div>
                    <div class="col-6">
                        <label class="form-label">Goal Weight (kg)</label>
                        <input type="number" step="0.1" name="goal_weight_kg" class="form-control" placeholder="e.g. 70" value="{{ form.goal_weight_kg.value|default:'' }}">
                    </div>
                    <div class="col-12 mt-2">
                        <button type="submit" class="btn btn-primary w-100" style="padding:12px;">Save Profile</button>
                    </div>
                </div>
            </form>
        </div>
    </div>
</div>
{% endblock %}
