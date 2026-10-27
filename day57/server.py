from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)

name = "joseph"





@app.route("/")
def index():
    random_number = random.randint(1, 10)
    current_year = datetime.now().year
    return render_template("index.html", num=random_number, year=current_year)


@app.route("/guess")
def guess():
    gender_response = requests.get("https://api.genderize.io", params={"name": name})
    age_response = requests.get("https://api.agify.io", params={"name": name})
    gender_content = gender_response.json()
    age_content = age_response.json()
    print(gender_content)
    user_gender = gender_content["gender"]
    user_age = age_content["age"]
    return render_template("guess.html", gender=user_gender, age=user_age, name=name.title())

@app.route("/blog/<num>")
def get_blog(num):
    print(num)
    blog_url = "https://api.npoint.io/c64c812990039adda3f3"
    response = requests.get(blog_url)
    all_posts = response.json()
    return render_template("blog.html",posts = all_posts)


if __name__ == '__main__':
    app.run(debug=True)
