# Veggie Planet   

## Milestone Project 3 - Python and Data Centric Development 


[Link to Live Website](https://veggie-planet.herokuapp.com/)  
  

***   

## Index – Table of Contents  

  

* [About](#About) 

* [User Experience](#User-Experience)  

* [Features](#Game-Requirements)

* [Database](#Database)

* [Technologies](#Technologies) 

* [Testing](#Testing) 

* [Deployment](#Deployment)   

* [Acknowledgements](#Acknowledgements) 

  
*** 

## About    

  

Veggie Planet is a project that is intended to be used for the scope of this project, and also outside of this project scope. As a proponent of the vegan lifestyle, I found it quite challenging to source out individual websites that compile a large amount of vegan recipes from various international cuisines. This is why Veggie planet was created. Not only to be a useful resource of vegan recipes, but also promote the vegan food, movement and lifestyle. This site is still work in progress as far as content is concerned, but for the scope of this project, I have opted to primarily design it as a vegan recipe cookbook, by the users, for the users, in which a user can search existing recipes, and also add, edit and delete their own recipes. 


***  

  
## Demo 


Clicking on this [link](https://veggie-planet.herokuapp.com/) provides access to the live website 

<p align="center"> 

   <img src="static/img/site-responsiveness.png" alt="screenshot of responsive site"/> 

</p> 

***

## User Experience 

This site targets visitors who are interested in vegan recipes, and would like to share recipes of their own to contribute to the ever growing database of recipes 

### The Ideal Customer For This Site Is:
* Vegan looking for a collection of vegan recipes
* Vegan looking for more info about vegan food and lifestyle
* Vegan looking for alternatives to dairy, meat or general animal products
* Vegan seeking to promote awareness of the vegan diet
* Non-vegan looking to explore vegan food options
* Non-vegan seeking information on plant alternatives to try out

### Visitor Goals

* To be able to see different recipes and search for recipes using keywords.
* To create an account, be able to log into account.
* To be able to add, edit and delete user's own recipes and contribute to database of vegan recipes.
* To be able to easily navigate throughout the site through clean, interactive presentation
* Allow users to identify this site as a promising collection of vegan recips which are challenging to find compiled in a single site
* Most sites don't make a clear distinction between vegan and vegetarian

### Site Owner's Goals

* To promote vegan movement and vegan lifestyle
* To convince user that vegan food is very delicious.
* Allow user to know that alternatives are well within reach.
* Answer some common questions through use of video and pages dedicated to plant based alternatives.
* To enlighten users about the contribution they're making towards environment
* To highlight the health benefit of a vegan diet
* To highlight substitutes for carnivorous diets.

### Strategy

The design goal is to make a clear, intuitive, accessible, structured websitesite that allows visitors to easily find recipes, ingredients, and instructions, have clear call to action buttons encounraging users to register in order to add, edit and delete their own recipes. Links between various pages are intended to be very intuitive to allow for easy navigation.

### Scope

The site consists of a home page comprised of a navigation bar, with a number of options available for all users, and a profile option consisting of a dropdown menu, that is only available to registered users. The profile section allows access to the user's own profile on which they can view their contribution of recipes, with the choice to edit or delete said recipes. It also allows access to the "Add Recipe" page in which a user can add a recipe title, recipe summary, number of servings, calories per serving, cooking and preperation time, ingredients and instructions. The sign Up button only appears to non-registered users. 

The hero section features two buttons, search recipes and signup, the latter of which is only visible to non-registered users, and a prominent play button that enables a video to play of well-renowned vegan activist Ed Winters, A.K.A. earthling Ed, dissecting the logic used to prevent the switch to a vegan diet in one of his popular TED Talks, which I thought was a very powerful to answer a lot of questions in a non-accusatory manner and appeals to the listener's logic.

The about section features a short brief regarding the mission of this site, clearly stating that one of it's primary functions is to compile a large database of vegan recipes from all over the world, followed by a "Why go vegan" section featuring three cards providing a very short summary of the benefits of a vegan diet.

In order to not sound very preachy, the featured section is intended to remind the user that this is a recipe site, and designed to choose random recipes from the database and feature them on a weekly basis, including recipe title, recipe summary and an image of the dish.

Following that is a section featuring a carousel that helps the user find plant alternatives to the standard carnivorous options, regarding meat, milk and eggs, with a button taking the user to the relevant page which then outlines the variety of plant options that can be incorporated into recipes.

Below is a table outlining what is visible to members and non members:

| Nav Bar        | Logged In           | Logged out  |
| ------------- |:-------------:| -----:|
| Home      | ✔ | ✔ |
| Recipes | ✔      |    ✔ |
| Contact | ✔      |    ✔ |
| Signup | ❌      |    ✔ |
| Log in | ❌      |    ✔ |
| Log Out | ✔      |    ❌ |
| My Profile | ✔      |    ❌ |
| Add Recipe | ✔      |    ❌ |


Accessing the "My Profile" page enables user to edit or delete recipe, both of which are also options not availabe to non members

### Design Structure
The website used a template that is free to use by [BootstrapMade](https://bootstrapmade.com/) called Restaurantly, after receiving permission to use this template for the purposes of my project. I have however modified the template and tailored it to my own needs, using slightly different colour schemes and free/license-free images from [Unsplash](https://unsplash.com/). The template comes with a few libraries including bootstrap, animate css for smooth animations, swiper touch slider, but I have also decided to use AOS on-scroll animation library, glightbox for interactive image animations on hover.

### Fonts
Three fonts from google fonts have been used to embed the following fonts: 

* "Poppins" for H1's that have been made to have a small font for a more modern feel. 
* "Playfair Display" for headers, which in fact are a further elaboration of the H1 title, and 
* "Open Sans" for content including paragraphs, list items including recipe methods, ingredients and Navbar list items.  

### Colours

The main colours used were various shades of black using RGBA, and in order to break the contrast, #cda45e, a version of beige has been used for buttons, headers, borders of a variety of elements including input fields.

### Icons

I have used [Font Awesome](https://fontawesome.com/) for all of the icons I have used throughout the website.

***

## Features

### Existing Features

* See overview of multiple recipes, by displaying title, summary, image, servings and cooking time
* See specific recipe details by clicking on view recipe button
* Clear, intuitive page navigation
* Call to action buttons on header, hero section and alternatives section guiding the user toward's site's intended goals
* Educational features presented using interactive elements such as slider, cards, and video button
* play button giving user to play video concerning common arguments regarding veganism.
* Use of images and scroll animations for a greater user experience
* Register account, log in and log out features
* View, add, edit and delete recipes, and view individual recipes
* Contact form requesting user's name, email, subject and message and a send button
* Header with logo and navigation list items that exists on every page of the site
* Footer section that exists on every page throughout the site

### Features To Be Incorporated In The Future

* Using vegan recipe API for a rich database
* Allow users to search recipes based on categories
* Allow users to comment on recipes 
* Incorporate blog to allow members to discuss relevant matters
* Incorporate share features to allow users to share recipes and pages on social media
* Favourite button that allows users to save preferred recipes and view saved recipes on their profiles
* Provide print-only version of recipes that allows users to print favourite recipes
* Incorporate section that allows users to enter available ingredients and suggest a recipe based on entered ingredients
* Integrate FAQ page for more commonly asked questions.
* Change site language option to draw in more users from all around the globe

***

## Database
* The database chosen for this is a non-relational database hosted on MongoDB.
* The application uses 2 database collections, 'categories' and 'recipes'.
* The basic information of each recipe (category, recipe_title, recipe_summary, recipe_servings, recipe_ready_in and calories) is stored as a key value whilst the content of the ingredients and instructions for each recipe are stored as an array.
* The idea behind the array is to be able to better structure the output of the ingredients and instructions data in the recipe view.
* This is achieved by the user segregating each ingredient/instruction in the add/edit recipe form using a line break (hit enter after each ingredient/instruction).
* The user is instructed to do this via the placeholder text in the applicable textarea on the edit/add recipe page.
* The textarea content is then split using "/n" and saved as an array in the database.
* The reverse is applied "/n.join" to pre-populate the textarea formfields when editing a recipe.
* The view recipe page applies a for each function to combine each array item into a collection of ingredienst/instructions to the user.
* This also felt like a better user experience since the other option was to add "add ingredient/method" and "remove ingredient/method" buttons which would make for a more tedious experience.
***

## Technologies

### Languages

* HTML
* CSS
* JavaScript
* Python

### Libraries & Frameworks

* Bootstrap
* Animate.css
* Aos scroll animations
* Swiper.js
* jQuery
* PyMongo
* Flask
* Jinja
* Werkzeug

### Wireframes

* Balsamiq
* Adobe Photoshop 

### Tools

* Adobe Photoshop - Wireframe and save images for web
* Tinypng - Compress images for faster loading
* [Imgbb](https://imgbb.com/) - To store images and get image URLs for recipes
* Gitpod - Writing code
* EmailJs - Turning user form input into email received
* Github - Repository
* Heroku - Host for project deployment
* MongoDb - Database used for website
* VSCode & Atom - For testing out tricky code prior to writing on Gitpod

***

## Testing

### Bug fixes
The website had a number of prominent bugs. The navigation options for "About" and "Contact were broken". This has been taken care of and the contact forms on both the contact page and the index page successfully sumbit visitor messages and forward them to my personal email address as displayed below:

<p align="center"> 

   <img src="static/img/email-confirmation.png" alt="screenshot of email confirmation when form is submitted"/> 

</p>

The other major bug was that updating a recipe produced a server error. This was mainly due to the fact that an if statement for the post method was not provided in the edit_recipe view, and also a discrepancy in the naming of the fields that will be updated on the database. When the methods were successfully handled, a bug still existed in that the submitted recipes would still not show up on the user's profile page, due to the "created_by" field being missing, so the view had no way of knowing that the submitted recipe belongs to the session user. This has been amended and the entire CRUD functionality is working seamlessly.

### HTML & CSS Testing

* I have used [W3C Makrkup Validator](https://validator.w3.org/) to validate HTML code
* I have used [W3C CSS Validator](https://jigsaw.w3.org/css-validator/validator) to validate HTML code

<p align="center"> 

   <img src="static/img/index-validator-error.png" alt="screenshot of HTML Validation"/> 

</p>

<p align="center"> 

   <img src="static/img/css-val.png" alt="screenshot of CSS validation"/> 

</p>


The website passed all validation tests, but however displayed a warning for not using a h1 tag as a top level header only. However, I have dismissed this warning as this is how the theme is intended and styled, where the h1 tag appears to be with a smaller font than proceeding tags, due to the styling applied to it for a modern look and feel to the website. Otherwise, there have been no errors.

For Javascript testing, I have used a [JS Linter](https://jshint.com/). The results only showed warnings, but no errors were found

<p align="center"> 

   <img src="static/img/jslinter.png" alt="js linter report"/> 

</p>

My python code was tested with the [PEP8 Linter](http://pep8online.com/) and passed all tests

<p align="center"> 

   <img src="static/img/pep8.png" alt="pep8 compliance report"/> 

</p>

All pages on the site passed through Lighthouse in Chrome developer tools

<p align="center"> 

   <img src="static/img/lighthouse1.png" alt="lighthouse report"/> 

</p>

<p align="center"> 

   <img src="static/img/lighthouse2.png" alt="lighthouse report"/> 

</p>

<p align="center"> 

   <img src="static/img/lighthouse3.png" alt="lighthouse report"/> 

</p>

<p align="center"> 

   <img src="static/img/lighthouse4.png" alt="lighthouse report"/> 

</p>

<p align="center"> 

   <img src="static/img/lighthouse5.png" alt="lighthouse report"/> 

</p>


### Manual Testing

The design goal is to make a clear, accessible, structured site so that visitors can easily read the displayed recipes, make an account and add, edit and delete their own recipes.

On small and medium devices the menu can be accessed through the hamburger menu, on large devices the navigation menu is always visible. There is a difference between the menu for a user who is not logged in and a user who is logged in. The signup call to action button disappears, the logged out user is left with the option to signup or login, while the logged in user is given the option to view profile, add recipe or log out.

<p align="center"> 
   <img src="static/img/logged-in-user-menu.png" alt="screenshot of menu for logged in user"/> 
   <img src="static/img/logged-out-user-menu.png" alt="screenshot of menu for logged out user"/> 
</p>

And on the desktop version..

<p align="center"> 
   <img src="static/img/logged-in-hero.png" alt="screenshot of hero section for logged in user"/> 
</p>

<p align="center"> 
   <img src="static/img/logged-out-hero.png" alt="screenshot of hero section for logged out user"/> 
</p>

#### The visitor goals are:

* To be able to search for recipe using keyword, and be told that no results were found should the keyword entered be invalid

<p align="center"> 
   <img src="static/img/search-query.png" alt="screenshot of search recipe"/> 
</p>

<p align="center"> 
   <img src="static/img/invalid-search.png" alt="screenshot of invalid search query"/> 
</p>

In order to log in or signup, the user has to meet certain criteria in order to be validated. The forms work as expected and produce a message prompting the user to meet the input criteria, i.e. no spaces allowed, or special characters in the username. The input fields also have a minimum and maximum length

<p align="center"> 
   <img src="static/img/invalid-login.png" alt="screenshot of invalid login"/> 
</p>

<p align="center"> 
   <img src="static/img/invalid-signup.png" alt="screenshot of hero section for invalid signup"/> 
</p>

If a username already exists on signup, or if a user enters incorrect username and/or password, a flash message prompts the user to that event, requiring the user to try again.


Once a user is logged in, they are directed to their own profile page, where a flash message greets the user, and the submitted recipes are presented in the form of cards, 4 of which stack in a row on large screen, 2 cards per screen on medium devices and one card per screen on mobile devices. If the user hasn't submitted any entries yet, that is relayed through a message on the profile page

<p align="center"> 
   <img src="static/img/profile.png" alt="screenshot of hero section for logged out user"/> 
</p>

<p align="center"> 
   <img src="static/img/profile-no-input.png" alt="screenshot of hero section for logged out user"/> 
</p>

When a registered user decides to add a recipe, they are required to complete fields for the recipe name, summary, number of servings, cooking and preparation time, estimated calories per serving, ingredients and method, the latter two were created as text areas that prompt the user to press enter after every entry, and the add recipe route in turn splits the entries at each new line and creates a list of ingredients/steps. I have opted for this method in order to generate a greater user experience, where I initially opted for an "Add ingredient" button and a "Remove ingredient" button for the ingredients, and "add" and "remove" buttons for the instructions. I found this method to be quite cumbersome for the user.

<p align="center"> 
   <img src="static/img/add-recipe1.png" alt="screenshot of hero section for logged out user"/> 
</p>

<p align="center"> 
   <img src="static/img/add-recipe2.png" alt="screenshot of hero section for logged out user"/> 
</p>

The edit recipe section relies on the edit_recipe route, which re-populates the user's entries, and rejoins the individual ingredients and instructions at each new line, allowing for a seamless entry that can be up to 3000 characters long.

<p align="center"> 
   <img src="static/img/edit-recipe1.png" alt="screenshot of hero section for logged out user"/> 
</p>

<p align="center"> 
   <img src="static/img/edit-recipe2.png" alt="screenshot of hero section for logged out user"/> 
</p>

On the home page, the about section contains a brief message about the site's mission, and the intention to spread the message.. This is reinforced by three brief cards that summarise the main benefits of choosing a vegan diet.

<p align="center"> 
   <img src="static/img/mission.png" alt="screenshot of hero section for logged out user"/> 
</p>

<p align="center"> 
   <img src="static/img/whyvegan.png" alt="screenshot of hero section for logged out user"/> 
</p>

<p align="center"> 
   <img src="static/img/alternatives.png" alt="screenshot of hero section for logged out user"/> 
</p>

<p align="center"> 
   <img src="static/img/alternatives2.png" alt="screenshot of hero section for logged out user"/> 
</p>

Each of the swiper elements is visible for 20 seconds, and three of them allow the user to further navigate to see plant alternatives for meat, milk and eggs and how they can be utilised to achieve the desired taste and or/ cooking effect..

<p align="center"> 
   <img src="static/img/alternatives3.png" alt="screenshot of hero section for logged out user"/> 
</p>

<p align="center"> 
   <img src="static/img/alternatives4.png" alt="screenshot of hero section for logged out user"/> 
</p>


***

## Deployment

### To find the repository:

1. Go to [Motaz's Github](https://github.com/moutaz3003) .. https://github.com/moutaz3003
2. go to repositories.
3. Find the repository for "Veggie Planet"
4. Click on the link on the right in the "About" section

### To View live link:

1. Go to readme file
2. Click on "Live demo" link at the very top of the readme.md file

### Run local:

If you would like to run this website locally you can clone this repository in an IDE such as VSCode. Make sure that PIP3, Flask, Python3 and Git are installed. Set up your account for MongoDB Atlas.

<p align="center"> 
   <img src="static/img/github.png" alt="screenshot of github repository"/> 
</p>

1. Log into Github
2. Find moutaz3003 account
3. Find the "Veggie Planet Repository"
4. Click on "Code"
5. Copy the code shown
6. Open up gitpod or preferred IDE
7. Type git clone https://github.com/moutaz3003/veggie-planet.git
8. create database on MongoDB then create application around it
9. create cluster then create collections for users, recipes and category names
10. inside each collection, insert document with key:value pairs (eg. recipe_name: "chickpea curry")


### Flask:
------

### In the terminal:
---------------
- install flask using "pip3 install flask"
- create python file which will be the foundation of application using "touch app.py"
- storing sensitive data which needs to be hidden using environment variables .. So touch env.py

### in env.py:
----------
inside env.py, we need to hide several pieces of data, to do that:
- first import os to set our default environment variable

setting up environment variables takes 2 arguments:
- first is the variable name to get the confidential data
- second is the actual data itself, so:

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")  .. port 5000 is the standard port used for flask applications

- Then we need to set up secret key, which is required whenever we use the flash and session functions in flask
os.environ.setdefault("SECRET_KEY", "password of choice")

- Then set up variable to connect to the mongo database:
os.environ.setdefault("MONGO_URI", "database connection URI"

- then add variable to the mongo database name:
os.environ.setdefault("MONGODB_NAME", "cook_book" or any name of choice) .. cook_book is the name of the database created earlier

- Save env.py file

***

### In app.py:
-------
- import os
- from flask import Flask .. importing Flask class from flask app

- in order to use environment variables, we need to import env package. Since we are not going to push 
the env.py file to GitHub, once our app is deployed to Heroku, it won't be able to find 
the env.py file, so it will throw an error. This is why we need to only import env if the os can find 
an existing file path for the env.py file itself, so:

So:

if os.path.exists("env.py"):
	import env

- create an instance of flask and store it in a variable called app:
app = Flask(__name__)

- create a test app to see if the set up is working:
@app.route("/")
def hello_world():
	return "Any string"

- The host will be set to the IP, so we need to type os.environ.get("IP") in order to fetch the default value
which was "0.0.0.0"

- The port will need to be converted to an integer, so we'll type: int(os.environ.get("PORT")).
- Don't forget to separate each parameter with a comma.

if __name__ == "__main__":
	app.run(host=os.environ.get("IP"), 
	port=int(os.environ.get("PORT")),
	debug=True
	)

*** 

### Heroku:
-------
- Before creating heroku application, we need to set up some dependencies that heroku needs to run the app.. This 
will be created in the requirements.txt file:

pip3 freeze --local > requirements.txt

- Then set up procfile that heroku looks for to know which file runs the app and how to run it.

echo:web python app.py > Procfile

-Head over to Heroku.com
- New --> Create new app

- To connect app, we can do one of a few things. For simplicity, connect to Github repository.

- Type in repository name as it appears on github, then Search

- Once it finds repository, click connect.

- Before Deploying, since some environment variables are hidden in the env.py file, Heroku will not be able
to find them.. 

- Therefore, click on settings tab --> Reveal config vars

- when inserting the config vars, make sure to not include any quotes for either the keys or values

insert keys and their values as per the env.py file.
IP -> 0.0.0.0
PORT -> 5000
SECRET_KEY -> secret key
MONGO_URI -> Mongo URI link
MONGO_DBNAME -> cook_book (name of database)

- Before deploying, we need to push the two files that we created first.
- add, commit and push the requirements.txt and Procfile seperately
- git add requirements.txt
- git commit -m "Add requirements.txt"
- git push
- git add Procfile
- git commit -m "Add Procfile"
- git push

- Then on Heroku deployment page, click "Deploy Branch".

- Once app has been built, click view to see successful deployment of app

- Any changes pushed on github from there on should be displayed on Heroku

*** 

# Wiring up database to flask application:
---------------------------------------

- For flask to communicate with Mongo, we need to install a third party library called flask-pymongo:
pip3 install flask-pymongo

- Need to install a package called dnspython in order to use the Mongo SRV connection string
pip3 install dnspython

- with every package installed, it's important to update requirements.txt for heroku to know we require more to
run the app.. This again can be achieved with the command:
pip3 freeze --local > requirements.txt

## In the app.py file:
------------------
- update it with the newly installed packages by importing them:
- from flask_pymongo import Pymongo
- from bson.objectid import ObjectId .. this allows us to rended json like object for mongodb to find them

- Then we need to add some configurations after the app variable:
app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME") 
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY") .. requirement when using some functions from flask


- Since we havent got the mongo URI connection string stored, we need to go back to mongodb website
overview -> connect --> connect your application

- copy the link provided, modify angle brackets to own clustername, password and database name
then paste that into quotes for mongoURI in env.py file

- update the heroku config var for MONGO_URI by pasting that link also

- We need to setup an instance of PyMongo, and add the app into that using something called
a constructor method, so type: 
mongo = PyMongo(app)

- This is the Flask 'app' object we've defined above, and is the final step to ensure our
Flask app is properly communicating with the Mongo database.


- we will import some additional functionalities from flask which we will use later.. These are:
flash, render_template, redirect, session, and url_for

- in the function under the route decorator, instead of returning hello world, we want it to render a template called
insertname.html

- On this tasks template, we want to be able to generate data from our collection
on MongoDB, visible to our users, so before return statement:

example = mongo.db.example.find()

- Along with the rendering of the example.html template, we'll pass that tasks variable through to
the template: example=example, where the first is a variable that the template will use.


----------------------------------------------------------------------------------------------------------------
### Template creation:
------------------
Flask looks for all HTML template files placed within a directory at the root-level called 'templates', plural.
So create that directory from the terminal using the 'make directory' command: "mkdir templates".

inside the templates folder, we will create your .html page

----------------------------------------------------------------------------------------------------------------
### Security using Werkzeug:
-----------------------
in appy.py:

from werkzeug.security import generate_password_hash, check_password_hash

this is important for generating password hash, and checking password hashes. 


***

## Acknowledgements

1. I would like to thank my Mentor Brian Macharia for his continued support and willingness to make time for me, and go back to the drawing board with me and walk me through code and coding logic.

2. I would like to thank my family who have been supportive and understanding.

3. I would like to thank my girlfriend Merve, who gave me the inspiration to embark on this project, which I'm sure will grow with time.

4. Brian Traversy's youtube channel

5. Kyle Webdev simplified for explaining code in a very watered down easy to understand manner.

5. Unsplash for the free images

6. Bootstrapmade for giving me the licence to use and modify one of their beautiful themes

7. I would like to thank Sean, Mikklos and everyone in the Code Institute tutor support team to help me grasp python which was very confusing to me at first, but they have been very patient with me and always followed up on problems raised.