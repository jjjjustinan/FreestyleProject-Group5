from app.meals import *
from app.email_service import *
from flask import Blueprint, Flask, request, render_template, render_template_string
import pandas as pd

meals_routes = Blueprint("meals_routes", __name__)


@meals_routes.route('/')
def root_page():
    return render_template("index.html")


@meals_routes.route('/meal', methods=['GET', 'POST'])
def meal_page():
    if request.method == "POST":
        # for data sent via POST request, form inputs are in request.form:
        request_data = dict(request.form)
    else:
        # for data sent via GET request, url params are in request.args
        request_data = dict(request.args)

    i = ''
    c = ''
    a = ''

    i = request_data.get("i")
    c = request_data.get("c")
    a = request_data.get("a")

    meal_dict = run_csv(i, c, a)

    return render_template("meals.html", meal_dict=meal_dict, i=i, c=c, a=a)



@meals_routes.route('/meal/<meal_id>', methods=['GET', 'POST'])
def recipe_page(meal_id):
    meal_details = recipe_search(meal_id)  # Replace with your actual data retrieval logic

    if request.method == 'POST':
        recipient_email = request.form['email']
        if meal_details and recipient_email:
            # Render the HTML content for the email
            html_content = render_template_string("""
                <div class="container mt-4">
    <h2 class="mb-3">{{ meal_details.name }}</h2>

    <!-- Meal Image -->
    <div class="row mb-4">
        <div class="col">
            <img src="{{ meal_details.thumb }}" class="img-fluid" alt="{{ meal_details.name }}">
        </div>
    </div>

    <!-- Meal Details -->
    <div class="row">
        <div class="col-md-6">
            <h3>Ingredients</h3>
            <table class="table">
                <tbody>
                    {% for ingredient in meal_details.ingredients %}
                        <tr>
                            <td>{{ ingredient }}</td>
                        </tr>
                    {% endfor %}
                </tbody>
            </table>
        </div>
        <div class="col-md-6">
            <h4>Instructions</h4>
            <p>{{ meal_details.instructions | safe }}</p>

            <h4>Category</h4>
            <p>{{ meal_details.category }}</p>

            <h4>Area</h4>
            <p>{{ meal_details.area }}</p>
        </div>
    </div>
</div>
            """, meal_details=meal_details)

            # Send the email with the rendered HTML content
            send_email(recipient_address=recipient_email, html_content=html_content)

            # Return a confirmation message or page
            return render_template('recipe.html', meal_details=meal_details, meal_id=meal_id,)

    if meal_details:
        return render_template('recipe.html', meal_details=meal_details, meal_id=meal_id)
    else:
        return "No meal details found"