import os
from flask import (Flask, flash, render_template,
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


# set up instance of PyMongo
mongo = PyMongo(app)


@app.route("/")
def home():
    """------------- Home -----------------------"""
    recipes = list(mongo.db.recipes.find())
    recipe_tabs = list(mongo.db.recipes.find())
    return render_template("index.html",
                           recipes=recipes, recipe_tabs=recipe_tabs)


@app.route("/signup", methods=["GET", "POST"])
def signup():
    """------------- Sign Up -----------------------"""
    if request.method == "POST":
        # Check if the username already exists
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )

        if existing_user:
            flash("Username already exists")
            return redirect(url_for("signup"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password")),
        }
        mongo.db.users.insert_one(register)

        # put the new user in a session cookie
        session["user"] = request.form.get("username").lower()
        flash("Sign Up Successful!")
        return redirect(url_for("profile", username=session["user"]))
    return render_template("signup.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    """------------- Log in -----------------------"""
    if request.method == "POST":
        # check if the username already exists in the database
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()}
        )

        if existing_user:
            # check to see if hashed password matches user input
            if check_password_hash(
                existing_user["password"], request.form.get("password")
            ):
                session["user"] = request.form.get("username").lower()
                flash("Welcome {}".format(request.form.get("username")))
                return redirect(url_for("profile", username=session["user"]))
            else:
                # Invalid password match
                flash("Invalid Username and/or Password")
                return redirect(url_for("login"))

        else:
            # Username does not exist
            flash("Incorrect Username and/or Password")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    """------------- User profile page -----------------------"""
    # retrieve the session user's username from the database
    username = mongo.db.users.find_one(
               {"username": session["user"]})["username"]

    recipes = mongo.db.recipes.find()

    if session["user"]:
        return render_template("profile.html",
                               username=username, recipes=recipes)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    """------------- Log out -----------------------"""
    # remove user session cookies
    flash("You Have Been Logged Out")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/meat_alternatives")
def meat_alternatives():
    """------------ Meat alternatives route ------------------"""
    return render_template("meat_alternatives.html")


@app.route("/milk_alternatives")
def milk_alternatives():
    """------------ Milk alternatives------------------"""
    return render_template("milk_alternatives.html")


@app.route("/egg_alternatives")
def egg_alternatives():
    """------------ Egg alternatives------------------"""
    return render_template("egg_alternatives.html")


@app.route("/find_recipes")
def find_recipes():
    """------------- Search All Recipes page -----------------------"""
    recipes = list(mongo.db.recipes.find())
    return render_template("find_recipes.html", recipes=recipes)


@app.route("/search", methods=["GET", "POST"])
def search():
    """--------- Search Recipe view for find_recipes search query --------"""
    query = request.form.get("query")
    recipes = list(mongo.db.recipes.find({"$text": {"$search": query}}))
    return render_template("find_recipes.html", recipes=recipes)


@app.route("/recipe/<recipe_id>")
def single_recipe(recipe_id):
    """------------- View Individual recipe -----------------------"""
    recipe = mongo.db.recipes.find_one_or_404({"_id": ObjectId(recipe_id)})
    return render_template("single_recipe.html", recipe=recipe)


@app.route("/add_recipe", methods=["GET", "POST"])
def add_recipe():
    """------------- Add Recipe -----------------------"""
    categories = mongo.db.categories.find().sort("category_name", 1)

    if request.method == "POST":
        form_info = request.form.to_dict()
        # Split text area content on new line for ingredients and instructions
        recipe_ingredients_list = form_info["recipe_ingredients"].split("\n")
        recipe_method_list = form_info["recipe_method"].split("\n")

        # get recipe info from user input fields
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
            "created_by": session["user"],
        }
        mongo.db.recipes.insert_one(new_recipe)
        flash("Recipe Successfully Added")
        return redirect(url_for("add_recipe"))

    return render_template("add_recipe.html", categories=categories)


@app.route("/edit_recipe/<recipe_id>")
def edit_recipe(recipe_id):
    """------------ Edit Recipe -----------------"""
    recipe = mongo.db.recipes.find_one_or_404({"_id": ObjectId(recipe_id)})
    categories = mongo.db.categories.find().sort("category_name", 1)

    # create lists for ingredients and method
    recipe_ingredients_list = [
        ingredient for ingredient in recipe["recipe_ingredients"]
    ]

    recipe_instructions_list = [instruction for instruction
                                in recipe["recipe_method"]]

    # join list on new line
    ingredients_text = "\n".join(recipe_ingredients_list)
    instructions_text = "\n".join(recipe_instructions_list)
    flash("Recipe Successfully Updated")
    return render_template(
        "edit_recipe.html",
        recipe=recipe,
        categories=categories,
        ingredients=ingredients_text,
        instructions=instructions_text,
    )


@app.route("/delete_recipe/<recipe_id>")
def delete_recipe(recipe_id):
    """------------- Delete Recipe ---------------"""
    mongo.db.recipes.remove({"_id": ObjectId(recipe_id)})
    flash("Recipe Has Been Deleted")
    return redirect(url_for("profile", username=session["user"]))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")), debug=True)
