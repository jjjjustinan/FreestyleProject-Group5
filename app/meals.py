import requests
import json


def search_by_ingredient(ingredient):
    request_url = f"https://www.themealdb.com/api/json/v1/1/filter.php?i={ingredient}"
    meal_data = requests.get(request_url).json()
    return meal_data


def search_by_category(category):
    request_url = f"https://www.themealdb.com/api/json/v1/1/filter.php?c={category}"
    meal_data = requests.get(request_url).json()
    return meal_data


def search_by_area(area):
    request_url = f"https://www.themealdb.com/api/json/v1/1/filter.php?a={area}"
    meal_data = requests.get(request_url).json()
    return meal_data

def run_csv(i, c, a):
    ids_ingredient = set()
    ids_category = set()
    ids_area = set()

    # Flags to check if any criteria are provided
    criteria_provided = False

    # Collect ids if ingredient is provided and not just spaces
    if i and i.strip():
        criteria_provided = True
        results1 = search_by_ingredient(i.strip())
        if results1 and results1["meals"]:
            ids_ingredient = {food["idMeal"] for food in results1["meals"]}

    # Collect ids if category is provided and not just spaces
    if c and c.strip():
        criteria_provided = True
        results2 = search_by_category(c.strip())
        if results2 and results2["meals"]:
            ids_category = {food["idMeal"] for food in results2["meals"]}

    # Collect ids if area is provided and not just spaces
    if a and a.strip():
        criteria_provided = True
        results3 = search_by_area(a.strip())
        if results3 and results3["meals"]:
            ids_area = {food["idMeal"] for food in results3["meals"]}

    # Initialize the dictionary
    d = {}

    # Find the intersection of ids if any criteria are provided, else return all meals
    if criteria_provided:
        all_ids = [ids_ingredient, ids_category, ids_area]
        valid_ids = set.intersection(*[ids for ids in all_ids if ids])

        if valid_ids:
            for id in valid_ids:
                meal_details = fetch_id(id)
                if meal_details:
                    d[id] = meal_details
    else:
        d = {}

    return d

def fetch_id(meal_id):
    request_url = f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={meal_id}"
    response = requests.get(request_url)
    
    if response.status_code == 200:
        meal_data = response.json()
        if meal_data and meal_data["meals"]:
            meal = meal_data["meals"][0]
            return {
                "name": meal["strMeal"],
                "image": meal["strMealThumb"]
            }
        else:
            return None
    else:
        return None

def recipe_search(id):
    request_url = f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={id}"
    recipe_data = requests.get(request_url).json()

    recipe_name = recipe_data["meals"][0]['strMeal']
    recipe_picture = recipe_data["meals"][0]['strMealThumb']
    meal_category = recipe_data['meals'][0]['strCategory']
    meal_area = recipe_data['meals'][0]['strArea']

    ingredients_data = recipe_data["meals"][0]

    ingredients = []

    for i in range(1, 21):
        ingredient_key = f"strIngredient{i}"
        measure_key = f"strMeasure{i}"
        ingredient = ingredients_data.get(ingredient_key)
        measure = ingredients_data.get(measure_key)
        if ingredient and ingredient.strip():
            ingredients.append(f"{measure} {ingredient}")


    meal_instructions = recipe_data['meals'][0]['strInstructions']
    meal_instructions = meal_instructions.replace(". ", ".<br>")

    recipe = {'name':recipe_name, 'thumb':recipe_picture, 'ingredients':ingredients, 'instructions':meal_instructions, 'category':meal_category, 'area':meal_area}

    return recipe


if __name__ == '"__main__':
    print('\nFind Recipe\n')

    name = input("\nEnter a meal name: ")

    meal_data = search_by_ingredient(name)

    print(meal_data)
