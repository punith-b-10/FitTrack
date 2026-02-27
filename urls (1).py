{% extends 'tracker/base.html' %}
{% block title %}Log Workout – FitTrack{% endblock %}
{% block content %}
<div class="d-flex justify-content-center" style="padding-top: 24px;">
    <div style="width: 100%; max-width: 560px;">
        <div class="page-header">
            <h2>⚡ Log Workout</h2>
            <p style="color:var(--text-muted);">Record your exercise session</p>
        </div>
        <div class="card p-4">
            <form method="post">
                {% csrf_token %}
                <div class="row g-3">
                    <div class="col-md-6">
                        <label class="form-label">Date</label>
                        <input type="date" name="date" class="form-control" value="{{ form.date.value }}" required>
                    </div>
                    <div class="col-md-6">
                        <label class="form-label">Workout Type</label>
                        <select name="workout_type" class="form-select" required>
                            <option value="">-- Select --</option>
                            <option value="cardio">Cardio</option>
                            <option value="strength">Strength Training</option>
                            <option value="yoga">Yoga / Flexibility</option>
                            <option value="sports">Sports</option>
                            <option value="hiit">HIIT</option>
                            <option value="other">Other</option>
                        </select>
                    </div>
                    <div class="col-12">
                        <label class="form-label">Exercise Name</label>
                        <input type="text" name="exercise_name" class="form-control" placeholder="e.g. Running, Bench Press, Yoga Flow" required>
                    </div>
                    <div class="col-md-4">
                        <label class="form-label">Duration (min)</label>
                        <input type="number" name="duration_minutes" class="form-control" placeholder="30" required min="1">
                    </div>
                    <div class="col-md-4">
                        <label class="form-label">Calories Burned</label>
                        <input type="number" name="calories_burned" class="form-control" placeholder="Optional">
                    </div>
                    <div class="col-md-4">
                        <label class="form-label">Intensity</label>
                        <select name="intensity" class="form-select">
                            <option value="low">Low</option>
                            <option value="medium" selected>Medium</option>
                            <option value="high">High</option>
                        </select>
                    </div>
                    <div class="col-md-6">
                        <label class="form-label">Sets (optional)</label>
                        <input type="number" name="sets" class="form-control" placeholder="e.g. 3">
                    </div>
                    <div class="col-md-6">
                        <label class="form-label">Reps (optional)</label>
                        <input type="number" name="reps" class="form-control" placeholder="e.g. 12">
                    </div>
                    <div class="col-12">
                        <label class="form-label">Notes</label>
                        <textarea name="notes" class="form-control" rows="2" placeholder="Any additional notes..."></textarea>
                    </div>
                    <div class="col-12 d-flex gap-2 mt-2">
                        <button type="submit" class="btn btn-primary flex-fill" style="padding:12px;">Save Workout</button>
                        <a href="{% url 'workout_list' %}" class="btn btn-outline-secondary" style="padding:12px;">Cancel</a>
                    </div>
                </div>
            </form>
        </div>
    </div>
</div>
{% endblock %}
