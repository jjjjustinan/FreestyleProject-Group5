import requests
import json


def search_by_ingredient(ingredient):
    request_url = f"https://www.themealdb.com/api/json/v1/1/search.php?i={ingredient}"
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
    d ={}
    results1 = search_by_ingredient(i)
    results2 = search_by_category(c)
    results3 = search_by_area(a)

    ingredientarr = results1["meals"]
    categoryarr = results2["meals"]
    areaarr = results3["meals"]
    
    for food in ingredientarr:
        if food["idMeal"] not in d:
            d[food["idMeal"]] = food["strMeal"]
    
    for food in categoryarr:
        if food["idMeal"] not in d:
            d[food["idMeal"]] = food["strMeal"]
    
    for food in areaarr:
        if food["idMeal"] not in d:
            d[food["idMeal"]] = food["strMeal"]
    
    for key in d:
        print(d[key])
    
    return d

def recipe_search(id):
    request_url = f"www.themealdb.com/api/json/v1/1/lookup.php?i={id}"
    recipe_data = requests.get(request_url).json()

    recipe_name = recipe_data["meals"][0]['strMeal']
    recipe_picture = recipe_data["meals"][0]['strMealThumb']
    ingredients = []
    measurements = []

    i = 1

    while i <= 20:

        meal_ingredient = recipe_data['drinks'][0]['strIngredient' + str(i)]
        meal_measure = recipe_data['drinks'][0]['strMeasure' + str(i)]

        if meal_ingredient != None:
            ingredients.append(meal_ingredient)


        if meal_measure != None:
            measurements.append(meal_measure)

        i += 1


    meal_instructions = recipe_data['drinks'][0]['strInstructions']

    meal_category = recipe_data['drinks'][0]['strCategory']

    recipe = {'name':recipe_name, 'thumb':recipe_picture, 'ingredients':ingredients, 'measurements': measurements, 'instructions':meal_instructions, 'category':meal_category}

    return recipe


if __name__ == '"__main__':
    print('\nFind Recipe\n')

    name = input("\nEnter a meal name: ")

    meal_data = search_by_name(name)

    print(meal_data)
