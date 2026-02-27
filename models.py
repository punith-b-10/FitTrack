{% extends 'tracker/base.html' %}
{% block title %}Dashboard – FitTrack{% endblock %}
{% block content %}

<div class="page-header d-flex justify-content-between align-items-center">
    <div>
        <h2>Dashboard</h2>
        <p style="color:var(--text-muted); margin:0;">{{ today|date:"l, F j, Y" }}</p>
    </div>
    <div class="d-flex gap-2">
        <a href="{% url 'log_workout' %}" class="btn btn-outline-primary btn-sm"><i class="bi bi-plus-lg"></i> Workout</a>
        <a href="{% url 'log_diet' %}" class="btn btn-outline-primary btn-sm"><i class="bi bi-plus-lg"></i> Diet</a>
        <a href="{% url 'log_metric' %}" class="btn btn-primary btn-sm"><i class="bi bi-plus-lg"></i> Metrics</a>
    </div>
</div>

<!-- Stat Cards -->
<div class="row g-3 mb-4">
    <div class="col-6 col-md-3">
        <div class="stat-card">
            <div class="d-flex justify-content-between">
                <div>
                    <div class="stat-value">
                        {% if latest_metric %}{{ latest_metric.weight_kg }}<small style="font-size:1rem;">kg</small>{% else %}--{% endif %}
                    </div>
                    <div class="stat-label">Current Weight</div>
                </div>
                <div class="stat-icon text-success"><i class="bi bi-person-standing"></i></div>
            </div>
            {% if ideal_low %}
            <div class="mt-2" style="font-size:0.78rem; color:var(--text-muted);">Ideal: {{ ideal_low }}–{{ ideal_high }} kg</div>
            {% endif %}
        </div>
    </div>
    <div class="col-6 col-md-3">
        <div class="stat-card">
            <div class="d-flex justify-content-between">
                <div>
                    <div class="stat-value {% if bmi_category == 'Normal' %}bmi-normal{% elif bmi_category == 'Overweight' %}bmi-overweight{% elif bmi_category == 'Obese' %}bmi-obese{% else %}bmi-underweight{% endif %}">
                        {% if bmi %}{{ bmi }}{% else %}--{% endif %}
                    </div>
                    <div class="stat-label">BMI – {{ bmi_category|default:"N/A" }}</div>
                </div>
                <div class="stat-icon"><i class="bi bi-heart-pulse"></i></div>
            </div>
        </div>
    </div>
    <div class="col-6 col-md-3">
        <div class="stat-card">
            <div class="d-flex justify-content-between">
                <div>
                    <div class="stat-value" style="color:var(--warning);">{{ total_workout_mins }}<small style="font-size:1rem;">m</small></div>
                    <div class="stat-label">Workout This Week</div>
                </div>
                <div class="stat-icon" style="color:var(--warning);"><i class="bi bi-lightning-charge"></i></div>
            </div>
            <div class="mt-2" style="font-size:0.78rem; color:var(--text-muted);">{{ total_calories_burned }} kcal burned</div>
        </div>
    </div>
    <div class="col-6 col-md-3">
        <div class="stat-card">
            <div class="d-flex justify-content-between">
                <div>
                    <div class="stat-value" style="color:var(--info);">{{ calories_today }}<small style="font-size:1rem;">kcal</small></div>
                    <div class="stat-label">Calories Today</div>
                </div>
                <div class="stat-icon" style="color:var(--info);"><i class="bi bi-egg-fried"></i></div>
            </div>
            <div class="mt-2" style="font-size:0.78rem; color:var(--text-muted);">{{ protein_today }}g protein</div>
        </div>
    </div>
</div>

<!-- Charts Row -->
<div class="row g-3 mb-4">
    <div class="col-md-8">
        <div class="card h-100">
            <div class="card-header p-3">⚖️ Weight Trend (Last 30 Days)</div>
            <div class="card-body">
                <div class="chart-container">
                    <canvas id="weightChart"></canvas>
                </div>
                {% if not latest_metric %}
                <div class="text-center py-4" style="color:var(--text-muted);">
                    No data yet. <a href="{% url 'log_metric' %}" style="color:var(--primary);">Log your first body metric</a>
                </div>
                {% endif %}
            </div>
        </div>
    </div>
    <div class="col-md-4">
        <div class="card h-100">
            <div class="card-header p-3">🏋️ Workout Types</div>
            <div class="card-body d-flex align-items-center justify-content-center">
                <div class="chart-container w-100">
                    <canvas id="workoutChart"></canvas>
                </div>
                {% if not recent_workouts %}
                <div class="text-center" style="color:var(--text-muted);">
                    No workouts yet. <a href="{% url 'log_workout' %}" style="color:var(--primary);">Log one!</a>
                </div>
                {% endif %}
            </div>
        </div>
    </div>
</div>

<!-- Recent Activity -->
<div class="row g-3">
    <div class="col-md-6">
        <div class="card">
            <div class="card-header p-3 d-flex justify-content-between align-items-center">
                <span>⚡ Recent Workouts</span>
                <a href="{% url 'workout_list' %}" style="font-size:0.8rem; color:var(--primary); font-family:'DM Sans',sans-serif;">View All</a>
            </div>
            <div class="card-body p-0">
                {% if recent_workouts %}
                <table class="table mb-0">
                    <thead><tr><th>Exercise</th><th>Type</th><th>Duration</th><th>Date</th></tr></thead>
                    <tbody>
                        {% for w in recent_workouts %}
                        <tr>
                            <td><strong>{{ w.exercise_name }}</strong></td>
                            <td><span class="badge bg-success bg-opacity-25 text-success" style="font-size:0.73rem;">{{ w.get_workout_type_display }}</span></td>
                            <td>{{ w.duration_minutes }}m</td>
                            <td style="color:var(--text-muted);">{{ w.date|date:"M d" }}</td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
                {% else %}
                <div class="p-4 text-center" style="color:var(--text-muted);">No workouts logged yet.</div>
                {% endif %}
            </div>
        </div>
    </div>
    <div class="col-md-6">
        <div class="card">
            <div class="card-header p-3 d-flex justify-content-between align-items-center">
                <span>🥗 Recent Diet</span>
                <a href="{% url 'diet_list' %}" style="font-size:0.8rem; color:var(--primary); font-family:'DM Sans',sans-serif;">View All</a>
            </div>
            <div class="card-body p-0">
                {% if recent_diet %}
                <table class="table mb-0">
                    <thead><tr><th>Food</th><th>Meal</th><th>Calories</th><th>Date</th></tr></thead>
                    <tbody>
                        {% for d in recent_diet %}
                        <tr>
                            <td><strong>{{ d.food_item }}</strong></td>
                            <td><span class="badge bg-info bg-opacity-25 text-info" style="font-size:0.73rem;">{{ d.get_meal_type_display }}</span></td>
                            <td>{% if d.calories %}{{ d.calories }}{% else %}--{% endif %}</td>
                            <td style="color:var(--text-muted);">{{ d.date|date:"M d" }}</td>
                        </tr>
                        {% endfor %}
                    </tbody>
                </table>
                {% else %}
                <div class="p-4 text-center" style="color:var(--text-muted);">No diet entries yet.</div>
                {% endif %}
            </div>
        </div>
    </div>
</div>

{% endblock %}

{% block extra_js %}
<script>
const chartDefaults = {
    color: '#6b7c6b',
    font: { family: 'DM Sans' }
};
Chart.defaults.color = chartDefaults.color;
Chart.defaults.font.family = chartDefaults.font.family;

// Weight Chart
const weightLabels = {{ weight_labels|safe }};
const weightData = {{ weight_data|safe }};

if (weightLabels.length > 0) {
    new Chart(document.getElementById('weightChart'), {
        type: 'line',
        data: {
            labels: weightLabels,
            datasets: [{
                label: 'Weight (kg)',
                data: weightData,
                borderColor: '#00e676',
                backgroundColor: 'rgba(0,230,118,0.08)',
                borderWidth: 2.5,
                pointBackgroundColor: '#00e676',
                pointRadius: 4,
                tension: 0.4,
                fill: true,
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            plugins: { legend: { display: false } },
            scales: {
                x: { grid: { color: '#1e2e1e' }, ticks: { maxTicksLimit: 7 } },
                y: { grid: { color: '#1e2e1e' }, ticks: { callback: v => v + ' kg' } }
            }
        }
    });
}

// Workout Donut Chart
const wLabels = {{ workout_type_labels|safe }};
const wData = {{ workout_type_data|safe }};

if (wLabels.length > 0) {
    new Chart(document.getElementById('workoutChart'), {
        type: 'doughnut',
        data: {
            labels: wLabels,
            datasets: [{
                data: wData,
                backgroundColor: ['#00e676','#40c4ff','#ffab40','#ff5252','#ce93d8','#80cbc4'],
                borderWidth: 0,
            }]
        },
        options: {
            responsive: true,
            maintainAspectRatio: false,
            cutout: '65%',
            plugins: {
                legend: { position: 'bottom', labels: { padding: 12, boxWidth: 12 } }
            }
        }
    });
}
</script>
{% endblock %}
