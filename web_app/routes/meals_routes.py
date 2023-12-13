from app.meals import *
from flask import Flask, request, render_template
import pandas as pd

@app.route('/', methods=['POST', 'GET'])
def root_page():
    i = ''
    c = ''
    a = ''
    if request.method == 'POST' and ('i' and 'c' and 'a') in request.form:
        ingredient = request.form.get('i')
        category = request.form.get('c')
        area = request.form.get('a')
        run_csv(i, c, a)
    return render_template("index.html", ingredient=ingredient, category=category, area=area)


@app.route('/meal', methods=['GET', 'POST'])
def meal_page():
    return render_template('meal.html')

@app.route('/meal/recipe', methods=['GET', 'POST'])
def recipe_page():
    return render_template('recipe.html')