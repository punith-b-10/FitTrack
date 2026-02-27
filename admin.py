{% extends 'tracker/base.html' %}
{% block title %}Login – FitTrack{% endblock %}
{% block content %}
<div class="d-flex justify-content-center align-items-center" style="min-height: 85vh;">
    <div style="width: 100%; max-width: 420px;">
        <div class="text-center mb-4">
            <h1 style="font-size:3rem; color:var(--primary);">FITTRACK</h1>
            <p style="color:var(--text-muted);">Your Smart Fitness Companion</p>
        </div>
        <div class="card p-4">
            <h3 class="mb-4 text-center">Welcome Back</h3>
            <form method="post">
                {% csrf_token %}
                <div class="mb-3">
                    <label class="form-label">Username</label>
                    <input type="text" name="username" class="form-control" placeholder="Enter username" required>
                </div>
                <div class="mb-3">
                    <label class="form-label">Password</label>
                    <input type="password" name="password" class="form-control" placeholder="Enter password" required>
                </div>
                {% if form.errors %}
                <div class="alert alert-danger">Invalid credentials. Please try again.</div>
                {% endif %}
                <button type="submit" class="btn btn-primary w-100 mt-2" style="padding:12px;">Sign In</button>
            </form>
            <hr style="border-color:var(--border);">
            <p class="text-center mb-0" style="color:var(--text-muted);">
                Don't have an account? <a href="{% url 'register' %}" style="color:var(--primary);">Register</a>
            </p>
        </div>
    </div>
</div>
{% endblock %}
