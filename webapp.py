from dataclasses import dataclass
from flask import Flask, url_for, render_template, request, Markup
import json

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

with open("ingredients.json") as file:
    food = json.load(file)
    
ingredients = ""
for i in food:
    ing =  i['Description']
    ingredients += Markup('<option>') + ing + Markup('</option>')
    
@app.route("/")
def render_main():
    return render_template("home.html")

@app.route("/calculator")
def render_calc():
    return render_template("calculator.html", ingredients = ingredients)

@app.route("/lib")
def render_lib():
    return render_template("library.html", ingredients = ingredients)

@app.route("/form")
def render_input():
    uIng = request.args["ingredient"]
    fat = ""
    for i in food:
        data = i['Description']
        if data == uIng:
            fat = round(i["Data"]["Fat"]["Total Lipid"])
            fatDv = round(fat/65*100)
            satfat = round(i["Data"]["Fat"]["Saturated Fat"])
            satfatDv = round(satfat/20*100)
            chole = round(i["Data"]["Cholesterol"])
            choleDv = round(chole/300*100)
            sodium = round(i["Data"]["Major Minerals"]["Sodium"])
            sodiumDv = round(sodium/2400*100)
            carbs = round(i["Data"]["Carbohydrate"])
            carbsDv = round(carbs/300*100)
            fiber = round(i["Data"]["Fiber"])
            fiberDv = round(fiber/25*100)
            sugar = round(i["Data"]["Sugar Total"])
            protein = round(i["Data"]["Protein"])
            vitA = round(i["Data"]["Vitamins"]["Vitamin A - RAE"]/1000*100)
            vitC = round(i["Data"]["Vitamins"]["Vitamin C"]/60*100)
            calcium = round(i["Data"]["Major Minerals"]["Calcium"]/1100*100)
            iron = round(i["Data"]["Major Minerals"]["Iron"]/14*100)
            cal = fat*9 + carbs*4 + protein*4
            calfat = fat*9
        
    return render_template(
        "output.html", 
        Fat = fat, 
        FatDv = fatDv, 
        SatFat = satfat, 
        SatFatDv = satfatDv, 
        Chole = chole, 
        CholeDv = choleDv, 
        Sodium = sodium, 
        SodiumDv = sodiumDv, 
        Carbs = carbs, 
        CarbsDv = carbsDv,
        Fiber = fiber,
        FiberDv = fiberDv,
        Sugar = sugar,
        Protein = protein,
        VitA = vitA,
        VitC = vitC,
        Calcium = calcium,
        Iron = iron,
        Calories = cal,
        FatCalories = calfat)
        
    
if __name__=="__main__":
    app.run(debug=False)