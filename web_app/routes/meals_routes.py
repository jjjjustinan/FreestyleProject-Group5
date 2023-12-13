from app.meals import *
from flask import Blueprint, Flask, request, render_template
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



@meals_routes.route('/meal/<meal_id>')
def recipe_page(meal_id):
    meal_details = recipe_search(meal_id)

    if meal_details:
        # Render a template with meal details
        return render_template('recipe.html', meal_details=meal_details)
    else:
        # Handle the case where no details are found (e.g., render a 'not found' page or message)
        return 0

