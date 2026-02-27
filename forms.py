{% extends 'tracker/base.html' %}
{% block title %}Diet History – FitTrack{% endblock %}
{% block content %}
<div class="page-header d-flex justify-content-between align-items-center">
    <div>
        <h2>🥗 Diet History</h2>
        <p style="color:var(--text-muted);">All your logged meals and nutrition</p>
    </div>
    <a href="{% url 'log_diet' %}" class="btn btn-primary"><i class="bi bi-plus-lg"></i> Log Meal</a>
</div>

<div class="card">
    <div class="card-body p-0">
        {% if diets %}
        <div class="table-responsive">
            <table class="table mb-0">
                <thead>
                    <tr><th>Date</th><th>Meal</th><th>Food</th><th>Quantity</th><th>Calories</th><th>Protein</th><th>Carbs</th><th>Fat</th><th></th></tr>
                </thead>
                <tbody>
                    {% for d in diets %}
                    <tr>
                        <td style="color:var(--text-muted); white-space:nowrap;">{{ d.date|date:"M d, Y" }}</td>
                        <td><span class="badge bg-info bg-opacity-25 text-info">{{ d.get_meal_type_display }}</span></td>
                        <td><strong>{{ d.food_item }}</strong></td>
                        <td style="color:var(--text-muted);">{{ d.quantity }}</td>
                        <td>{% if d.calories %}{{ d.calories }}{% else %}–{% endif %}</td>
                        <td>{% if d.protein_g %}{{ d.protein_g }}g{% else %}–{% endif %}</td>
                        <td>{% if d.carbs_g %}{{ d.carbs_g }}g{% else %}–{% endif %}</td>
                        <td>{% if d.fat_g %}{{ d.fat_g }}g{% else %}–{% endif %}</td>
                        <td>
                            <a href="{% url 'delete_diet' d.pk %}" class="btn btn-outline-danger btn-sm"
                               onclick="return confirm('Delete this entry?')">
                                <i class="bi bi-trash"></i>
                            </a>
                        </td>
                    </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
        {% else %}
        <div class="p-5 text-center">
            <i class="bi bi-egg-fried" style="font-size:3rem; color:var(--text-muted);"></i>
            <p class="mt-3" style="color:var(--text-muted);">No diet entries yet.</p>
            <a href="{% url 'log_diet' %}" class="btn btn-primary">Log Your First Meal</a>
        </div>
        {% endif %}
    </div>
</div>
{% endblock %}
