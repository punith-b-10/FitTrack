{% extends 'tracker/base.html' %}
{% block title %}Log Diet – FitTrack{% endblock %}
{% block content %}
<div class="d-flex justify-content-center" style="padding-top: 24px;">
    <div style="width: 100%; max-width: 560px;">
        <div class="page-header">
            <h2>🥗 Log Diet Entry</h2>
            <p style="color:var(--text-muted);">Track your meals and nutrition</p>
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
                        <label class="form-label">Meal Type</label>
                        <select name="meal_type" class="form-select" required>
                            <option value="">-- Select --</option>
                            <option value="breakfast">Breakfast</option>
                            <option value="lunch">Lunch</option>
                            <option value="dinner">Dinner</option>
                            <option value="snack">Snack</option>
                        </select>
                    </div>
                    <div class="col-md-8">
                        <label class="form-label">Food Item</label>
                        <input type="text" name="food_item" class="form-control" placeholder="e.g. Oatmeal with banana" required>
                    </div>
                    <div class="col-md-4">
                        <label class="form-label">Quantity</label>
                        <input type="text" name="quantity" class="form-control" placeholder="e.g. 1 cup" required>
                    </div>
                    <div class="col-md-3">
                        <label class="form-label">Calories</label>
                        <input type="number" name="calories" class="form-control" placeholder="kcal">
                    </div>
                    <div class="col-md-3">
                        <label class="form-label">Protein (g)</label>
                        <input type="number" step="0.1" name="protein_g" class="form-control" placeholder="g">
                    </div>
                    <div class="col-md-3">
                        <label class="form-label">Carbs (g)</label>
                        <input type="number" step="0.1" name="carbs_g" class="form-control" placeholder="g">
                    </div>
                    <div class="col-md-3">
                        <label class="form-label">Fat (g)</label>
                        <input type="number" step="0.1" name="fat_g" class="form-control" placeholder="g">
                    </div>
                    <div class="col-12">
                        <label class="form-label">Notes</label>
                        <textarea name="notes" class="form-control" rows="2" placeholder="Any notes..."></textarea>
                    </div>
                    <div class="col-12 d-flex gap-2 mt-2">
                        <button type="submit" class="btn btn-primary flex-fill" style="padding:12px;">Save Entry</button>
                        <a href="{% url 'diet_list' %}" class="btn btn-outline-secondary" style="padding:12px;">Cancel</a>
                    </div>
                </div>
            </form>
        </div>
    </div>
</div>
{% endblock %}
