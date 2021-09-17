import os
from flask import (
    Flask, flash, render_template, 
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash 
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")


#set up instance of PyMongo
mongo = PyMongo(app)


#------------- Home -----------------------
@app.route("/")
def home():
    recipes = list(mongo.db.recipes.find())
    recipe_tabs = list(mongo.db.recipes.find())
    return render_template("index.html", recipes=recipes, recipe_tabs=recipe_tabs)


#------------- Sign Up -----------------------
@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        #Check if the username already exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("signup"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        #put the new user in a session cookie
        session["user"] = request.form.get("username").lower()
        flash("Sign Up Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("signup.html")


#------------- Log in -----------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        #check if the username already exists in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            #check to see if hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome {}".format(request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))
            else:
                #Invalid password match
                flash("Invalid Username and/or Password")
                return redirect(url_for("login"))
        
        else:
            #Username does not exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))
                               
    return render_template("login.html")


#------------- User profile page -----------------------
@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    #retrieve the session user's username from the database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    
    recipes = mongo.db.recipes.find()

    if session["user"]:
        return render_template("profile.html", 
        username=username, recipes=recipes)

    return redirect(url_for("login"))


#------------- Log out -----------------------
@app.route("/logout")
def logout():
    #remove user session cookies
    flash("You Have Been Logged Out")
    session.pop("user")
    return redirect(url_for("login"))


#------------ Meat alternatives------------------
@app.route("/meat_alternatives")
def meat_alternatives():
    return render_template("meat_alternatives.html")


#------------ Milk alternatives------------------
@app.route("/milk_alternatives")
def milk_alternatives():
    return render_template("milk_alternatives.html")


#------------ Egg alternatives------------------
@app.route("/egg_alternatives")
def egg_alternatives():
    return render_template("egg_alternatives.html")


#------------- Recipes page -----------------------
@app.route("/find_recipes")
def find_recipes():
    recipes = list(mongo.db.recipes.find())
    return render_template("find_recipes.html", recipes=recipes)


#------------ Search Recipe ------------------------------
@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("find_recipes.html", recipes=recipes)


#------------- Individual recipe -----------------------
@app.route("/recipe/<recipe_id>")
def single_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one_or_404({"_id": ObjectId(recipe_id)})
    return render_template("single_recipe.html", recipe=recipe)


#------------- Add Recipe -----------------------
@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    categories = mongo.db.categories.find().sort("category_name", 1)

    if request.method == "POST":
        form_info = request.form.to_dict()
        recipe_ingredients_list = form_info["recipe_ingredients"].split("\n")
        recipe_method_list = form_info["recipe_method"].split("\n")
        new_recipe = {
            "category_name": form_info["category_name"],
            "recipe_title": form_info["recipe_title"],
            "recipe_summary": form_info["recipe_summary"],
            "recipe_servings": form_info["recipe_servings"],
            "recipe_ready_in": form_info["recipe_ready_in"],
            "recipe_calories": form_info["recipe_calories"],
            "recipe_ingredients": recipe_ingredients_list,
            "recipe_method": recipe_method_list,
            "recipe_image_url": form_info["recipe_image_url"],
            "created_by": session["user"]
            }
        mongo.db.recipes.insert_one(new_recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for("add_recipe"))

    return render_template("add_recipe.html", categories=categories)


#------------- Edit Recipe -----------------------
@app.route("/edit_recipe/<recipe_id>")
def edit_recipe(recipe_id):
    recipe = mongo.db.recipes.find_one_or_404({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)
    
    recipe_ingredients_list = [ingredient for ingredient
                                in recipe['recipe_ingredients']]
    
    recipe_instructions_list = [instruction for instruction
                                in recipe['recipe_method']]
    
    ingredients_text = "\n".join(recipe_ingredients_list)
    instructions_text = "\n".join(recipe_instructions_list)
    flash("Recipe Successfully Updated")
    return render_template("edit_recipe.html", 
                            recipe=recipe, 
                            categories=categories, 
                            ingredients=ingredients_text,
                            instructions=instructions_text)


#------------- Delete Recipe -----------------------
@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Has Been Deleted")
    return redirect(url_for("profile", username=session["user"]))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
