import requests
from pprint import pprint

from flask import Flask, render_template
app =Flask(__name__)

@app.route('/')
def recipes_site():
    return render_template('RecipesWebsite.html')

app.run(debug=True)


def ingredient_search(ingredient_name):

    key = "9b6153cb33143e8ec7ab80c6c9a93eb2&"

    url='https://www.food2fork.com/api/search?key={}q={}'.format(key, ingredient_name)

    response=requests.get(url)

    recipe=response.json()
    return recipe




ingredient_name = input('What ingredient? ')

recipes = ingredient_search(ingredient_name)

pprint(recipes)