def search_meal(name:str, random:bool = False) -> str:
    if not random:
        URL = f"https://www.themealdb.com/api/json/v1/1/search.php?s={name}"
    else:
        URL = "https://www.themealdb.com/api/json/v1/1/random.php"
        
    try:
        req = requests.get(URL)
        content = json.loads(req.text)

        #Access stuff
        content = content["meals"]

        if not content:
            os.system("color E")
            return print(f"\nNothing found for {name}!\n")
        
    except Exception as ex:
        os.system("color 4")
        return print(f"\nUh Oh, something was done wrong!\nDetails: {ex}")

    #print(content)

    #Access every dictionary in list and gather values
    for c,element in enumerate(content,start=1):
        #strIngredients and strMeasures
        ingredient = [f"strIngredient{x}" for x in range(1, 21)]
        measure = [f"strMeasure{x}" for x in range(1, 21)]
        ingredients = []
        measures = []

        #Get all possible existing ingredients in a range from 1 to 20
        for n in ingredient:
            try:
                current_ingredient = element[n]
                ingredients.append(current_ingredient)
            except:
                continue
        for n in measure:
            try:
                current_measure = element[n]
                measures.append(current_measure)
            except:
                continue
            
        #Remove NoneType values
        ingredients = list(filter(lambda x: x is not None, ingredients))
        measures = list(filter(lambda x: x is not None, measures))

        #Assign number on each elemnt
        for i in range(len(measures)):
            measures[i] = f"[{str(i+1)}] {measures[i]}" #Assign the number i that takes the value of each list's index and format it to the ingredients name (weird to explain)

        m_i = list(zip(measures,ingredients))
        
        #Get info
        name = element["strMeal"]
        category = element["strCategory"]
        Area:str = element["strArea"]
        instructions: str = element["strInstructions"]