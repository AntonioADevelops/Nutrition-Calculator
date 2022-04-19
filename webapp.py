from dataclasses import dataclass
from flask import Flask, request_started, url_for, render_template, request, Markup
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
        FoodName = uIng,
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
        
@app.route("/formcalc")
def render_calc_input():
    uIng = []
    for keys in request.args.keys():
        if keys != "amount":
            uIng.append(request.args[keys])
    uAmt = float(request.args["amount"])
    sumfat = 0
    sumfatDv = 0
    sumsatfat = 0
    sumsatfatDv = 0
    sumchole = 0
    sumcholeDv = 0
    sumsodium = 0
    sumsodiumDv = 0
    sumcarbs = 0
    sumcarbsDv = 0
    sumfiber = 0
    sumfiberDv = 0
    sumsugar = 0
    sumprotein = 0
    sumvitA = 0
    sumvitC = 0
    sumcalcium = 0
    sumiron = 0
    for i in food:
        data = i['Description']
        if data in uIng:
            fat = round(i["Data"]["Fat"]["Total Lipid"]*uAmt)
            sumfat = sumfat + fat
            fatDv = round(fat/65*100)
            sumfatDv = sumfatDv + fatDv
            satfat = round(i["Data"]["Fat"]["Saturated Fat"]*uAmt)
            sumsatfat = sumfatDv + fatDv
            satfatDv = round(satfat/20*100)
            sumsatfatDv = sumsatfatDv + satfatDv
            chole = round(i["Data"]["Cholesterol"]*uAmt)
            sumchole = sumchole + fatDv
            choleDv = round(chole/300*100)
            sumcholeDv = sumcholeDv + choleDv
            sodium = round(i["Data"]["Major Minerals"]["Sodium"]*uAmt)
            sumsodium= sumsodium + sodium
            sodiumDv = round(sodium/2400*100)
            sumsodiumDv= sumsodiumDv + sodiumDv
            carbs = round(i["Data"]["Carbohydrate"]*uAmt)
            sumcarbs = sumcarbs + carbs
            carbsDv = round(carbs/300*100)
            sumcarbsDv = sumcarbsDv + carbsDv
            fiber = round(i["Data"]["Fiber"]*uAmt)
            sumfiber = sumfiber + fiber
            fiberDv = round(fiber/25*100)
            sumfiberDv = sumfiberDv + fiberDv
            sugar = round(i["Data"]["Sugar Total"]*uAmt)
            sumsugar = sumsugar + sugar
            protein = round(i["Data"]["Protein"]*uAmt)
            sumprotein = sumprotein + protein
            vitA = round(i["Data"]["Vitamins"]["Vitamin A - RAE"]*uAmt/1000*100)
            sumvitA = sumvitA + vitA
            vitC = round(i["Data"]["Vitamins"]["Vitamin C"]*uAmt/60*100)
            sumvitC = sumvitC + vitC
            calcium = round(i["Data"]["Major Minerals"]["Calcium"]*uAmt/1100*100)
            sumcalcium = sumcalcium + calcium
            iron = round(i["Data"]["Major Minerals"]["Iron"]*uAmt/14*100)
            sumiron = sumiron + iron
            cal = sumfat*9 + sumcarbs*4 + sumprotein*4
            calfat = sumfat*9
            
    return render_template(
        "output.html",
        FoodName = uIng,
        Fat = sumfat, 
        FatDv = sumfatDv,
        SatFat = sumsatfat, 
        SatFatDv = sumsatfatDv, 
        Chole = sumchole, 
        CholeDv = sumcholeDv, 
        Sodium = sumsodium, 
        SodiumDv = sumsodiumDv, 
        Carbs = sumcarbs, 
        CarbsDv = sumcarbsDv,
        Fiber = sumfiber,
        FiberDv = sumfiberDv,
        Sugar = sumsugar,
        Protein = sumprotein,
        VitA = sumvitA,
        VitC = sumvitC,
        Calcium = sumcalcium,
        Iron = sumiron,
        Calories = cal,
        FatCalories = calfat)
    
if __name__=="__main__":
    app.run(debug=False)