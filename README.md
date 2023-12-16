# MealDB Cookbook

This web app is designed to take in user input of a choice of ingredient, category, and area of cuisine, or a combination of the three, and provide you with a list of possible dishes you could make that fulfills these filters. Then, once you select a dish, you are given the name of the dish, a picture, ingredients, instructions, and the category and area! To make the user experience even better, you are able to email the recipe to yourself or someone else to save the recipe, making it much easier for you to access later on!

## Setup

Create and activate a virtual environment:

```sh
conda create -n mealDB python=3.10

conda activate mealDB
```
Obtain an [API Key from The Meal DB](https://www.themealdb.com/api.php)

Please sign up on Paypal and/or email thedatadb@gmail.com to obtain a key upgrade. Otherwise, use the API key "1".

Then, please obtain a SendGrid API key from https://sendgrid.com/en-us and a SENDER_ADDRESS.

Create a ".env" file and paste in the following contents:

```sh
# this is the ".env" file...

MEALDB_API_KEY="_____"
SENDGRID_API_KEY="_______"
SENDER_ADDRESS="______"

```
After activating your environment, you should use this command to install all of the necessary packages to run the program.

## Usage

Install packages:
```sh
pip install -r requirements.txt
```

To test to make sure all functions are working properly, you can use the command, pytest.
## Testing

```sh
pytest
```

### Web App

Run the web app using these commands (then view in the browser at http://localhost:5000/):

```sh
For Mac OS:
FLASK_APP=web_app flask run

For Windows OS:
export FLASK_APP=web_app
flask run
```
If `export` doesn't work for you, try `set` instead
```sh
set FLASK_APP=web_app
flask run
```
Or set FLASK_APP variable via the .env file

## [Deployment Guide](/DEPLOYING.md)

### Live App
To access the web app, you can click this link at https://freestyleprojectgroup5-2023.onrender.com/ and try our app for yourself!