# MealDB Cookbook

## Setup

Create and activate a virtual environment:

```sh
conda create -n mealDB python=3.10

conda activate mealDB
```
Obtain an [API Key from The Meal DB](https://www.themealdb.com/api.php)

Please email sign up on Paypal and/or email thedatadb@gmail.com to obtain a key upgrade. Otherwise, use the API key "1".

Then, please obtain a SendGrid API key from https://sendgrid.com/en-us and a SENDER_ADDRESS.

Create a ".env" file and paste in the following contents:

```sh
# this is the ".env" file...

MEALDB_API_KEY="______"
SENDGRID_API_KEY="_________"
SENDER_ADDRESS="example.gmail.com"


## Usage

Install packages:
```sh
pip install -r requirements.txt
```

### Web App

Run the web app (then view in the browser at http://localhost:5000/):

```sh
# Mac OS:
FLASK_APP=web_app flask run

# Windows OS:
# ... if `export` doesn't work for you, try `set` instead
# ... or set FLASK_APP variable via ".env" file
export FLASK_APP=web_app
flask run
```