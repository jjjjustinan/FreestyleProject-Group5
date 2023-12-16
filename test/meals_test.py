from app.meals import search_by_ingredient, search_by_category, search_by_area, run_csv, fetch_id, recipe_search

def test_search_by_ingredient():
    
    data = search_by_ingredient("chicken_breast")
    assert isinstance(data, dict), """{"meals":[{"strMeal":"Chick-Fil-A Sandwich","strMealThumb":"https:\/\/www.themealdb.com\/images\/media\/meals\/sbx7n71587673021.jpg","idMeal":"53016"},{"strMeal":"Chicken Couscous","strMealThumb":"https:\/\/www.themealdb.com\/images\/media\/meals\/qxytrx1511304021.jpg","idMeal":"52850"},{"strMeal":"Chicken Fajita Mac and Cheese","strMealThumb":"https:\/\/www.themealdb.com\/images\/media\/meals\/qrqywr1503066605.jpg","idMeal":"52818"},{"strMeal":"Chicken Ham and Leek Pie","strMealThumb":"https:\/\/www.themealdb.com\/images\/media\/meals\/xrrtss1511555269.jpg","idMeal":"52875"},{"strMeal":"Chicken Quinoa Greek Salad","strMealThumb":"https:\/\/www.themealdb.com\/images\/media\/meals\/k29viq1585565980.jpg","idMeal":"53011"},{"strMeal":"General Tso's Chicken","strMealThumb":"https:\/\/www.themealdb.com\/images\/media\/meals\/1529444113.jpg","idMeal":"52951"},{"strMeal":"Honey Balsamic Chicken with Crispy Broccoli & Potatoes","strMealThumb":"https:\/\/www.themealdb.com\/images\/media\/meals\/kvbotn1581012881.jpg","idMeal":"52993"},{"strMeal":"Katsu Chicken curry","strMealThumb":"https:\/\/www.themealdb.com\/images\/media\/meals\/vwrpps1503068729.jpg","idMeal":"52820"},{"strMeal":"Rappie Pie","strMealThumb":"https:\/\/www.themealdb.com\/images\/media\/meals\/ruwpww1511817242.jpg","idMeal":"52933"}]}"""

def test_search_by_category():
    data = search_by_category("vegan")
    assert isinstance(data, dict), """{"meals":[{"strMeal":"Roast fennel and aubergine paella","strMealThumb":"https:\/\/www.themealdb.com\/images\/media\/meals\/1520081754.jpg","idMeal":"52942"},{"strMeal":"Vegan Chocolate Cake","strMealThumb":"https:\/\/www.themealdb.com\/images\/media\/meals\/qxutws1486978099.jpg","idMeal":"52794"},{"strMeal":"Vegan Lasagna","strMealThumb":"https:\/\/www.themealdb.com\/images\/media\/meals\/rvxxuy1468312893.jpg","idMeal":"52775"}]}"""

def test_search_by_area():
    data = search_by_area("canadian")
    assert isinstance(data, dict), """{"meals":[{"strMeal":"BeaverTails","strMealThumb":"https:\/\/www.themealdb.com\/images\/media\/meals\/ryppsv1511815505.jpg","idMeal":"52928"},{"strMeal":"Breakfast Potatoes","strMealThumb":"https:\/\/www.themealdb.com\/images\/media\/meals\/1550441882.jpg","idMeal":"52965"},{"strMeal":"Canadian Butter Tarts","strMealThumb":"https:\/\/www.themealdb.com\/images\/media\/meals\/wpputp1511812960.jpg","idMeal":"52923"},{"strMeal":"Montreal Smoked Meat","strMealThumb":"https:\/\/www.themealdb.com\/images\/media\/meals\/uttupv1511815050.jpg","idMeal":"52927"},{"strMeal":"Nanaimo Bars","strMealThumb":"https:\/\/www.themealdb.com\/images\/media\/meals\/vwuprt1511813703.jpg","idMeal":"52924"},{"strMeal":"Pate Chinois","strMealThumb":"https:\/\/www.themealdb.com\/images\/media\/meals\/yyrrxr1511816289.jpg","idMeal":"52930"},{"strMeal":"Pouding chomeur","strMealThumb":"https:\/\/www.themealdb.com\/images\/media\/meals\/yqqqwu1511816912.jpg","idMeal":"52932"},{"strMeal":"Poutine","strMealThumb":"https:\/\/www.themealdb.com\/images\/media\/meals\/uuyrrx1487327597.jpg","idMeal":"52804"},{"strMeal":"Rappie Pie","strMealThumb":"https:\/\/www.themealdb.com\/images\/media\/meals\/ruwpww1511817242.jpg","idMeal":"52933"},{"strMeal":"Split Pea Soup","strMealThumb":"https:\/\/www.themealdb.com\/images\/media\/meals\/xxtsvx1511814083.jpg","idMeal":"52925"},{"strMeal":"Sugar Pie","strMealThumb":"https:\/\/www.themealdb.com\/images\/media\/meals\/yrstur1511816601.jpg","idMeal":"52931"},{"strMeal":"Timbits","strMealThumb":"https:\/\/www.themealdb.com\/images\/media\/meals\/txsupu1511815755.jpg","idMeal":"52929"},{"strMeal":"Tourtiere","strMealThumb":"https:\/\/www.themealdb.com\/images\/media\/meals\/ytpstt1511814614.jpg","idMeal":"52926"}]}"""

def test_run_csv():
    data = run_csv("chicken", " ", " ")
    assert isinstance(data, dict), """{'52945': {'name': 'Kung Pao Chicken', 'image': 'https://www.themealdb.com/images/media/meals/1525872624.jpg'}, '53039': {'name': 'Piri-piri chicken and slaw', 'image': 'https://www.themealdb.com/images/media/meals/hglsbl1614346998.jpg'}, '52814': {'name': 'Thai Green Curry', 'image': 'https://www.themealdb.com/images/media/meals/sstssx1487349585.jpg'}, '52813': {'name': 'Kentucky Fried Chicken', 'image': 'https://www.themealdb.com/images/media/meals/xqusqy1487348868.jpg'}, '52934': {'name': 'Chicken Basquaise', 'image': 'https://www.themealdb.com/images/media/meals/wruvqv1511880994.jpg'}, '52796': {'name': 'Chicken Alfredo Primavera', 'image': 'https://www.themealdb.com/images/media/meals/syqypv1486981727.jpg'}, '52795': {'name': 'Chicken Handi', 'image': 'https://www.themealdb.com/images/media/meals/wyxwsp1486979827.jpg'}, '52846': {'name': 'Chicken & mushroom Hotpot', 'image': 'https://www.themealdb.com/images/media/meals/uuuspp1511297945.jpg'}, '52940': {'name': 'Brown Stew Chicken', 'image': 'https://www.themealdb.com/images/media/meals/sypxpx1515365095.jpg'}, '52774': {'name': 'Pad See Ew', 'image': 'https://www.themealdb.com/images/media/meals/uuuspp1468263334.jpg'}, '52956': {'name': 'Chicken Congee', 'image': 'https://www.themealdb.com/images/media/meals/1529446352.jpg'}}"""

def test_fetch_id():
    data = fetch_id("52956")
    assert isinstance(data, dict), """{'name': 'Chicken Congee', 'image': 'https://www.themealdb.com/images/media/meals/1529446352.jpg'}"""

def test_recipe_search():
    data = recipe_search("52956")
    assert isinstance(data, dict), """{'name': 'Chicken Congee', 'thumb': 'https://www.themealdb.com/images/media/meals/1529446352.jpg', 'ingredients': ['8 oz  Chicken', 'pinch Salt', 'pinch Pepper', '1 tsp  Ginger Cordial', '1 tsp  Ginger', '1 tbs Spring Onions', '1/2 cup  Rice', '8 cups  Water', '2 oz  Coriander'], 'instructions': 'STEP 1 - MARINATING THE CHICKEN\r\nIn a bowl, add chicken, salt, white pepper, ginger juice and then mix it together well.\r\nSet the chicken aside.\r\nSTEP 2 - RINSE THE WHITE RICE\r\nRinse the rice in a metal bowl or pot a couple times and then drain the water.\r\nSTEP 2 - BOILING THE WHITE RICE\r\nNext add 8 cups of water and then set the stove on high heat until it is boiling.<br>Once rice porridge starts to boil, set the stove on low heat and then stir it once every 8-10 minutes for around 20-25 minutes.\r\nAfter 25 minutes, this is optional but you can add a little bit more water to make rice porridge to make it less thick or to your preference.\r\nNext add the marinated chicken to the rice porridge and leave the stove on low heat for another 10 minutes.\r\nAfter an additional 10 minutes add the green onions, sliced ginger, 1 pinch of salt, 1 pinch of white pepper and stir for 10 seconds.\r\nServe the rice porridge in a bowl\r\nOptional: add Coriander on top of the rice porridge.', 'category': 'Chicken', 'area': 'Chinese'}"""

